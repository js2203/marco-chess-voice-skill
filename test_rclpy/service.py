
from string_interfaces.srv import MARCO

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(MARCO, 'MARCO', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        if request.req == 'Hello':
            response.res = 'Hi'
        else:
            response.res = 'no'
        self.get_logger().info('Incoming request\n{}'.format(
            request.req))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()