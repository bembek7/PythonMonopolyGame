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
        MainWindow.resize(1051, 723)
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
        self.tura = QLabel(self.gra)
        self.tura.setObjectName(u"tura")
        self.tura.setGeometry(QRect(400, 30, 251, 71))
        font2 = QFont()
        font2.setPointSize(20)
        self.tura.setFont(font2)
        self.RzutButton = QPushButton(self.gra)
        self.RzutButton.setObjectName(u"RzutButton")
        self.RzutButton.setGeometry(QRect(820, 120, 191, 91))
        self.RzutButton.setFont(font2)
        self.RzutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.KupDomek = QPushButton(self.gra)
        self.KupDomek.setObjectName(u"KupDomek")
        self.KupDomek.setEnabled(False)
        self.KupDomek.setGeometry(QRect(820, 20, 191, 81))
        self.KupDomek.setFont(font2)
        self.WynikRzutu = QLabel(self.gra)
        self.WynikRzutu.setObjectName(u"WynikRzutu")
        self.WynikRzutu.setGeometry(QRect(880, 230, 71, 71))
        self.WynikRzutu.setFont(font2)
        self.WynikRzutu.setCursor(QCursor(Qt.ArrowCursor))
        self.plansze.addWidget(self.gra)

        self.verticalLayout_2.addWidget(self.plansze)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 20))
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
        self.tura.setText(QCoreApplication.translate("MainWindow", u"Tura gracza: ", None))
        self.RzutButton.setText(QCoreApplication.translate("MainWindow", u"Rzu\u0107 kostk\u0105", None))
        self.KupDomek.setText(QCoreApplication.translate("MainWindow", u"Kup domek", None))
        self.WynikRzutu.setText("")
    # retranslateUi

