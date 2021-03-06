# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import cv2
from PyQt5.QtGui import QPixmap
from Camera.D3_Camera import D3_Camera_Item
from Camera.D5_Camera import D5_Camera_Item
from Camera.LP_Camera import LP_Camera_Item


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bg_colors = ["gray", "beige", "tan", "silver"]
        self.setupUi()
        self.camera_items_dict = {1: D5_Camera_Item(), 2: D3_Camera_Item(), 3: LP_Camera_Item()}
        self.grid_layout_cameras_dict = {}
        for k in [2, 3]:
            self.grid_layout_cameras_dict[k] = QtWidgets.QGridLayout()
            self.grid_layout_cameras_dict[k].setContentsMargins(0, 0, 0, 0)
            self.grid_layout_cameras_dict[k].addWidget(self.camera_items_dict[k], 0, 0, 1, 1)
            self.frame_camera_dict[k].setLayout(self.grid_layout_cameras_dict[k])
            self.camera_items_dict[k].start()

    def show_frame(self, frame_camera, current_frame):
        if current_frame is not None:
            rgb_img = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            qt_img = QPixmap.fromImage(
                QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
                frame_camera.width(), frame_camera.height())
            frame_camera.setPixmap(qt_img)
            frame_camera.setScaledContents(True)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.layout_main = QtWidgets.QGridLayout(self.centralwidget)
        self.layout_main.setObjectName("layout_main")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.frame_camera_dict = {}
        for i in range(1, 5):
            self.frame_camera_dict[i] = QtWidgets.QLabel(self.centralwidget)
            sizePolicy.setHeightForWidth(self.frame_camera_dict[i].sizePolicy().hasHeightForWidth())
            self.frame_camera_dict[i].setSizePolicy(sizePolicy)
            self.frame_camera_dict[i].setStyleSheet(f"background: {self.bg_colors[i - 1]};")

        self.layout_main.addWidget(self.frame_camera_dict[1], 0, 1, 1, 1)
        self.layout_main.addWidget(self.frame_camera_dict[2], 0, 2, 1, 1)
        self.layout_main.addWidget(self.frame_camera_dict[3], 1, 2, 1, 1)
        self.layout_main.addWidget(self.frame_camera_dict[4], 1, 1, 1, 1)

        self.menu = QtWidgets.QLabel(self.centralwidget)
        self.menu.setMinimumSize(QtCore.QSize(128, 0))
        self.menu.setFrameShape(QtWidgets.QLabel.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QLabel.Raised)
        self.menu.setObjectName("menu")
        self.layout_menu = QtWidgets.QGridLayout(self.menu)
        self.layout_menu.setObjectName("layout_menu")
        self.btn_search = QtWidgets.QPushButton(self.menu)
        self.btn_search.setObjectName("btn_search")
        self.layout_menu.addWidget(self.btn_search, 2, 0, 1, 1)
        self.line = QtWidgets.QLabel(self.menu)
        self.line.setFrameShape(QtWidgets.QLabel.HLine)
        self.line.setFrameShadow(QtWidgets.QLabel.Sunken)
        self.line.setObjectName("line")
        self.layout_menu.addWidget(self.line, 3, 0, 1, 1)
        self.btn_info_table = QtWidgets.QPushButton(self.menu)
        self.btn_info_table.setObjectName("btn_info_table")
        self.layout_menu.addWidget(self.btn_info_table, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QLabel(self.menu)
        self.line_2.setFrameShape(QtWidgets.QLabel.HLine)
        self.line_2.setFrameShadow(QtWidgets.QLabel.Sunken)
        self.line_2.setObjectName("line_2")
        self.layout_menu.addWidget(self.line_2, 5, 0, 1, 1)
        self.btn_view_2d_map = QtWidgets.QPushButton(self.menu)
        self.btn_view_2d_map.setObjectName("btn_view_2d_map")
        self.layout_menu.addWidget(self.btn_view_2d_map, 0, 0, 1, 1)
        self.layout_main.addWidget(self.menu, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_info_table.setText(_translate("MainWindow", "View Information"))
        self.btn_view_2d_map.setText(_translate("MainWindow", "View 2D map"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
