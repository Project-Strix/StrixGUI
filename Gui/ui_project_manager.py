# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ProjectManagerForm(object):
    def setupUi(self, ProjectManagerForm):
        if not ProjectManagerForm.objectName():
            ProjectManagerForm.setObjectName(u"ProjectManagerForm")
        ProjectManagerForm.setWindowModality(Qt.NonModal)
        ProjectManagerForm.resize(1822, 1378)
        self.verticalLayoutWidget = QWidget(ProjectManagerForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 40, 1701, 1281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 60))

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))

        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 60))

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ProjectManagerForm)

        QMetaObject.connectSlotsByName(ProjectManagerForm)
    # setupUi

    def retranslateUi(self, ProjectManagerForm):
        ProjectManagerForm.setWindowTitle(QCoreApplication.translate("ProjectManagerForm", u"ProjectManager", None))
        self.label_2.setText(QCoreApplication.translate("ProjectManagerForm", u"\u5b58\u50a8\u4f4d\u7f6e\uff1a", None))
        self.label.setText(QCoreApplication.translate("ProjectManagerForm", u"\u9879\u76ee\u540d\u79f0\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("ProjectManagerForm", u"\u6d4f\u89c8...", None))
    # retranslateUi

