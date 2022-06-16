import cv2
from widget_layout.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import pyqtSignal
from widget_layout.map_2d import Ui_map2D
from widget_layout.layout_search_2 import Ui_Layout_Search
from Database.utils import Database
from PyQt5 import QtWidgets
from PyQt5 import QtCore


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

        self.database = Database()

        self.show()

    def slot_apply(self):
        plate = self.layout_search.txt_plate.text()
        brand = self.layout_search.txt_brand.text()
        color = self.layout_search.txt_color.text()
        result_dict = self.database.get_info({'plate': plate, 'brand': brand, 'color': color})

        if result_dict:
            img_path = result_dict[list(result_dict.keys())[0]]['img_path']
            img = cv2.imread(img_path)
            self.show_frame(self.layout_search.qlabel_crop_frame, img)

    def slot_cancel(self):
        self.layout_search.hide()

    def slot_view_2d_map(self):
        self.map_2d.hide()
        self.map_2d.move(100, 200)
        self.map_2d.show()

    def slot_search(self):
        plates = self.database.get_plate_list()
        colors = self.database.get_color_list()
        brands = self.database.get_brand_list()
        print(plates, colors, brands)

        completer_plate = QtWidgets.QCompleter(plates, self)
        completer_plate.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer_color = QtWidgets.QCompleter(colors, self)
        completer_color.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer_brand = QtWidgets.QCompleter(brands, self)
        completer_brand.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.layout_search.txt_plate.setCompleter(completer_plate)
        self.layout_search.txt_color.setCompleter(completer_color)
        self.layout_search.txt_brand.setCompleter(completer_brand)

        self.layout_search.hide()
        self.layout_search.move(200, 300)
        self.layout_search.show()

    def slot_car_info_from_lp(self, car_info):
        print(car_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
