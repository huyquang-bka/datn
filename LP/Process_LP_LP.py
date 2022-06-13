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
from detect_yolov5 import Detection
from LP.Polygon import detect_zone


class ProcessLP_LPThread(QtCore.QThread, Detection):
    def __init__(self, queue_tracking, queue_LP, queue_lp_process):
        super().__init__()
        # id
        self.__thread_active = False
        self.queue_tracking = queue_tracking
        self.queue_lp = queue_LP
        self.queue_lp_process = queue_lp_process

    def run(self):
        weight_path = r"weights/lp_final.pt"
        classes = [0]
        conf = 0.7
        imgsz = 256
        device = "0"
        self.setup_model(weight_path, classes, conf, imgsz, device)
        self.__thread_active = True
        print('Starting Process LP LP...')
        while self.__thread_active:
            if not self.queue_tracking.qsize() >= 1:
                QtCore.QThread.msleep(1)
                continue
            lp_dict = {}
            id_dict = self.queue_tracking.get()
            image = id_dict['image']
            image_copy = image.copy()
            cv2.polylines(image, [detect_zone], True, (0, 255, 0), 2)
            for id in id_dict.keys():
                if id == 'image':
                    continue
                x1, y1, x2, y2, category = id_dict[id]
                is_in_detect_zone = cv2.pointPolygonTest(detect_zone, ((x1 + x2) // 2, y2), False)
                if is_in_detect_zone < 1:
                    continue
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                crop = image_copy[y1:y2, x1:x2]
                list_lp = self.detect(crop)
                for lp in list_lp:
                    x1_, y1_, x2_, y2_, cls = lp
                    lp_dict[id] = [x1, y1, x2, y2, x1_, y1_, x2_, y2_]

            if self.queue_lp.qsize() < 1:
                self.queue_lp.put(image)
            if self.queue_lp_process.qsize() < 1:
                lp_dict['image'] = image_copy
                self.queue_lp_process.put(lp_dict)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
