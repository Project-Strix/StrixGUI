# from signal import signal
# from sqlite3 import connect
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Gui.ui_mainwnd import Ui_MainWindow
from ImageLoaderWidget import ImageLoaderWidget
from ProjectManagerWidget import ProjectManagerWidget
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.interfaces_btns = [self.ui.imageLoaderPushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4]
        self.init_interfaces()
    
    def init_interfaces(self):
        for index in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.removeWidget(self.ui.stackedWidget.widget(0))
        print(self.ui.stackedWidget.count())
        self.image_preprocess_widget = ImageLoaderWidget(self)
        self.ui.stackedWidget.addWidget(self.image_preprocess_widget)
        self.ui.stackedWidget.addWidget(ProjectManagerWidget(self))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.imageLoaderPushButton.clicked.connect(lambda: self.on_btn_clicked(self.ui.imageLoaderPushButton, 0))
        self.ui.pushButton_2.clicked.connect(lambda: self.on_btn_clicked(self.ui.pushButton_2, 1))
        self.ui.pushButton_3.clicked.connect(lambda: self.on_btn_clicked(self.ui.pushButton_3, 2))
        self.ui.pushButton_4.clicked.connect(lambda: self.on_btn_clicked(self.ui.pushButton_4, 3))
        self.ui.imageLoaderPushButton.setStyleSheet("background-color: #2da8fe;")
        
      
    def on_btn_clicked(self, btn, index):
        print(btn)
        if index < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(index)
        for temp_btn in self.interfaces_btns:
            temp_btn.setStyleSheet("background-color: #465364;")
        btn.setStyleSheet("background-color: #2da8fe;")
                

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    win = MainWindow()
    win.setWindowTitle("StrixGUI")
    win.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
    app.exit(app.exec_())
