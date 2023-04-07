/*
** I2C RPM peripheral driver code
** by Will Wu <willwu@wustl.edu>
**
** Last modified: Mar 29th, 2023
** References:
** - Pi Pico I2C memory example (https://github.com/raspberrypi/pico-examples/blob/1c5d9aa567598e6e3eadf6d7f2d8a9342b44dab4/i2c/slave_mem_i2c/slave_mem_i2c.c)
*/

#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
#include "hardware/gpio.h"
#include "hardware/i2c.h"
#include "pico/i2c_slave.h"
#include <stdio.h>

#define HALL_SENSOR 28
#define SCL 3
#define SDA 2
#define CIRC_BUFF_SIZE 3
#define TIME_CONV 1000000.0
#define RPM_MULT 20.0
#define BIT_MASK 255
#define BIT_SHIFT 256

const static uint PERIPHERAL_ADDR = 0x17;
const static uint I2C_BAUDRATE = 10000;
const static uint32_t zero_upp = 10000000;

static struct peripheral{
    uint32_t latest_time;
    uint32_t mov_avg[CIRC_BUFF_SIZE];
    uint8_t send_buff[sizeof(uint32_t)/sizeof(uint8_t)];
    uint8_t test_buff[sizeof(uint32_t)/sizeof(uint8_t)];
    uint zero_out_timer;
    int write_ptr;
    bool filter;
} encoder;

static void initPeripheral(struct peripheral *circ_buff){
    circ_buff->latest_time = 0;
    for (int i = 0; i < CIRC_BUFF_SIZE; i++){
        circ_buff->mov_avg[i] = 0;
    }
    size_t upp = sizeof(uint32_t)/sizeof(uint8_t);
    for (size_t n = 0; n < upp; n++){
        circ_buff->send_buff[n] = 0;
        circ_buff->test_buff[n] = 1;
    }
    circ_buff->write_ptr = 0;
    circ_buff->filter = true;
    circ_buff->zero_out_timer = 0;
}
static void updatePeripheral(struct peripheral *circ_buff, uint32_t new_val){
    circ_buff->mov_avg[circ_buff->write_ptr] = new_val;
    circ_buff->latest_time = new_val;
    circ_buff->write_ptr++;
    if (circ_buff->write_ptr >= CIRC_BUFF_SIZE){
        circ_buff->write_ptr = 0;
    }
}

static uint32_t CalcRaw(struct peripheral *circ_buff, uint32_t start, uint32_t stop){
    updatePeripheral(circ_buff, stop - start);
    return circ_buff->latest_time;
}

static uint32_t CalcFilter(struct peripheral *circ_buff){
    uint32_t ret = 0;
    for (int i = 0; i < CIRC_BUFF_SIZE; i++){
        ret += circ_buff->mov_avg[i];
    }
    return ret/5;
}

static float CalcRPM(struct peripheral *circ_buff){
    float avg_t = (float) CalcFilter(circ_buff);
    if (avg_t == 0.0){
        return 0.0;
    }
    float ret = RPM_MULT/(avg_t / TIME_CONV);
    return ret;
}

static uint32_t myPow(uint32_t base, uint exp){
    if (!exp){
        return 1;
    }
    return base * myPow(base, exp-1);
}


static void FormatBuff(const uint32_t base, uint8_t* send_buff){
    size_t upp = sizeof(uint32_t)/sizeof(uint8_t);
    for (size_t n = 0; n < upp; n++){
        send_buff[n] = (base & (BIT_MASK * myPow(BIT_SHIFT, n))) >> n*upp;
    }
}

static void FormatSend(struct peripheral *circ_buff){
    if (circ_buff->filter){
        FormatBuff(CalcFilter(circ_buff), circ_buff->send_buff);
    } else {
        FormatBuff(circ_buff->latest_time, circ_buff->send_buff);
    }
}

static void zeroTimer(struct peripheral *circ_buff){
    if (circ_buff->zero_out_timer >= zero_upp){
        // reset circular buffer after a period of untrigger
        for (int i = 0; i < CIRC_BUFF_SIZE; i++){
            circ_buff->mov_avg[i] = 0;
        }
        circ_buff->zero_out_timer = 0;
    } else {
        circ_buff->zero_out_timer++;
    }
}

static void peripheral_handler(i2c_inst_t *i2c, i2c_slave_event_t event) {
    switch (event) {
    case I2C_SLAVE_RECEIVE: // manager has written some data
        encoder.filter = i2c_read_byte_raw(i2c);
        break;
    case I2C_SLAVE_REQUEST: // manager is requesting data
        //FormatSend(&encoder);
        i2c_write_raw_blocking(i2c, encoder.test_buff, (sizeof(encoder.latest_time)/sizeof(uint8_t)));
        break;
    case I2C_SLAVE_FINISH: // manager has signalled Stop / Restart
        initPeripheral(&encoder);
        break;
    default:
        break;
    }
}

static void i2cSet() {
    i2c_init(i2c1, I2C_BAUDRATE);
    // configure I2C1 for slave mode
    //i2c_set_slave_mode(i2c1, true, PERIPHERAL_ADDR);
    i2c_slave_init(i2c1, PERIPHERAL_ADDR, &peripheral_handler);

    gpio_init(SDA);
    gpio_set_function(SDA, GPIO_FUNC_I2C);
    gpio_pull_up(SDA);

    gpio_init(SCL);
    gpio_set_function(SCL, GPIO_FUNC_I2C);
    gpio_pull_up(SCL);
    printf("I2C set\n");

}

int main() {
    stdio_init_all();
    cyw43_arch_init();
    // read from sensor
    gpio_init(HALL_SENSOR);
    gpio_set_dir(HALL_SENSOR, GPIO_IN);
    gpio_pull_up(HALL_SENSOR);

    initPeripheral(&encoder);
    uint32_t start, stop;
    int curr_pin_val, last_val;
    last_val = gpio_get(HALL_SENSOR);
    start = time_us_32();

    printf("Setting I2C...");
    //i2cSet();
    while (true) {
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1); // turn on led

        curr_pin_val = gpio_get(HALL_SENSOR);
        if (!(curr_pin_val) && last_val){
            stop = time_us_32();
            updatePeripheral(&encoder, CalcRaw(&encoder, start, stop));
            last_val = curr_pin_val;
            start = stop;
        } else {
            last_val = curr_pin_val;
        }

        printf("%f\n", CalcRPM(&encoder));
    }
}
