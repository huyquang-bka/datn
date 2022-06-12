import sys
import time
import torch
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from test_window import Ui_MainWindow
import cv2
from PyQt5.QtGui import QBrush, QColor, QImage, QPainter, QPen
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.W, self.H = self.uic.img4.width() * 2, self.uic.img4.height() * 2

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))

        painter.drawLine(0, self.H // 2 + 2, self.W, self.H // 2 + 2)
        painter.drawLine(self.W // 2 + 2, 0, self.W // 2 + 2, self.H)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
