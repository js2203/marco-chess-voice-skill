import rclpy
import asyncio
from rclpy.node import Node

from std_msgs.msg import String
from string_interface.srv import MARCO
import threading


class IdentityCollector(Node):

    def __init__(self):
        super().__init__('identity_subscriber')
        self.subscription = self.create_subscription(
            String,
            'Identity',
            self.listener_callback,
            10)

        self.srv = self.create_service(
            MARCO,
            'MARCO_identity',
            self.request_current_identity)

        self.subscription
        self.collection = {}
        self.BackgroundDeletion(self)

    def request_current_identity(self, request, response):
        try:
            response.res = max(self.collection, key=self.collection.get)
        except ValueError:
            response.res = 'NoFace'
        return response

    def listener_callback(self, msg):
        key = str(msg.data)
        try:
            self.collection[key] += 1
        except KeyError:
            self.collection[key] = 1
        self.get_logger().info('{}'.format(self.collection))

    class BackgroundDeletion(object):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

        def run(self):
            asyncio.run(self.clear_dict())

        async def clear_dict(self):
            while True:
                self.outer_instance.collection = {}
                await asyncio.sleep(10)


def main(args=None):
    rclpy.init(args=args)

    identity_collector = IdentityCollector()
    rclpy.spin(identity_collector)
    identity_collector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
