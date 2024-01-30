# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import View.files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(477, 558)
        icon = QIcon()
        icon.addFile(u":/icons/Downloads/_5fe58046-7e4c-4a4a-a920-a013dba99d18.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color:  #133955;\n"
"	font-family: Rubik;\n"
"	font-size: 15pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_temp = QLabel(self.centralwidget)
        self.label_temp.setObjectName(u"label_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_temp.sizePolicy().hasHeightForWidth())
        self.label_temp.setSizePolicy(sizePolicy)
        self.label_temp.setStyleSheet(u"color: #777777;")

        self.verticalLayout.addWidget(self.label_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        self.le_entry.setStyleSheet(u"font-size: 25pt;\n"
"border: none;")
        self.le_entry.setMaxLength(50)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_btn = QGridLayout()
        self.layout_btn.setObjectName(u"layout_btn")
        self.btn_camera = QPushButton(self.centralwidget)
        self.btn_camera.setObjectName(u"btn_camera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy1)
        self.btn_camera.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Downloads/camera (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon1)
        self.btn_camera.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_camera, 0, 5, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy1.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy1)
        self.btn_sqrt.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_sqrt.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Downloads/square-root (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sqrt.setIcon(icon2)
        self.btn_sqrt.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_sqrt, 2, 0, 1, 1)

        self.btn_pow = QPushButton(self.centralwidget)
        self.btn_pow.setObjectName(u"btn_pow")
        sizePolicy1.setHeightForWidth(self.btn_pow.sizePolicy().hasHeightForWidth())
        self.btn_pow.setSizePolicy(sizePolicy1)
        self.btn_pow.setCursor(QCursor(Qt.OpenHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Downloads/power.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pow.setIcon(icon3)
        self.btn_pow.setIconSize(QSize(48, 48))
        self.btn_pow.setCheckable(False)
        self.btn_pow.setAutoRepeat(False)
        self.btn_pow.setAutoExclusive(False)

        self.layout_btn.addWidget(self.btn_pow, 3, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_8, 1, 3, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_7, 1, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_9, 1, 4, 1, 1)

        self.btn_fx = QPushButton(self.centralwidget)
        self.btn_fx.setObjectName(u"btn_fx")
        sizePolicy1.setHeightForWidth(self.btn_fx.sizePolicy().hasHeightForWidth())
        self.btn_fx.setSizePolicy(sizePolicy1)
        self.btn_fx.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_fx, 0, 0, 1, 1)

        self.btn_pi = QPushButton(self.centralwidget)
        self.btn_pi.setObjectName(u"btn_pi")
        sizePolicy1.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy1)
        self.btn_pi.setCursor(QCursor(Qt.OpenHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/Downloads/pi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pi.setIcon(icon4)
        self.btn_pi.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_pi, 3, 1, 1, 1)

        self.btn_mikro = QPushButton(self.centralwidget)
        self.btn_mikro.setObjectName(u"btn_mikro")
        sizePolicy1.setHeightForWidth(self.btn_mikro.sizePolicy().hasHeightForWidth())
        self.btn_mikro.setSizePolicy(sizePolicy1)
        self.btn_mikro.setCursor(QCursor(Qt.OpenHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Downloads/microphone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_mikro.setIcon(icon5)
        self.btn_mikro.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_mikro, 0, 1, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy1.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy1)
        self.btn_div.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_div, 1, 5, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_2, 3, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_3, 3, 4, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_1, 3, 2, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy1.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy1)
        self.btn_sub.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_sub, 3, 5, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_4, 2, 2, 1, 1)

        self.btn_mod = QPushButton(self.centralwidget)
        self.btn_mod.setObjectName(u"btn_mod")
        sizePolicy1.setHeightForWidth(self.btn_mod.sizePolicy().hasHeightForWidth())
        self.btn_mod.setSizePolicy(sizePolicy1)
        self.btn_mod.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_mod, 4, 1, 1, 1)

        self.btn_a = QPushButton(self.centralwidget)
        self.btn_a.setObjectName(u"btn_a")
        self.btn_a.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_a.sizePolicy().hasHeightForWidth())
        self.btn_a.setSizePolicy(sizePolicy1)
        self.btn_a.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_a.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_a, 4, 0, 1, 1)

        self.btn_e = QPushButton(self.centralwidget)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy1.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy1)
        self.btn_e.setCursor(QCursor(Qt.OpenHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Downloads/letter-e (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_e.setIcon(icon6)
        self.btn_e.setIconSize(QSize(36, 36))

        self.layout_btn.addWidget(self.btn_e, 2, 1, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy1.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy1)

        self.layout_btn.addWidget(self.btn_equal, 4, 4, 1, 1)

        self.btn_mull = QPushButton(self.centralwidget)
        self.btn_mull.setObjectName(u"btn_mull")
        sizePolicy1.setHeightForWidth(self.btn_mull.sizePolicy().hasHeightForWidth())
        self.btn_mull.setSizePolicy(sizePolicy1)
        self.btn_mull.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_mull, 2, 5, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy1.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy1)
        self.btn_point.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy1.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy1)
        self.btn_plus.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_plus, 4, 5, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)
        self.btn_0.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_0, 4, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_5, 2, 3, 1, 1)

        self.btn_clearEntry = QPushButton(self.centralwidget)
        self.btn_clearEntry.setObjectName(u"btn_clearEntry")
        sizePolicy1.setHeightForWidth(self.btn_clearEntry.sizePolicy().hasHeightForWidth())
        self.btn_clearEntry.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.btn_clearEntry.setFont(font)
        self.btn_clearEntry.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_clearEntry.setStyleSheet(u"font: 75 22pt;\n"
"\n"
"")

        self.layout_btn.addWidget(self.btn_clearEntry, 0, 2, 1, 1)

        self.btn_Right = QPushButton(self.centralwidget)
        self.btn_Right.setObjectName(u"btn_Right")
        sizePolicy1.setHeightForWidth(self.btn_Right.sizePolicy().hasHeightForWidth())
        self.btn_Right.setSizePolicy(sizePolicy1)
        self.btn_Right.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_Right, 1, 1, 1, 1)

        self.btn_Left = QPushButton(self.centralwidget)
        self.btn_Left.setObjectName(u"btn_Left")
        sizePolicy1.setHeightForWidth(self.btn_Left.sizePolicy().hasHeightForWidth())
        self.btn_Left.setSizePolicy(sizePolicy1)
        self.btn_Left.setCursor(QCursor(Qt.OpenHandCursor))

        self.layout_btn.addWidget(self.btn_Left, 1, 0, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy1.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy1)
        self.btn_backspace.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Downloads/backspace (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon7)
        self.btn_backspace.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_backspace, 0, 4, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.btn_clear.setFont(font1)
        self.btn_clear.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_clear.setStyleSheet(u"font-size: 22pt;")
        self.btn_clear.setIconSize(QSize(64, 64))

        self.layout_btn.addWidget(self.btn_clear, 0, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_6.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.btn_6, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.layout_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PhotoMath", None))
        self.label_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_camera.setText("")
        self.btn_sqrt.setText("")
        self.btn_pow.setText("")
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_fx.setText(QCoreApplication.translate("MainWindow", u"F(x)...", None))
        self.btn_pi.setText("")
        self.btn_mikro.setText("")
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mod.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_a.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn_e.setText("")
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_mull.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_clearEntry.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_Right.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_Left.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_backspace.setText("")
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

