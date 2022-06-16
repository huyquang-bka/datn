from widget_layout.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import pyqtSignal
from widget_layout.map_2d import Ui_map2D
from widget_layout.layout_search import Ui_Layout_Search


class MainWindow(Ui_MainWindow):
    sig_view_2d_map = pyqtSignal(bool)
    sig_view_info = pyqtSignal(bool)
    sig_search = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.map_2d = Ui_map2D()
        self.layout_search = Ui_Layout_Search()

        self.btn_view_2d_map.clicked.connect(self.slot_view_2d_map)
        self.btn_search.clicked.connect(self.slot_search)

        self.layout_search.btn_apply.clicked.connect(self.slot_apply)
        self.layout_search.btn_cancel.clicked.connect(self.slot_cancel)

        self.camera_items_dict[3].process_digit.sig_car_info.connect(self.slot_car_info_from_lp)

        self.show()

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

    def slot_car_info_from_lp(self, car_info):
        print(car_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
