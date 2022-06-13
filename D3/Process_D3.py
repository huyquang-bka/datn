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


class ProcessD3Thread(QtCore.QThread):
    def __init__(self, queue_D3, queue_D3_process):
        super().__init__()
        # id
        self.__thread_active = False
        self.queue_D3 = queue_D3
        self.queue_D3_process = queue_D3_process

    def run(self):
        self.__thread_active = True
        print('Starting Process D3...')
        while self.__thread_active:
            if not self.queue_D3.qsize() >= 1:
                time.sleep(0.001)
                continue
            frame = self.queue_D3.get()
            if self.queue_D3_process.qsize() < 1:
                self.queue_D3_process.put(frame)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False