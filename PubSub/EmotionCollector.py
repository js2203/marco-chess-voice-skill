import rclpy
import asyncio
from rclpy.node import Node

from std_msgs.msg import String
from string_interface.srv import MARCO
import threading


class EmotionCollector(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'Emotion',
            self.listener_callback,
            10)

        self.srv = self.create_service(
            MARCO,
            'MARCO_emotion',
            self.request_current_emotion)

        self.subscription
        self.incoming = 'Nothing'
        self.collection = {}
        self.BackgroundDeletion(self)

    def request_current_emotion(self, request, response):
        response.res = max(self.collection, key=self.collection.get)

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
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()
            self.outer_instance = outer_instance

        def run(self):
            asyncio.run(self.clear_dict())

        async def clear_dict(self):
            while True:
                self.outer_instance.collection = {}
                await asyncio.sleep(10)


def main(args=None):
    rclpy.init(args=args)

    emotion_collector = EmotionCollector()
    rclpy.spin(emotion_collector)
    emotion_collector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
