import random
import time
# QT
from PyQt5 import QtCore
import os
import cv2
import numpy as np

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"


class ProcessDigitThread(QtCore.QThread):
    def __init__(self, queue_lp_process):
        super().__init__()

        self.weight_path = "YOLO_v4_file/lp.weights"
        self.cfg_path = "YOLO_v4_file/base_data_tiny.cfg"
        self.class_path = "YOLO_v4_file/obj.names"
        self.net = cv2.dnn.readNet(self.weight_path, self.cfg_path)
        self.classes = self.get_classes()
        self.scale = 1 / 255.
        self.size = (224, 224)
        self.conf_threshold = 0.5
        self.nms_threshold = 0.4
        self.queue_lp_process = queue_lp_process

    def get_classes(self):
        with open(self.class_path, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        return self.classes

    def get_output_layers(self, net):
        layer_names = net.getLayerNames()

        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return output_layers

    def is_square_lp(self, image):
        return image.shape[1] / image.shape[0] <= 2

    def process_square_lp(self, bboxes):
        line_1 = []
        line_2 = []
        all_y = [box[1] for box in bboxes]
        if len(all_y) == 0:
            return []
        average_y = sum(all_y) / len(all_y)
        for bbox in bboxes:
            if bbox[1] < average_y:
                line_1.append(bbox)
            else:
                line_2.append(bbox)
        line_1 = sorted(line_1, key=lambda x: x[0])
        line_2 = sorted(line_2, key=lambda x: x[0])
        return line_1 + line_2

    def run(self):
        self.__thread_active = True
        print('Starting Digits Thread...')
        count = 0
        lp_list = []
        count_missing_lp = 0
        while self.__thread_active:
            if self.queue_lp_process.qsize() < 1:
                count_missing_lp += 1
                if count_missing_lp > 25:
                    count_missing_lp = 0
                    if not lp_list:
                        continue
                    lp_most_dict = {}
                    print("lp_list: ", lp_list)
                    lp_set = set(lp_list)
                    for lp in lp_set:
                        lp_most_dict[lp_list.count(lp)] = lp
                    lp_final = lp_most_dict[max(lp_most_dict.keys())]
                    print(lp_final)
                    lp_list = []
                time.sleep(0.001)
                continue
            lp_dict = self.queue_lp_process.get()
            img = lp_dict['image']
            count += 1
            for key in lp_dict.keys():
                if key == 'image':
                    continue
                x1, y1, x2, y2, x1_crop, y1_crop, x2_crop, y2_crop = lp_dict[key]
                car_crop = img[y1:y2, x1:x2]
                image = car_crop[y1_crop:y2_crop, x1_crop:x2_crop]
                Width = image.shape[1]
                Height = image.shape[0]
                blob = cv2.dnn.blobFromImage(image, self.scale, self.size, (0, 0, 0), True, crop=False)

                self.net.setInput(blob)

                outs = self.net.forward(self.get_output_layers(self.net))

                class_ids = []
                confidences = []
                boxes = []

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > self.conf_threshold:
                            center_x = int(detection[0] * Width)
                            center_y = int(detection[1] * Height)
                            w = int(detection[2] * Width)
                            h = int(detection[3] * Height)
                            x = center_x - w / 2
                            y = center_y - h / 2
                            class_ids.append(class_id)
                            confidences.append(float(confidence))
                            boxes.append([x, y, w, h])

                indices = cv2.dnn.NMSBoxes(boxes, confidences, self.conf_threshold, self.nms_threshold)

                bboxes = []

                for i in indices:
                    i = i[0]
                    box = list(map(int, boxes[i]))
                    x = box[0]
                    y = box[1]
                    w = box[2]
                    h = box[3]
                    bboxes.append([x, y, w, h, confidences[i], class_ids[i]])

                bboxes = sorted(bboxes, key=lambda x: x[0])
                is_square = self.is_square_lp(image)
                if is_square:
                    bboxes = self.process_square_lp(bboxes)
                lp_text = ""
                for bbox in bboxes:
                    x, y, w, h, confidence, class_id = bbox
                    lp_text += self.classes[class_id]
                lp_text = lp_text.upper()
                if len(lp_text) < 7:
                    lp_text = ""
                lp_list.append(lp_text)
                cv2.imshow("image", cv2.resize(image, dsize=None, fx=5, fy=5))
                cv2.waitKey(1)

    def stop(self):
        print('Stopping Processing Thread')

        self.__thread_active = False
