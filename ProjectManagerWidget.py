import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from Gui.ui_project_manager import Ui_ProjectManagerForm

class ProjectManagerWidget(QWidget):
     def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_ProjectManagerForm()
        self.ui.setupUi(self) 