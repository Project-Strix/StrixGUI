# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_loader_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_imageLoaderForm(object):
    def setupUi(self, imageLoaderForm):
        if not imageLoaderForm.objectName():
            imageLoaderForm.setObjectName(u"imageLoaderForm")
        imageLoaderForm.setWindowModality(Qt.NonModal)
        imageLoaderForm.resize(2044, 1740)
        self.gridLayout_3 = QGridLayout(imageLoaderForm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(30)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.radioButton_17 = QRadioButton(imageLoaderForm)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout_4.addWidget(self.radioButton_17, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.radioButton_18 = QRadioButton(imageLoaderForm)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_4.addWidget(self.radioButton_18, 2, 3, 1, 1)

        self.label_17 = QLabel(imageLoaderForm)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(imageLoaderForm)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_16 = QLabel(imageLoaderForm)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.comboBox_8 = QComboBox(imageLoaderForm)
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_4.addWidget(self.comboBox_8, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(imageLoaderForm)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 4, 1, 1)

        self.comboBox_7 = QComboBox(imageLoaderForm)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_4.addWidget(self.comboBox_7, 1, 4, 1, 1)

        self.radioButton_16 = QRadioButton(imageLoaderForm)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_4.addWidget(self.radioButton_16, 2, 1, 1, 1)

        self.label_13 = QLabel(imageLoaderForm)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 16777215))
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 1, 3, 1, 1)

        self.label_15 = QLabel(imageLoaderForm)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_14 = QLabel(imageLoaderForm)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_4)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_24 = QLabel(imageLoaderForm)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_11 = QLabel(imageLoaderForm)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 2)

        self.label_12 = QLabel(imageLoaderForm)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 1, 1, 1)

        self.checkBox_3 = QCheckBox(imageLoaderForm)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_2.addWidget(self.checkBox_3, 1, 5, 1, 2)

        self.line_2 = QFrame(imageLoaderForm)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 7, 1, 1)

        self.comboBox_6 = QComboBox(imageLoaderForm)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 1, 2, 1, 3)

        self.label_10 = QLabel(imageLoaderForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)

        self.comboBox_5 = QComboBox(imageLoaderForm)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 2, 2, 1, 3)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.checkBox = QCheckBox(imageLoaderForm)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_9 = QCheckBox(imageLoaderForm)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(imageLoaderForm)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(imageLoaderForm)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_2.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(imageLoaderForm)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_2.addWidget(self.checkBox_12)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.listWidget = QListWidget(imageLoaderForm)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.toolButton = QToolButton(imageLoaderForm)
        self.toolButton.setObjectName(u"toolButton")
        icon = QIcon()
        icon.addFile(u"E:/icon/icons8-plus-math-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)

        self.gridLayout.addWidget(self.toolButton, 0, 0, 1, 1)

        self.toolButton_2 = QToolButton(imageLoaderForm)
        self.toolButton_2.setObjectName(u"toolButton_2")
        icon1 = QIcon()
        icon1.addFile(u"E:/icon/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon1)

        self.gridLayout.addWidget(self.toolButton_2, 3, 0, 1, 1)

        self.toolButton_3 = QToolButton(imageLoaderForm)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon2 = QIcon()
        icon2.addFile(u"E:/icon/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon2)

        self.gridLayout.addWidget(self.toolButton_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.toolButton_4 = QToolButton(imageLoaderForm)
        self.toolButton_4.setObjectName(u"toolButton_4")
        icon3 = QIcon()
        icon3.addFile(u"E:/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon3)

        self.gridLayout.addWidget(self.toolButton_4, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(30, 30, 30, 30)
        self.comboBox_4 = QComboBox(imageLoaderForm)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.line_4 = QFrame(imageLoaderForm)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.widget = QWidget(imageLoaderForm)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 300))

        self.verticalLayout_4.addWidget(self.widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(imageLoaderForm)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(2, 8)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 6)

        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(imageLoaderForm)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_9.addWidget(self.pushButton)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.currentStepInfo_2 = QLabel(imageLoaderForm)
        self.currentStepInfo_2.setObjectName(u"currentStepInfo_2")

        self.verticalLayout_7.addWidget(self.currentStepInfo_2)

        self.infoListWidget_2 = QListWidget(imageLoaderForm)
        self.infoListWidget_2.setObjectName(u"infoListWidget_2")
        self.infoListWidget_2.setMinimumSize(QSize(0, 100))

        self.verticalLayout_7.addWidget(self.infoListWidget_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_9.setStretch(0, 3)
        self.verticalLayout_9.setStretch(1, 3)
        self.verticalLayout_9.setStretch(2, 9)
        self.verticalLayout_9.setStretch(3, 1)
        self.verticalLayout_9.setStretch(4, 4)

        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)


        self.retranslateUi(imageLoaderForm)

        QMetaObject.connectSlotsByName(imageLoaderForm)
    # setupUi

    def retranslateUi(self, imageLoaderForm):
        imageLoaderForm.setWindowTitle(QCoreApplication.translate("imageLoaderForm", u"Form", None))
        self.radioButton_17.setText(QCoreApplication.translate("imageLoaderForm", u"2.5D\uff08C * W * H *3\uff09", None))
        self.radioButton_18.setText(QCoreApplication.translate("imageLoaderForm", u"3D\uff08C * W * H * S\uff09", None))
        self.label_17.setText(QCoreApplication.translate("imageLoaderForm", u"\u7ef4\u5ea6\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\u7c7b\u578b\uff1a", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("imageLoaderForm", u"float32", None))

        self.radioButton_16.setText(QCoreApplication.translate("imageLoaderForm", u"2D\uff08C * W * H\uff09", None))
        self.label_13.setText(QCoreApplication.translate("imageLoaderForm", u"\u6807\u6ce8\u7c7b\u578b\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("imageLoaderForm", u"ImageKey\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("imageLoaderForm", u"MaskKey\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("imageLoaderForm", u"\u6570\u636e\u52a0\u8f7d", None))
        self.label_11.setText(QCoreApplication.translate("imageLoaderForm", u"\uff08\u901a\u9053\u6570\u5728\u7b2c\u4e00\u7ef4\uff09", None))
        self.label_12.setText(QCoreApplication.translate("imageLoaderForm", u"\u6807\u6ce8\uff1a", None))
        self.checkBox_3.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\u4e0e\u6807\u6ce8\u52a0\u8f7d\u65b9\u6cd5\u76f8\u540c", None))
        self.label_10.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("imageLoaderForm", u"\u6570\u636e\u901a\u9053\u64cd\u4f5c", None))
        self.checkBox_9.setText(QCoreApplication.translate("imageLoaderForm", u"\u65b9\u4f4d\u8f6c\u6362", None))
        self.checkBox_10.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\u88c1\u526a\u589e\u8865", None))
        self.checkBox_11.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\u5f52\u4e00\u5316", None))
        self.checkBox_12.setText(QCoreApplication.translate("imageLoaderForm", u"\u6570\u636e\u6269\u589e", None))
        self.toolButton.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.toolButton_4.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("imageLoaderForm", u"\u6dfb\u52a0", None))
        self.pushButton.setText(QCoreApplication.translate("imageLoaderForm", u"\u5b8c\u6210", None))
        self.currentStepInfo_2.setText(QCoreApplication.translate("imageLoaderForm", u"Output\uff1a", None))
    # retranslateUi

