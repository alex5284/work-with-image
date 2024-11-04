# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1310, 658)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 30, 93, 29))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 110, 651, 501))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 630, 691, 20))
        self.btn_color = QPushButton(Widget)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setGeometry(QRect(170, 30, 93, 29))
        self.btn_gray = QPushButton(Widget)
        self.btn_gray.setObjectName(u"btn_gray")
        self.btn_gray.setGeometry(QRect(280, 30, 93, 29))
        self.btn_blur = QPushButton(Widget)
        self.btn_blur.setObjectName(u"btn_blur")
        self.btn_blur.setGeometry(QRect(390, 30, 93, 29))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(780, 30, 113, 25))
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(900, 30, 113, 25))
        self.btn_size = QPushButton(Widget)
        self.btn_size.setObjectName(u"btn_size")
        self.btn_size.setGeometry(QRect(680, 30, 93, 29))
        self.btn_save = QPushButton(Widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(490, 30, 93, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Read", None))
        self.label.setText("")
        self.label_2.setText("")
        self.btn_color.setText(QCoreApplication.translate("Widget", u"Color", None))
        self.btn_gray.setText(QCoreApplication.translate("Widget", u"Gray", None))
        self.btn_blur.setText(QCoreApplication.translate("Widget", u"Blur", None))
        self.btn_size.setText(QCoreApplication.translate("Widget", u"Size", None))
        self.btn_save.setText(QCoreApplication.translate("Widget", u"Save", None))
    # retranslateUi

