import rclpy
from rclpy.node import Node

from example_interface.srv import AddTwoInts

class RPMService(Node):

    def __init__(self):
        super().__init__('rpm_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def get_rpm_callback(self, request, response):
        # ------- Find a way to get the request and response for the rpm ---
        response.sum = request.a + request.b 
        self.get_logger().info('Incoming request\n a: %d b: %d' % (request.a, request.b)) 

        return response

def main(args=None):
    rclpy.init(args=args)

    rpm_service = RPMService()

    rclpy.spin(rpm_service)

    rclpy.shutdown()

if __name__== '__main__':
    main()

