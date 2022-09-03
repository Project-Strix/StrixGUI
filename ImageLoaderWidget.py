import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from Gui.ui_image_loader_form import Ui_imageLoaderForm

class ImageLoaderWidget(QWidget):
     def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_imageLoaderForm()
        self.ui.setupUi(self) 



