# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'layout_info_car_group_box.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info_Car(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(500, 300)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("background: beige")
        self.groupBox.setObjectName("Car Info")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.qlabel_brand = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_brand.sizePolicy().hasHeightForWidth())
        self.qlabel_brand.setSizePolicy(sizePolicy)
        self.qlabel_brand.setMinimumSize(QtCore.QSize(0, 30))
        self.qlabel_brand.setMaximumSize(QtCore.QSize(16777215, 30))
        self.qlabel_brand.setStyleSheet("background: white")
        self.qlabel_brand.setObjectName("qlabel_brand")
        self.qlabel_brand.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.qlabel_brand, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        # self.label.setStyleSheet("background: white")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.qlabel_out_time = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_out_time.sizePolicy().hasHeightForWidth())
        self.qlabel_out_time.setSizePolicy(sizePolicy)
        self.qlabel_out_time.setMinimumSize(QtCore.QSize(0, 30))
        self.qlabel_out_time.setMaximumSize(QtCore.QSize(16777215, 30))
        self.qlabel_out_time.setStyleSheet("background: white")
        self.qlabel_out_time.setObjectName("qlabel_out_time")
        self.qlabel_out_time.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.qlabel_out_time, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        # self.label.setStyleSheet("background: white")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        # self.label.setStyleSheet("background: white")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.qlabel_plate = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_plate.sizePolicy().hasHeightForWidth())
        self.qlabel_plate.setSizePolicy(sizePolicy)
        self.qlabel_plate.setMinimumSize(QtCore.QSize(0, 30))
        self.qlabel_plate.setMaximumSize(QtCore.QSize(16777215, 30))
        self.qlabel_plate.setStyleSheet("background: white")
        self.qlabel_plate.setObjectName("qlabel_plate")
        self.qlabel_plate.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.qlabel_plate, 1, 1, 1, 1)
        self.qlabel_frame = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_frame.sizePolicy().hasHeightForWidth())
        self.qlabel_frame.setSizePolicy(sizePolicy)
        self.qlabel_frame.setMinimumSize(QtCore.QSize(200, 200))
        self.qlabel_frame.setStyleSheet("background: white")
        self.qlabel_frame.setObjectName("qlabel_frame")
        self.gridLayout.addWidget(self.qlabel_frame, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        # self.label.setStyleSheet("background: white")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.qlabel_in_time = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_in_time.sizePolicy().hasHeightForWidth())
        self.qlabel_in_time.setSizePolicy(sizePolicy)
        self.qlabel_in_time.setMinimumSize(QtCore.QSize(0, 30))
        self.qlabel_in_time.setMaximumSize(QtCore.QSize(16777215, 30))
        self.qlabel_in_time.setStyleSheet("background: white")
        self.qlabel_in_time.setObjectName("qlabel_in_time")
        self.qlabel_in_time.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.qlabel_in_time, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        # self.label.setStyleSheet("background: white")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.qlabel_color = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_color.sizePolicy().hasHeightForWidth())
        self.qlabel_color.setSizePolicy(sizePolicy)
        self.qlabel_color.setMinimumSize(QtCore.QSize(0, 30))
        self.qlabel_color.setMaximumSize(QtCore.QSize(16777215, 30))
        self.qlabel_color.setStyleSheet("background: white")
        self.qlabel_color.setObjectName("qlabel_color")
        self.qlabel_color.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.qlabel_color, 2, 1, 1, 1)
        # self.qlabel_frame_other = QtWidgets.QLabel(self.groupBox)
        # self.qlabel_frame_other.setMinimumSize(QtCore.QSize(240, 215))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.qlabel_frame_other.sizePolicy().hasHeightForWidth())
        # self.qlabel_frame_other.setSizePolicy(sizePolicy)
        # self.qlabel_frame_other.setStyleSheet("background: white")
        # self.qlabel_frame_other.setObjectName("qlabel_frame_other")
        # self.gridLayout.addWidget(self.qlabel_frame_other, 0, 2, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Car Info", "Car Info"))
        self.groupBox.setTitle(_translate("Car Info", "Car Info"))
        self.qlabel_brand.setText(_translate("self", "qlabel_brand"))
        self.label_6.setText(_translate("self", "Out time"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_out_time.setText(_translate("self", "Out time"))
        self.label_4.setText(_translate("self", "Brand"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText(_translate("self", "Plate"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_plate.setText(_translate("self", "qlabel_plate"))
        self.qlabel_frame.setText(_translate("self", "frame"))
        self.qlabel_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setText(_translate("self", "In time"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_in_time.setText(_translate("self", "In time"))
        self.label_3.setText(_translate("self", "Color"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.qlabel_color.setText(_translate("self", "qlabel_color"))
        # self.qlabel_frame_other.setText(_translate("self", "frame"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Info_Car()
    ui.show()
    sys.exit(app.exec_())

