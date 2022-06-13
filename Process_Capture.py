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
import time


class ProcessCaptureThread(QtCore.QThread):
    def __init__(self, queue_capture, rtsp_url, camera_id):
        super().__init__()
        # id
        self.camera_id = camera_id
        self.__thread_active = False
        self.cap = cv2.VideoCapture(rtsp_url)
        self.queue_capture = queue_capture

    def run(self):
        self.__thread_active = True
        print('Starting Process Capture...')
        count = 0
        while self.__thread_active:
            count += 1
            s = time.time()
            ret, frame = self.cap.read()
            if not ret:
                break
            if self.queue_capture.qsize() < 1:
                cv2.putText(frame, str(count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                self.queue_capture.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False