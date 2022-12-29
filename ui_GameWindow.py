# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GameWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1112, 802)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plansze = QStackedWidget(self.centralwidget)
        self.plansze.setObjectName(u"plansze")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Logo = QLabel(self.menu)
        self.Logo.setObjectName(u"Logo")
        font = QFont()
        font.setPointSize(50)
        self.Logo.setFont(font)
        self.Logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Logo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QSize(50, 20))
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.ListaGraczy = QListWidget(self.menu)
        self.ListaGraczy.setObjectName(u"ListaGraczy")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ListaGraczy.sizePolicy().hasHeightForWidth())
        self.ListaGraczy.setSizePolicy(sizePolicy1)
        self.ListaGraczy.setMinimumSize(QSize(0, 10))
        self.ListaGraczy.setMaximumSize(QSize(16777215, 167222))

        self.verticalLayout.addWidget(self.ListaGraczy)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.menu)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.DodajGraczaButton = QPushButton(self.menu)
        self.DodajGraczaButton.setObjectName(u"DodajGraczaButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.DodajGraczaButton.sizePolicy().hasHeightForWidth())
        self.DodajGraczaButton.setSizePolicy(sizePolicy2)
        self.DodajGraczaButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.DodajGraczaButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.GrajButton = QPushButton(self.menu)
        self.GrajButton.setObjectName(u"GrajButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.GrajButton.sizePolicy().hasHeightForWidth())
        self.GrajButton.setSizePolicy(sizePolicy3)
        self.GrajButton.setMinimumSize(QSize(2, 2))
        self.GrajButton.setMaximumSize(QSize(500, 100))
        self.GrajButton.setBaseSize(QSize(200, 200))
        self.GrajButton.setFont(font1)
        self.GrajButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.GrajButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.GrajButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.plansze.addWidget(self.menu)
        self.gra = QWidget()
        self.gra.setObjectName(u"gra")
        self.Tura = QLabel(self.gra)
        self.Tura.setObjectName(u"Tura")
        self.Tura.setGeometry(QRect(400, 30, 251, 71))
        font2 = QFont()
        font2.setPointSize(20)
        self.Tura.setFont(font2)
        self.RzutButton = QPushButton(self.gra)
        self.RzutButton.setObjectName(u"RzutButton")
        self.RzutButton.setGeometry(QRect(820, 120, 191, 91))
        self.RzutButton.setFont(font2)
        self.RzutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.KupDomekButton = QPushButton(self.gra)
        self.KupDomekButton.setObjectName(u"KupDomekButton")
        self.KupDomekButton.setEnabled(False)
        self.KupDomekButton.setGeometry(QRect(820, 20, 191, 81))
        self.KupDomekButton.setFont(font2)
        self.WynikRzutu = QLabel(self.gra)
        self.WynikRzutu.setObjectName(u"WynikRzutu")
        self.WynikRzutu.setGeometry(QRect(880, 230, 71, 71))
        self.WynikRzutu.setFont(font2)
        self.WynikRzutu.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayoutWidget = QWidget(self.gra)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 90, 871, 581))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pole_1 = QVBoxLayout()
        self.pole_1.setObjectName(u"pole_1")
        self.pole_1.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa = QLabel(self.gridLayoutWidget)
        self.nazwa.setObjectName(u"nazwa")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.nazwa.sizePolicy().hasHeightForWidth())
        self.nazwa.setSizePolicy(sizePolicy4)
        self.nazwa.setBaseSize(QSize(17, 10))
        font3 = QFont()
        font3.setPointSize(15)
        self.nazwa.setFont(font3)
        self.nazwa.setAlignment(Qt.AlignCenter)

        self.pole_1.addWidget(self.nazwa)

        self.kolor = QGraphicsView(self.gridLayoutWidget)
        self.kolor.setObjectName(u"kolor")
        sizePolicy2.setHeightForWidth(self.kolor.sizePolicy().hasHeightForWidth())
        self.kolor.setSizePolicy(sizePolicy2)
        self.kolor.setMinimumSize(QSize(0, 0))
        self.kolor.setMaximumSize(QSize(150, 35))
        self.kolor.setAutoFillBackground(True)
        brush = QBrush(QColor(0, 10, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        self.kolor.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        self.kolor.setForegroundBrush(brush1)
        self.kolor.setInteractive(True)
        self.kolor.setSceneRect(QRectF(0, 0, 0, 0))

        self.pole_1.addWidget(self.kolor)

        self.gracze = QListView(self.gridLayoutWidget)
        self.gracze.setObjectName(u"gracze")
        sizePolicy2.setHeightForWidth(self.gracze.sizePolicy().hasHeightForWidth())
        self.gracze.setSizePolicy(sizePolicy2)
        self.gracze.setMinimumSize(QSize(0, 0))
        self.gracze.setMaximumSize(QSize(150, 100))

        self.pole_1.addWidget(self.gracze)

        self.cena = QLabel(self.gridLayoutWidget)
        self.cena.setObjectName(u"cena")
        sizePolicy4.setHeightForWidth(self.cena.sizePolicy().hasHeightForWidth())
        self.cena.setSizePolicy(sizePolicy4)
        self.cena.setFont(font3)
        self.cena.setAlignment(Qt.AlignCenter)

        self.pole_1.addWidget(self.cena)


        self.gridLayout_2.addLayout(self.pole_1, 0, 0, 1, 1)

        self.pole_2 = QVBoxLayout()
        self.pole_2.setObjectName(u"pole_2")
        self.pole_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_2 = QLabel(self.gridLayoutWidget)
        self.nazwa_2.setObjectName(u"nazwa_2")
        sizePolicy4.setHeightForWidth(self.nazwa_2.sizePolicy().hasHeightForWidth())
        self.nazwa_2.setSizePolicy(sizePolicy4)
        self.nazwa_2.setBaseSize(QSize(17, 10))
        self.nazwa_2.setFont(font3)
        self.nazwa_2.setAlignment(Qt.AlignCenter)

        self.pole_2.addWidget(self.nazwa_2)

        self.kolor_2 = QGraphicsView(self.gridLayoutWidget)
        self.kolor_2.setObjectName(u"kolor_2")
        sizePolicy2.setHeightForWidth(self.kolor_2.sizePolicy().hasHeightForWidth())
        self.kolor_2.setSizePolicy(sizePolicy2)
        self.kolor_2.setMinimumSize(QSize(0, 0))
        self.kolor_2.setMaximumSize(QSize(150, 35))
        self.kolor_2.setAutoFillBackground(True)

        self.pole_2.addWidget(self.kolor_2)

        self.gracze_2 = QListView(self.gridLayoutWidget)
        self.gracze_2.setObjectName(u"gracze_2")
        sizePolicy2.setHeightForWidth(self.gracze_2.sizePolicy().hasHeightForWidth())
        self.gracze_2.setSizePolicy(sizePolicy2)
        self.gracze_2.setMinimumSize(QSize(0, 0))
        self.gracze_2.setMaximumSize(QSize(150, 100))

        self.pole_2.addWidget(self.gracze_2)

        self.cena_2 = QLabel(self.gridLayoutWidget)
        self.cena_2.setObjectName(u"cena_2")
        sizePolicy4.setHeightForWidth(self.cena_2.sizePolicy().hasHeightForWidth())
        self.cena_2.setSizePolicy(sizePolicy4)
        self.cena_2.setFont(font3)
        self.cena_2.setAlignment(Qt.AlignCenter)

        self.pole_2.addWidget(self.cena_2)


        self.gridLayout_2.addLayout(self.pole_2, 0, 1, 1, 1)

        self.plansze.addWidget(self.gra)

        self.verticalLayout_2.addWidget(self.plansze)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1112, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.plansze.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"Monopoly", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gracze", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz imi\u0119 gracza", None))
        self.DodajGraczaButton.setText(QCoreApplication.translate("MainWindow", u"Dodaj gracza", None))
        self.GrajButton.setText(QCoreApplication.translate("MainWindow", u"Graj", None))
        self.Tura.setText(QCoreApplication.translate("MainWindow", u"Tura gracza: ", None))
        self.RzutButton.setText(QCoreApplication.translate("MainWindow", u"Rzu\u0107 kostk\u0105", None))
        self.KupDomekButton.setText(QCoreApplication.translate("MainWindow", u"Kup domek", None))
        self.WynikRzutu.setText("")
        self.nazwa.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cena.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.cena_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

