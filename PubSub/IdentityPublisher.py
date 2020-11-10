import asyncio
import os
import threading
from glob import glob

import tensorflow as tf
import cv2
import numpy as np
from PIL import Image

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def cut_faces(image, faces_coord):
    faces = []
    for (x, y, w, h) in faces_coord:
        faces.append(image[y: y + h, x: x + w])

    return faces


def resize(images, size=(224, 224)):
    images_norm = []
    for image in images:
        if image.shape < size:
            image_norm = cv2.resize(image, size,
                                    interpolation=cv2.INTER_AREA)
        else:
            image_norm = cv2.resize(image, size,
                                    interpolation=cv2.INTER_CUBIC)
        images_norm.append(image_norm)

    return images_norm


def normalize_faces(image, faces_coord):
    faces = cut_faces(image, faces_coord)
    faces = resize(faces)

    return faces


class webcam_detection():

    def __init__(self, model_path: str):
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        assert len(
            physical_devices) > 0, "Not enough GPU hardware devices available"
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        self.model = tf.keras.models.load_model(model_path)
        self.predicted_name = 'unknown'

    def identity_detection(self):

        classifier = cv2.CascadeClassifier(
            './haarcascade_frontalface_default.xml')

        classes = []
        for name in glob('../FaceDetection/src/people/train/*'):
            classes.append(os.path.basename(name))
        label = sorted(classes)

        # Initialize Webcam
        video_capture = cv2.VideoCapture(0)

        while True:

            _, frame = video_capture.read()

            faces = classifier.detectMultiScale(
                frame,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(100, 100),
                flags=cv2.CASCADE_SCALE_IMAGE)

            if faces == ():
                self.predicted_name = 'NoFace'
                pass
            else:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),
                                  2)
                faces_only = normalize_faces(frame, faces)
                for face in faces_only:
                    image = Image.fromarray(face, 'RGB')
                    image_array = np.array(image, dtype=np.float32)
                    image_array /= 255
                    # image_array /= 127.5
                    # image_array -= 1
                    image_array = np.expand_dims(image_array, axis=0)
                    prediction = self.model.predict(image_array)

                    if prediction[0][np.argmax(prediction)] > 10.0:
                        self.predicted_name = label[np.argmax(prediction)]
                    else:
                        self.predicted_name = 'unknown Face'

                cv2.putText(frame,
                            self.predicted_name,
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (0, 255, 0),
                            2)

            cv2.imshow('Detection', frame)

            if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break

        video_capture.release()
        cv2.destroyAllWindows()


class BackgroundPublisher(object):

    def __init__(self, outer_instance):
        self.outer_instance = outer_instance
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        rclpy.init(args=None)
        identity_publisher = IdentityPublisher(self.outer_instance)
        rclpy.spin(identity_publisher)
        identity_publisher.destroy_node()
        rclpy.shutdown()


class IdentityPublisher(Node):

    def __init__(self, outer_instance):
        super().__init__('identity_publisher')
        self.publisher_ = self.create_publisher(String, 'Identity', 10)
        self.outer_instance = outer_instance
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.emotion_callback)

    def emotion_callback(self):
        msg = String()
        msg.data = self.outer_instance.predicted_name
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


if __name__ == '__main__':

    Detector = webcam_detection('C:\\Users\\janni\\Desktop\\BA\\BA_src\\FaceDetection\\src\weights\\vgg16_linear_11-06-2020-17_04.h5')
    BackgroundPublisher(Detector)
    Detector.identity_detection()
