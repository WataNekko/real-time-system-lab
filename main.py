#!/usr/bin/env python3

print("Hello LAB2")
import time
from scheduler import *
from ai_task import *
from task3 import *
from camera import *

import cv2  # Install opencv-python


# "O(n)" scheduler
# scheduler = Scheduler()

# "O(1)" scheduler on Update
scheduler = Scheduler2()

scheduler.SCH_Init()


class TimerTask:
    def __init__(self):
        pass

    def run(self):
        print(f"At time: {self.timer}")
        self.timer += 1



    timer = 0


task3 = Task3()
timer_task = TimerTask()


cam1 = Camera(0, "Laptop Cam")
cam2 = Camera(1, "Phone Cam")
lap_task = Aitask(cam1.get_image);
phone_task = Aitask(cam2.get_image)

scheduler.SCH_Add_Task(lap_task.run, 1000, 2000)
scheduler.SCH_Add_Task(phone_task.run, 2000, 4000)
scheduler.SCH_Add_Task(task3.Task3_Run, 3000, 1000)
scheduler.SCH_Add_Task(timer_task.run, 0, 1000)

prev_time = time.time()
curr_time = prev_time
while True:
    cam1.show_image()
    cam2.show_image()

    curr_time = time.time()
    if curr_time - prev_time >= 1:
        scheduler.SCH_Update()
        scheduler.SCH_Dispatch_Tasks()
        prev_time = curr_time
