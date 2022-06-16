# QT
from PyQt5 import QtCore
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import cv2
from utils_huy_quang.detect_yolov5 import Detection
from D3.Polygon import detect_zone


class ProcessShowThread(QtCore.QThread, Detection):
    def __init__(self, queue_tracking, queue_lp, queue_show):
        super().__init__()
        # id
        self.__thread_active = True

        # queues
        self.queue_tracking = queue_tracking
        self.queue_lp = queue_lp
        self.queue_show = queue_show

    def run(self):
        self.__thread_active = True
        print('Starting Process LP LP...')
        while self.__thread_active:
            if not self.queue_tracking.qsize() >= 1:
                QtCore.QThread.msleep(1)
                continue
            id_dict = self.queue_tracking.get()
            image = id_dict['image']
            image_copy = image.copy()
            # cv2.polylines(image, [detect_zone], True, (0, 255, 0), 2)
            cv2.fillPoly(image, [detect_zone], (0, 255, 0))
            image = cv2.addWeighted(image, 0.2, image_copy, 0.8, 0)
            for id in id_dict.keys():
                if id == 'image':
                    continue
                x1, y1, x2, y2, category = id_dict[id]
                is_in_detect_zone = cv2.pointPolygonTest(detect_zone, ((x1 + x2) // 2, y2), False)
                if is_in_detect_zone < 1:
                    continue
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(image, str(id), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if self.queue_show.qsize() < 1:
                self.queue_show.put(image)
            QtCore.QThread.msleep(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
