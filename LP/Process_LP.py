import random
import time
# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from PyQt5.QtCore import pyqtSignal

import sys
import os
import numpy as np
import cv2
from detect_yolov5 import Tracking
from queue import Queue


class ProcessLPThread(QtCore.QThread, Tracking):
    def __init__(self, queue_capture, queue_tracking):
        super().__init__()
        # id
        self.__thread_active = False
        self.queue_capture = queue_capture
        self.queue_tracking = queue_tracking

    def run(self):
        weight_path = r"weights/yolov5s.pt"
        classes = [2, 5]
        conf = 0.7
        imgsz = 640
        device = "0"
        self.setup_model(weight_path, classes, conf, imgsz, device)
        self.__thread_active = True
        print('Starting Process LP...')
        while self.__thread_active:
            if not self.queue_capture.qsize() >= 1:
                time.sleep(0.001)
                continue
            frame = self.queue_capture.get()
            id_dict = self.detect(frame)
            # for id in id_dict.keys():
            #     x1, y1, x2, y2, category = id_dict[id]
            #     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #     cv2.putText(frame, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if self.queue_tracking.qsize() < 1:
                id_dict['image'] = frame
                self.queue_tracking.put(id_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False


if __name__ == '__main__':
    queue_1 = Queue()
    queue_2 = Queue()
    process = ProcessLPThread(queue_1, queue_2)
    process.start()
