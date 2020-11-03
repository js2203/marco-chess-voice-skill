import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from string_interface.srv import MARCO


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)

        self.srv = self.create_service(MARCO, 'MARCO',
                                       self.add_two_ints_callback)
        self.subscription  # prevent unused variable warning
        self.incoming = ''

    def add_two_ints_callback(self, request, response):
        if request.req == 'Hello':
            response.res = 'Hi'
        else:
            response.res = self.incoming
        self.get_logger().info('Incoming request\n{}'.format(
            request.req))

        return response

    def listener_callback(self, msg):
        self.incoming = msg.data
        self.get_logger().info('I heard: "%s"' % msg.data)




def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
