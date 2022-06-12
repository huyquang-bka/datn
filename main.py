from main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import pyqtSignal
from map_2d import Ui_map2D
from layout_search import Ui_Layout_Search
from PyQt5.QtGui import QBrush, QColor, QImage, QPainter, QPen
from PyQt5.QtCore import Qt


class MainWindow(Ui_MainWindow):
    sig_view_2d_map = pyqtSignal(bool)
    sig_view_info = pyqtSignal(bool)
    sig_search = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.map_2d = Ui_map2D()
        self.layout_search = Ui_Layout_Search()

        # Button Main Window
        self.btn_view_2d_map.clicked.connect(self.slot_view_2d_map)
        self.btn_search.clicked.connect(self.slot_search)

        # Button Map 2D

        # Button Layout Search
        self.layout_search.btn_apply.clicked.connect(self.slot_apply)
        self.layout_search.btn_cancel.clicked.connect(self.slot_cancel)

        # self.W, self.H = self.img4.width() * 2, self.img4.height() * 2

        self.show()
    #
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
    #
    #     painter.drawLine(0, self.H // 2 + 2, self.W, self.H // 2 + 2)
    #     painter.drawLine(self.W // 2 + 2, 0, self.W // 2 + 2, self.H)

    def slot_apply(self):
        plate = self.layout_search.txt_plate.text()
        brand = self.layout_search.txt_brand.text()
        color = self.layout_search.txt_color.text()
        print(plate, brand, color)

    def slot_cancel(self):
        self.layout_search.hide()

    def slot_view_2d_map(self):
        self.map_2d.hide()
        self.map_2d.move(100, 200)
        self.map_2d.show()

    def slot_search(self):
        self.layout_search.hide()
        self.layout_search.move(200, 300)
        self.layout_search.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
