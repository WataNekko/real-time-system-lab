#pip install adafruit-io
import random
import time
import sys
from Adafruit_IO import  MQTTClient

class Task3:
    client = None
    def __init__(self):
        print("Init task 3")

        AIO_USERNAME = "hehevgu"
        AIO_KEY = "aio_YRzI97ePRcWVeCtAeHqkWhXBBGS8"

        self.client = MQTTClient(AIO_USERNAME, AIO_KEY)

        self.client.connect()
        self.client.loop_background()
        return

    def Task3_Run(self):
        print("Task 3 is running!!!")
        value = random.randint(0, 100)
        self.client.publish("Camera recognition", value)


