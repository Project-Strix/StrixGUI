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

        self.dim25dRadioButton = QRadioButton(imageLoaderForm)
        self.dim25dRadioButton.setObjectName(u"dim25dRadioButton")

        self.gridLayout_4.addWidget(self.dim25dRadioButton, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.dim3dRadioButton = QRadioButton(imageLoaderForm)
        self.dim3dRadioButton.setObjectName(u"dim3dRadioButton")

        self.gridLayout_4.addWidget(self.dim3dRadioButton, 2, 3, 1, 1)

        self.label_17 = QLabel(imageLoaderForm)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)

        self.imageKeyLineEdit = QLineEdit(imageLoaderForm)
        self.imageKeyLineEdit.setObjectName(u"imageKeyLineEdit")

        self.gridLayout_4.addWidget(self.imageKeyLineEdit, 0, 1, 1, 1)

        self.label_16 = QLabel(imageLoaderForm)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 1)

        self.imageTypeComboBox = QComboBox(imageLoaderForm)
        self.imageTypeComboBox.addItem("")
        self.imageTypeComboBox.setObjectName(u"imageTypeComboBox")

        self.gridLayout_4.addWidget(self.imageTypeComboBox, 1, 1, 1, 1)

        self.maskKeyLineEdit = QLineEdit(imageLoaderForm)
        self.maskKeyLineEdit.setObjectName(u"maskKeyLineEdit")

        self.gridLayout_4.addWidget(self.maskKeyLineEdit, 0, 4, 1, 1)

        self.labelTypeComboBox = QComboBox(imageLoaderForm)
        self.labelTypeComboBox.setObjectName(u"labelTypeComboBox")

        self.gridLayout_4.addWidget(self.labelTypeComboBox, 1, 4, 1, 1)

        self.dim2dRadioButton = QRadioButton(imageLoaderForm)
        self.dim2dRadioButton.setObjectName(u"dim2dRadioButton")

        self.gridLayout_4.addWidget(self.dim2dRadioButton, 2, 1, 1, 1)

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

        self.sameLoadAsImageCheckBox = QCheckBox(imageLoaderForm)
        self.sameLoadAsImageCheckBox.setObjectName(u"sameLoadAsImageCheckBox")
        self.sameLoadAsImageCheckBox.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_2.addWidget(self.sameLoadAsImageCheckBox, 1, 5, 1, 2)

        self.line_2 = QFrame(imageLoaderForm)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 7, 1, 1)

        self.imageLoadFuncNameComboBox = QComboBox(imageLoaderForm)
        self.imageLoadFuncNameComboBox.setObjectName(u"imageLoadFuncNameComboBox")

        self.gridLayout_2.addWidget(self.imageLoadFuncNameComboBox, 1, 2, 1, 3)

        self.label_10 = QLabel(imageLoaderForm)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)

        self.labelLoadFuncNameComboBox = QComboBox(imageLoaderForm)
        self.labelLoadFuncNameComboBox.setObjectName(u"labelLoadFuncNameComboBox")

        self.gridLayout_2.addWidget(self.labelLoadFuncNameComboBox, 2, 2, 1, 3)


        self.verticalLayout_9.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.channelOperToolButton = QToolButton(imageLoaderForm)
        self.channelOperToolButton.setObjectName(u"channelOperToolButton")

        self.verticalLayout_2.addWidget(self.channelOperToolButton)

        self.orienTransToolButton = QToolButton(imageLoaderForm)
        self.orienTransToolButton.setObjectName(u"orienTransToolButton")

        self.verticalLayout_2.addWidget(self.orienTransToolButton)

        self.imageCropToolButton = QToolButton(imageLoaderForm)
        self.imageCropToolButton.setObjectName(u"imageCropToolButton")

        self.verticalLayout_2.addWidget(self.imageCropToolButton)

        self.imageNormToolButton = QToolButton(imageLoaderForm)
        self.imageNormToolButton.setObjectName(u"imageNormToolButton")

        self.verticalLayout_2.addWidget(self.imageNormToolButton)

        self.dataAugToolButton = QToolButton(imageLoaderForm)
        self.dataAugToolButton.setObjectName(u"dataAugToolButton")

        self.verticalLayout_2.addWidget(self.dataAugToolButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.operItemsListWidget = QListWidget(imageLoaderForm)
        self.operItemsListWidget.setObjectName(u"operItemsListWidget")

        self.horizontalLayout_2.addWidget(self.operItemsListWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.addToolButton = QToolButton(imageLoaderForm)
        self.addToolButton.setObjectName(u"addToolButton")
        icon = QIcon()
        icon.addFile(u"E:/icon/icons8-plus-math-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addToolButton.setIcon(icon)

        self.gridLayout.addWidget(self.addToolButton, 0, 0, 1, 1)

        self.downToolButton = QToolButton(imageLoaderForm)
        self.downToolButton.setObjectName(u"downToolButton")
        icon1 = QIcon()
        icon1.addFile(u"E:/icon/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.downToolButton.setIcon(icon1)

        self.gridLayout.addWidget(self.downToolButton, 3, 0, 1, 1)

        self.upToolButton = QToolButton(imageLoaderForm)
        self.upToolButton.setObjectName(u"upToolButton")
        icon2 = QIcon()
        icon2.addFile(u"E:/icon/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.upToolButton.setIcon(icon2)

        self.gridLayout.addWidget(self.upToolButton, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.deleteToolButton = QToolButton(imageLoaderForm)
        self.deleteToolButton.setObjectName(u"deleteToolButton")
        icon3 = QIcon()
        icon3.addFile(u"E:/icon/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteToolButton.setIcon(icon3)

        self.gridLayout.addWidget(self.deleteToolButton, 1, 0, 1, 1)


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
        self.dim25dRadioButton.setText(QCoreApplication.translate("imageLoaderForm", u"2.5D\uff08C * W * H *3\uff09", None))
        self.dim3dRadioButton.setText(QCoreApplication.translate("imageLoaderForm", u"3D\uff08C * W * H * S\uff09", None))
        self.label_17.setText(QCoreApplication.translate("imageLoaderForm", u"\u7ef4\u5ea6\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\u7c7b\u578b\uff1a", None))
        self.imageTypeComboBox.setItemText(0, QCoreApplication.translate("imageLoaderForm", u"float32", None))

        self.dim2dRadioButton.setText(QCoreApplication.translate("imageLoaderForm", u"2D\uff08C * W * H\uff09", None))
        self.label_13.setText(QCoreApplication.translate("imageLoaderForm", u"\u6807\u6ce8\u7c7b\u578b\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("imageLoaderForm", u"ImageKey\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("imageLoaderForm", u"MaskKey\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("imageLoaderForm", u"\u6570\u636e\u52a0\u8f7d", None))
        self.label_11.setText(QCoreApplication.translate("imageLoaderForm", u"\uff08\u901a\u9053\u6570\u5728\u7b2c\u4e00\u7ef4\uff09", None))
        self.label_12.setText(QCoreApplication.translate("imageLoaderForm", u"\u6807\u6ce8\uff1a", None))
        self.sameLoadAsImageCheckBox.setText(QCoreApplication.translate("imageLoaderForm", u"\u6807\u6ce8\u4e0e\u56fe\u50cf\u52a0\u8f7d\u65b9\u6cd5\u76f8\u540c", None))
        self.label_10.setText(QCoreApplication.translate("imageLoaderForm", u"\u56fe\u50cf\uff1a", None))
        self.channelOperToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"+\u6570\u636e\u901a\u9053\u64cd\u4f5c", None))
        self.orienTransToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"+\u65b9\u4f4d\u8f6c\u6362", None))
        self.imageCropToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"+\u56fe\u50cf\u88c1\u526a\u589e\u8865", None))
        self.imageNormToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"+\u56fe\u50cf\u5f52\u4e00\u5316", None))
        self.dataAugToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"+\u6570\u636e\u6269\u589e", None))
        self.addToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.downToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.upToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.deleteToolButton.setText(QCoreApplication.translate("imageLoaderForm", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("imageLoaderForm", u"\u6dfb\u52a0", None))
        self.pushButton.setText(QCoreApplication.translate("imageLoaderForm", u"\u5b8c\u6210", None))
        self.currentStepInfo_2.setText(QCoreApplication.translate("imageLoaderForm", u"Output\uff1a", None))
    # retranslateUi

