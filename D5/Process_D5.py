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


class ProcessD5Thread(QtCore.QThread):
    def __init__(self, queue_D5, queue_D5_process):
        super().__init__()
        # id
        self.__thread_active = False
        self.queue_D5 = queue_D5
        self.queue_D5_process = queue_D5_process

    def run(self):
        self.__thread_active = True
        print('Starting Process D5...')
        while self.__thread_active:
            if not self.queue_D5.qsize() >= 1:
                time.sleep(0.001)
                continue
            frame = self.queue_D5.get()
            if self.queue_D5_process.qsize() < 1:
                self.queue_D5_process.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
