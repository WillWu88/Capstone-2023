import rclpy
import time
from rclpy.node import Node
import drivers.encoder_driver
from rpm_server.action import RPM

class RpmActionServer(Node):

    def __init__(self,size):
        super().__init__('rpm_service')
        self.size = 5
        self.encoder = drivers.encoder_driver.EncoderDriver(self.size)
        self.action_server = ActionServer(
            self,
            RPM,
            'rpm readings',
            self.rpm_callback)

    def rpm_callback(self, request, response):

        self.get_logger().info('Reading RPM...')

        # feedback here
        feedback_msg = RPM.Feedback()
        feedback_msg.instant = self.encoder.CalcFilter()
        goal_handle.publish_feedback(feedback_msg)

        self.encoder.update()
        goal_handle.succeed()
        # results below
        self.get_logger().info('Data read!')
        response = RPM.Result()
        response.filtered = self.encoder.CalcFilter()
        response.raw = self.encoder.latest
        return response


def main(args=None):
    rclpy.init(args=args)

    rpm_service = RpmActionServer()

    rclpy.spin(rpm_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
