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
        MainWindow.resize(1188, 1314)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plansze = QStackedWidget(self.centralwidget)
        self.plansze.setObjectName(u"plansze")
        self.plansze.setGeometry(QRect(9, 9, 1170, 1254))
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
        self.verticalLayout_4 = QVBoxLayout(self.gra)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.KupDomekButton = QPushButton(self.gra)
        self.KupDomekButton.setObjectName(u"KupDomekButton")
        self.KupDomekButton.setEnabled(False)
        font2 = QFont()
        font2.setPointSize(20)
        self.KupDomekButton.setFont(font2)

        self.verticalLayout_4.addWidget(self.KupDomekButton)

        self.RzutButton = QPushButton(self.gra)
        self.RzutButton.setObjectName(u"RzutButton")
        self.RzutButton.setFont(font2)
        self.RzutButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.RzutButton)

        self.WynikRzutu = QLabel(self.gra)
        self.WynikRzutu.setObjectName(u"WynikRzutu")
        self.WynikRzutu.setFont(font2)
        self.WynikRzutu.setCursor(QCursor(Qt.ArrowCursor))

        self.verticalLayout_4.addWidget(self.WynikRzutu)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.pole_1 = QVBoxLayout()
        self.pole_1.setObjectName(u"pole_1")
        self.pole_1.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa = QLabel(self.gra)
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

        self.label_3 = QLabel(self.gra)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(150, 35))
        self.label_3.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_1.addWidget(self.label_3)

        self.gracze = QListView(self.gra)
        self.gracze.setObjectName(u"gracze")
        sizePolicy2.setHeightForWidth(self.gracze.sizePolicy().hasHeightForWidth())
        self.gracze.setSizePolicy(sizePolicy2)
        self.gracze.setMinimumSize(QSize(0, 0))
        self.gracze.setMaximumSize(QSize(150, 100))

        self.pole_1.addWidget(self.gracze)

        self.label_2 = QLabel(self.gra)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.pole_1.addWidget(self.label_2)

        self.cena = QLabel(self.gra)
        self.cena.setObjectName(u"cena")
        sizePolicy4.setHeightForWidth(self.cena.sizePolicy().hasHeightForWidth())
        self.cena.setSizePolicy(sizePolicy4)
        self.cena.setFont(font3)
        self.cena.setAlignment(Qt.AlignCenter)

        self.pole_1.addWidget(self.cena)


        self.gridLayout_2.addLayout(self.pole_1, 0, 0, 1, 1)

        self.pole_5 = QVBoxLayout()
        self.pole_5.setObjectName(u"pole_5")
        self.pole_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_5 = QLabel(self.gra)
        self.nazwa_5.setObjectName(u"nazwa_5")
        sizePolicy4.setHeightForWidth(self.nazwa_5.sizePolicy().hasHeightForWidth())
        self.nazwa_5.setSizePolicy(sizePolicy4)
        self.nazwa_5.setBaseSize(QSize(17, 10))
        self.nazwa_5.setFont(font3)
        self.nazwa_5.setAlignment(Qt.AlignCenter)

        self.pole_5.addWidget(self.nazwa_5)

        self.label_10 = QLabel(self.gra)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(150, 35))
        self.label_10.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_5.addWidget(self.label_10)

        self.gracze_5 = QListView(self.gra)
        self.gracze_5.setObjectName(u"gracze_5")
        sizePolicy2.setHeightForWidth(self.gracze_5.sizePolicy().hasHeightForWidth())
        self.gracze_5.setSizePolicy(sizePolicy2)
        self.gracze_5.setMinimumSize(QSize(0, 0))
        self.gracze_5.setMaximumSize(QSize(150, 100))

        self.pole_5.addWidget(self.gracze_5)

        self.label_11 = QLabel(self.gra)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.pole_5.addWidget(self.label_11)

        self.cena_5 = QLabel(self.gra)
        self.cena_5.setObjectName(u"cena_5")
        sizePolicy4.setHeightForWidth(self.cena_5.sizePolicy().hasHeightForWidth())
        self.cena_5.setSizePolicy(sizePolicy4)
        self.cena_5.setFont(font3)
        self.cena_5.setAlignment(Qt.AlignCenter)

        self.pole_5.addWidget(self.cena_5)


        self.gridLayout_2.addLayout(self.pole_5, 0, 4, 1, 1)

        self.pole_11 = QVBoxLayout()
        self.pole_11.setObjectName(u"pole_11")
        self.pole_11.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_11 = QLabel(self.gra)
        self.nazwa_11.setObjectName(u"nazwa_11")
        sizePolicy4.setHeightForWidth(self.nazwa_11.sizePolicy().hasHeightForWidth())
        self.nazwa_11.setSizePolicy(sizePolicy4)
        self.nazwa_11.setBaseSize(QSize(17, 10))
        self.nazwa_11.setFont(font3)
        self.nazwa_11.setAlignment(Qt.AlignCenter)

        self.pole_11.addWidget(self.nazwa_11)

        self.label_22 = QLabel(self.gra)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(150, 35))
        self.label_22.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_11.addWidget(self.label_22)

        self.gracze_11 = QListView(self.gra)
        self.gracze_11.setObjectName(u"gracze_11")
        sizePolicy2.setHeightForWidth(self.gracze_11.sizePolicy().hasHeightForWidth())
        self.gracze_11.setSizePolicy(sizePolicy2)
        self.gracze_11.setMinimumSize(QSize(0, 0))
        self.gracze_11.setMaximumSize(QSize(150, 100))

        self.pole_11.addWidget(self.gracze_11)

        self.label_23 = QLabel(self.gra)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.pole_11.addWidget(self.label_23)

        self.cena_11 = QLabel(self.gra)
        self.cena_11.setObjectName(u"cena_11")
        sizePolicy4.setHeightForWidth(self.cena_11.sizePolicy().hasHeightForWidth())
        self.cena_11.setSizePolicy(sizePolicy4)
        self.cena_11.setFont(font3)
        self.cena_11.setAlignment(Qt.AlignCenter)

        self.pole_11.addWidget(self.cena_11)


        self.gridLayout_2.addLayout(self.pole_11, 0, 9, 1, 1)

        self.pole_14 = QVBoxLayout()
        self.pole_14.setObjectName(u"pole_14")
        self.pole_14.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_14 = QLabel(self.gra)
        self.nazwa_14.setObjectName(u"nazwa_14")
        sizePolicy4.setHeightForWidth(self.nazwa_14.sizePolicy().hasHeightForWidth())
        self.nazwa_14.setSizePolicy(sizePolicy4)
        self.nazwa_14.setBaseSize(QSize(17, 10))
        self.nazwa_14.setFont(font3)
        self.nazwa_14.setAlignment(Qt.AlignCenter)

        self.pole_14.addWidget(self.nazwa_14)

        self.label_28 = QLabel(self.gra)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(150, 35))
        self.label_28.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_14.addWidget(self.label_28)

        self.gracze_14 = QListView(self.gra)
        self.gracze_14.setObjectName(u"gracze_14")
        sizePolicy2.setHeightForWidth(self.gracze_14.sizePolicy().hasHeightForWidth())
        self.gracze_14.setSizePolicy(sizePolicy2)
        self.gracze_14.setMinimumSize(QSize(0, 0))
        self.gracze_14.setMaximumSize(QSize(150, 100))

        self.pole_14.addWidget(self.gracze_14)

        self.label_29 = QLabel(self.gra)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.pole_14.addWidget(self.label_29)

        self.cena_14 = QLabel(self.gra)
        self.cena_14.setObjectName(u"cena_14")
        sizePolicy4.setHeightForWidth(self.cena_14.sizePolicy().hasHeightForWidth())
        self.cena_14.setSizePolicy(sizePolicy4)
        self.cena_14.setFont(font3)
        self.cena_14.setAlignment(Qt.AlignCenter)

        self.pole_14.addWidget(self.cena_14)


        self.gridLayout_2.addLayout(self.pole_14, 3, 0, 1, 1)

        self.pole_22 = QVBoxLayout()
        self.pole_22.setObjectName(u"pole_22")
        self.pole_22.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_22 = QLabel(self.gra)
        self.nazwa_22.setObjectName(u"nazwa_22")
        sizePolicy4.setHeightForWidth(self.nazwa_22.sizePolicy().hasHeightForWidth())
        self.nazwa_22.setSizePolicy(sizePolicy4)
        self.nazwa_22.setBaseSize(QSize(17, 10))
        self.nazwa_22.setFont(font3)
        self.nazwa_22.setAlignment(Qt.AlignCenter)

        self.pole_22.addWidget(self.nazwa_22)

        self.label_44 = QLabel(self.gra)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(150, 35))
        self.label_44.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_22.addWidget(self.label_44)

        self.gracze_22 = QListView(self.gra)
        self.gracze_22.setObjectName(u"gracze_22")
        sizePolicy2.setHeightForWidth(self.gracze_22.sizePolicy().hasHeightForWidth())
        self.gracze_22.setSizePolicy(sizePolicy2)
        self.gracze_22.setMinimumSize(QSize(0, 0))
        self.gracze_22.setMaximumSize(QSize(150, 100))

        self.pole_22.addWidget(self.gracze_22)

        self.label_45 = QLabel(self.gra)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.pole_22.addWidget(self.label_45)

        self.cena_22 = QLabel(self.gra)
        self.cena_22.setObjectName(u"cena_22")
        sizePolicy4.setHeightForWidth(self.cena_22.sizePolicy().hasHeightForWidth())
        self.cena_22.setSizePolicy(sizePolicy4)
        self.cena_22.setFont(font3)
        self.cena_22.setAlignment(Qt.AlignCenter)

        self.pole_22.addWidget(self.cena_22)


        self.gridLayout_2.addLayout(self.pole_22, 6, 0, 1, 1)

        self.pole_17 = QVBoxLayout()
        self.pole_17.setObjectName(u"pole_17")
        self.pole_17.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_17 = QLabel(self.gra)
        self.nazwa_17.setObjectName(u"nazwa_17")
        sizePolicy4.setHeightForWidth(self.nazwa_17.sizePolicy().hasHeightForWidth())
        self.nazwa_17.setSizePolicy(sizePolicy4)
        self.nazwa_17.setBaseSize(QSize(17, 10))
        self.nazwa_17.setFont(font3)
        self.nazwa_17.setAlignment(Qt.AlignCenter)

        self.pole_17.addWidget(self.nazwa_17)

        self.label_34 = QLabel(self.gra)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(150, 35))
        self.label_34.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_17.addWidget(self.label_34)

        self.gracze_17 = QListView(self.gra)
        self.gracze_17.setObjectName(u"gracze_17")
        sizePolicy2.setHeightForWidth(self.gracze_17.sizePolicy().hasHeightForWidth())
        self.gracze_17.setSizePolicy(sizePolicy2)
        self.gracze_17.setMinimumSize(QSize(0, 0))
        self.gracze_17.setMaximumSize(QSize(150, 100))

        self.pole_17.addWidget(self.gracze_17)

        self.label_35 = QLabel(self.gra)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.pole_17.addWidget(self.label_35)

        self.cena_17 = QLabel(self.gra)
        self.cena_17.setObjectName(u"cena_17")
        sizePolicy4.setHeightForWidth(self.cena_17.sizePolicy().hasHeightForWidth())
        self.cena_17.setSizePolicy(sizePolicy4)
        self.cena_17.setFont(font3)
        self.cena_17.setAlignment(Qt.AlignCenter)

        self.pole_17.addWidget(self.cena_17)


        self.gridLayout_2.addLayout(self.pole_17, 3, 9, 1, 1)

        self.pole_2 = QVBoxLayout()
        self.pole_2.setObjectName(u"pole_2")
        self.pole_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_2 = QLabel(self.gra)
        self.nazwa_2.setObjectName(u"nazwa_2")
        sizePolicy4.setHeightForWidth(self.nazwa_2.sizePolicy().hasHeightForWidth())
        self.nazwa_2.setSizePolicy(sizePolicy4)
        self.nazwa_2.setBaseSize(QSize(17, 10))
        self.nazwa_2.setFont(font3)
        self.nazwa_2.setAlignment(Qt.AlignCenter)

        self.pole_2.addWidget(self.nazwa_2)

        self.label_4 = QLabel(self.gra)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 35))
        self.label_4.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_2.addWidget(self.label_4)

        self.gracze_2 = QListView(self.gra)
        self.gracze_2.setObjectName(u"gracze_2")
        sizePolicy2.setHeightForWidth(self.gracze_2.sizePolicy().hasHeightForWidth())
        self.gracze_2.setSizePolicy(sizePolicy2)
        self.gracze_2.setMinimumSize(QSize(0, 0))
        self.gracze_2.setMaximumSize(QSize(150, 100))

        self.pole_2.addWidget(self.gracze_2)

        self.label_5 = QLabel(self.gra)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.pole_2.addWidget(self.label_5)

        self.cena_2 = QLabel(self.gra)
        self.cena_2.setObjectName(u"cena_2")
        sizePolicy4.setHeightForWidth(self.cena_2.sizePolicy().hasHeightForWidth())
        self.cena_2.setSizePolicy(sizePolicy4)
        self.cena_2.setFont(font3)
        self.cena_2.setAlignment(Qt.AlignCenter)

        self.pole_2.addWidget(self.cena_2)


        self.gridLayout_2.addLayout(self.pole_2, 0, 1, 1, 1)

        self.pole_18 = QVBoxLayout()
        self.pole_18.setObjectName(u"pole_18")
        self.pole_18.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_18 = QLabel(self.gra)
        self.nazwa_18.setObjectName(u"nazwa_18")
        sizePolicy4.setHeightForWidth(self.nazwa_18.sizePolicy().hasHeightForWidth())
        self.nazwa_18.setSizePolicy(sizePolicy4)
        self.nazwa_18.setBaseSize(QSize(17, 10))
        self.nazwa_18.setFont(font3)
        self.nazwa_18.setAlignment(Qt.AlignCenter)

        self.pole_18.addWidget(self.nazwa_18)

        self.label_36 = QLabel(self.gra)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(150, 35))
        self.label_36.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_18.addWidget(self.label_36)

        self.gracze_18 = QListView(self.gra)
        self.gracze_18.setObjectName(u"gracze_18")
        sizePolicy2.setHeightForWidth(self.gracze_18.sizePolicy().hasHeightForWidth())
        self.gracze_18.setSizePolicy(sizePolicy2)
        self.gracze_18.setMinimumSize(QSize(0, 0))
        self.gracze_18.setMaximumSize(QSize(150, 100))

        self.pole_18.addWidget(self.gracze_18)

        self.label_37 = QLabel(self.gra)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.pole_18.addWidget(self.label_37)

        self.cena_18 = QLabel(self.gra)
        self.cena_18.setObjectName(u"cena_18")
        sizePolicy4.setHeightForWidth(self.cena_18.sizePolicy().hasHeightForWidth())
        self.cena_18.setSizePolicy(sizePolicy4)
        self.cena_18.setFont(font3)
        self.cena_18.setAlignment(Qt.AlignCenter)

        self.pole_18.addWidget(self.cena_18)


        self.gridLayout_2.addLayout(self.pole_18, 4, 9, 1, 1)

        self.pole_10 = QVBoxLayout()
        self.pole_10.setObjectName(u"pole_10")
        self.pole_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_10 = QLabel(self.gra)
        self.nazwa_10.setObjectName(u"nazwa_10")
        sizePolicy4.setHeightForWidth(self.nazwa_10.sizePolicy().hasHeightForWidth())
        self.nazwa_10.setSizePolicy(sizePolicy4)
        self.nazwa_10.setBaseSize(QSize(17, 10))
        self.nazwa_10.setFont(font3)
        self.nazwa_10.setAlignment(Qt.AlignCenter)

        self.pole_10.addWidget(self.nazwa_10)

        self.label_20 = QLabel(self.gra)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(150, 35))
        self.label_20.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_10.addWidget(self.label_20)

        self.gracze_10 = QListView(self.gra)
        self.gracze_10.setObjectName(u"gracze_10")
        sizePolicy2.setHeightForWidth(self.gracze_10.sizePolicy().hasHeightForWidth())
        self.gracze_10.setSizePolicy(sizePolicy2)
        self.gracze_10.setMinimumSize(QSize(0, 0))
        self.gracze_10.setMaximumSize(QSize(150, 100))

        self.pole_10.addWidget(self.gracze_10)

        self.label_21 = QLabel(self.gra)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.pole_10.addWidget(self.label_21)

        self.cena_10 = QLabel(self.gra)
        self.cena_10.setObjectName(u"cena_10")
        sizePolicy4.setHeightForWidth(self.cena_10.sizePolicy().hasHeightForWidth())
        self.cena_10.setSizePolicy(sizePolicy4)
        self.cena_10.setFont(font3)
        self.cena_10.setAlignment(Qt.AlignCenter)

        self.pole_10.addWidget(self.cena_10)


        self.gridLayout_2.addLayout(self.pole_10, 0, 8, 1, 1)

        self.pole_8 = QVBoxLayout()
        self.pole_8.setObjectName(u"pole_8")
        self.pole_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_8 = QLabel(self.gra)
        self.nazwa_8.setObjectName(u"nazwa_8")
        sizePolicy4.setHeightForWidth(self.nazwa_8.sizePolicy().hasHeightForWidth())
        self.nazwa_8.setSizePolicy(sizePolicy4)
        self.nazwa_8.setBaseSize(QSize(17, 10))
        self.nazwa_8.setFont(font3)
        self.nazwa_8.setAlignment(Qt.AlignCenter)

        self.pole_8.addWidget(self.nazwa_8)

        self.label_16 = QLabel(self.gra)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(150, 35))
        self.label_16.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_8.addWidget(self.label_16)

        self.gracze_8 = QListView(self.gra)
        self.gracze_8.setObjectName(u"gracze_8")
        sizePolicy2.setHeightForWidth(self.gracze_8.sizePolicy().hasHeightForWidth())
        self.gracze_8.setSizePolicy(sizePolicy2)
        self.gracze_8.setMinimumSize(QSize(0, 0))
        self.gracze_8.setMaximumSize(QSize(150, 100))

        self.pole_8.addWidget(self.gracze_8)

        self.label_17 = QLabel(self.gra)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.pole_8.addWidget(self.label_17)

        self.cena_8 = QLabel(self.gra)
        self.cena_8.setObjectName(u"cena_8")
        sizePolicy4.setHeightForWidth(self.cena_8.sizePolicy().hasHeightForWidth())
        self.cena_8.setSizePolicy(sizePolicy4)
        self.cena_8.setFont(font3)
        self.cena_8.setAlignment(Qt.AlignCenter)

        self.pole_8.addWidget(self.cena_8)


        self.gridLayout_2.addLayout(self.pole_8, 0, 6, 1, 1)

        self.pole_6 = QVBoxLayout()
        self.pole_6.setObjectName(u"pole_6")
        self.pole_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_6 = QLabel(self.gra)
        self.nazwa_6.setObjectName(u"nazwa_6")
        sizePolicy4.setHeightForWidth(self.nazwa_6.sizePolicy().hasHeightForWidth())
        self.nazwa_6.setSizePolicy(sizePolicy4)
        self.nazwa_6.setBaseSize(QSize(17, 10))
        self.nazwa_6.setFont(font3)
        self.nazwa_6.setAlignment(Qt.AlignCenter)

        self.pole_6.addWidget(self.nazwa_6)

        self.label_12 = QLabel(self.gra)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(150, 35))
        self.label_12.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_6.addWidget(self.label_12)

        self.gracze_6 = QListView(self.gra)
        self.gracze_6.setObjectName(u"gracze_6")
        sizePolicy2.setHeightForWidth(self.gracze_6.sizePolicy().hasHeightForWidth())
        self.gracze_6.setSizePolicy(sizePolicy2)
        self.gracze_6.setMinimumSize(QSize(0, 0))
        self.gracze_6.setMaximumSize(QSize(150, 100))

        self.pole_6.addWidget(self.gracze_6)

        self.label_13 = QLabel(self.gra)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.pole_6.addWidget(self.label_13)

        self.cena_6 = QLabel(self.gra)
        self.cena_6.setObjectName(u"cena_6")
        sizePolicy4.setHeightForWidth(self.cena_6.sizePolicy().hasHeightForWidth())
        self.cena_6.setSizePolicy(sizePolicy4)
        self.cena_6.setFont(font3)
        self.cena_6.setAlignment(Qt.AlignCenter)

        self.pole_6.addWidget(self.cena_6)


        self.gridLayout_2.addLayout(self.pole_6, 1, 9, 1, 1)

        self.pole_21 = QVBoxLayout()
        self.pole_21.setObjectName(u"pole_21")
        self.pole_21.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_21 = QLabel(self.gra)
        self.nazwa_21.setObjectName(u"nazwa_21")
        sizePolicy4.setHeightForWidth(self.nazwa_21.sizePolicy().hasHeightForWidth())
        self.nazwa_21.setSizePolicy(sizePolicy4)
        self.nazwa_21.setBaseSize(QSize(17, 10))
        self.nazwa_21.setFont(font3)
        self.nazwa_21.setAlignment(Qt.AlignCenter)

        self.pole_21.addWidget(self.nazwa_21)

        self.label_42 = QLabel(self.gra)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(150, 35))
        self.label_42.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_21.addWidget(self.label_42)

        self.gracze_21 = QListView(self.gra)
        self.gracze_21.setObjectName(u"gracze_21")
        sizePolicy2.setHeightForWidth(self.gracze_21.sizePolicy().hasHeightForWidth())
        self.gracze_21.setSizePolicy(sizePolicy2)
        self.gracze_21.setMinimumSize(QSize(0, 0))
        self.gracze_21.setMaximumSize(QSize(150, 100))

        self.pole_21.addWidget(self.gracze_21)

        self.label_43 = QLabel(self.gra)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.pole_21.addWidget(self.label_43)

        self.cena_21 = QLabel(self.gra)
        self.cena_21.setObjectName(u"cena_21")
        sizePolicy4.setHeightForWidth(self.cena_21.sizePolicy().hasHeightForWidth())
        self.cena_21.setSizePolicy(sizePolicy4)
        self.cena_21.setFont(font3)
        self.cena_21.setAlignment(Qt.AlignCenter)

        self.pole_21.addWidget(self.cena_21)


        self.gridLayout_2.addLayout(self.pole_21, 5, 9, 1, 1)

        self.pole_12 = QVBoxLayout()
        self.pole_12.setObjectName(u"pole_12")
        self.pole_12.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_12 = QLabel(self.gra)
        self.nazwa_12.setObjectName(u"nazwa_12")
        sizePolicy4.setHeightForWidth(self.nazwa_12.sizePolicy().hasHeightForWidth())
        self.nazwa_12.setSizePolicy(sizePolicy4)
        self.nazwa_12.setBaseSize(QSize(17, 10))
        self.nazwa_12.setFont(font3)
        self.nazwa_12.setAlignment(Qt.AlignCenter)

        self.pole_12.addWidget(self.nazwa_12)

        self.label_24 = QLabel(self.gra)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(150, 35))
        self.label_24.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_12.addWidget(self.label_24)

        self.gracze_12 = QListView(self.gra)
        self.gracze_12.setObjectName(u"gracze_12")
        sizePolicy2.setHeightForWidth(self.gracze_12.sizePolicy().hasHeightForWidth())
        self.gracze_12.setSizePolicy(sizePolicy2)
        self.gracze_12.setMinimumSize(QSize(0, 0))
        self.gracze_12.setMaximumSize(QSize(150, 100))

        self.pole_12.addWidget(self.gracze_12)

        self.label_25 = QLabel(self.gra)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.pole_12.addWidget(self.label_25)

        self.cena_12 = QLabel(self.gra)
        self.cena_12.setObjectName(u"cena_12")
        sizePolicy4.setHeightForWidth(self.cena_12.sizePolicy().hasHeightForWidth())
        self.cena_12.setSizePolicy(sizePolicy4)
        self.cena_12.setFont(font3)
        self.cena_12.setAlignment(Qt.AlignCenter)

        self.pole_12.addWidget(self.cena_12)


        self.gridLayout_2.addLayout(self.pole_12, 2, 0, 1, 1)

        self.pole_25 = QVBoxLayout()
        self.pole_25.setObjectName(u"pole_25")
        self.pole_25.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_25 = QLabel(self.gra)
        self.nazwa_25.setObjectName(u"nazwa_25")
        sizePolicy4.setHeightForWidth(self.nazwa_25.sizePolicy().hasHeightForWidth())
        self.nazwa_25.setSizePolicy(sizePolicy4)
        self.nazwa_25.setBaseSize(QSize(17, 10))
        self.nazwa_25.setFont(font3)
        self.nazwa_25.setAlignment(Qt.AlignCenter)

        self.pole_25.addWidget(self.nazwa_25)

        self.label_50 = QLabel(self.gra)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(150, 35))
        self.label_50.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_25.addWidget(self.label_50)

        self.gracze_25 = QListView(self.gra)
        self.gracze_25.setObjectName(u"gracze_25")
        sizePolicy2.setHeightForWidth(self.gracze_25.sizePolicy().hasHeightForWidth())
        self.gracze_25.setSizePolicy(sizePolicy2)
        self.gracze_25.setMinimumSize(QSize(0, 0))
        self.gracze_25.setMaximumSize(QSize(150, 100))

        self.pole_25.addWidget(self.gracze_25)

        self.label_51 = QLabel(self.gra)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.pole_25.addWidget(self.label_51)

        self.cena_25 = QLabel(self.gra)
        self.cena_25.setObjectName(u"cena_25")
        sizePolicy4.setHeightForWidth(self.cena_25.sizePolicy().hasHeightForWidth())
        self.cena_25.setSizePolicy(sizePolicy4)
        self.cena_25.setFont(font3)
        self.cena_25.setAlignment(Qt.AlignCenter)

        self.pole_25.addWidget(self.cena_25)


        self.gridLayout_2.addLayout(self.pole_25, 8, 0, 1, 1)

        self.pole_3 = QVBoxLayout()
        self.pole_3.setObjectName(u"pole_3")
        self.pole_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_3 = QLabel(self.gra)
        self.nazwa_3.setObjectName(u"nazwa_3")
        sizePolicy4.setHeightForWidth(self.nazwa_3.sizePolicy().hasHeightForWidth())
        self.nazwa_3.setSizePolicy(sizePolicy4)
        self.nazwa_3.setBaseSize(QSize(17, 10))
        self.nazwa_3.setFont(font3)
        self.nazwa_3.setAlignment(Qt.AlignCenter)

        self.pole_3.addWidget(self.nazwa_3)

        self.label_6 = QLabel(self.gra)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(150, 35))
        self.label_6.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_3.addWidget(self.label_6)

        self.gracze_3 = QListView(self.gra)
        self.gracze_3.setObjectName(u"gracze_3")
        sizePolicy2.setHeightForWidth(self.gracze_3.sizePolicy().hasHeightForWidth())
        self.gracze_3.setSizePolicy(sizePolicy2)
        self.gracze_3.setMinimumSize(QSize(0, 0))
        self.gracze_3.setMaximumSize(QSize(150, 100))

        self.pole_3.addWidget(self.gracze_3)

        self.label_7 = QLabel(self.gra)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.pole_3.addWidget(self.label_7)

        self.cena_3 = QLabel(self.gra)
        self.cena_3.setObjectName(u"cena_3")
        sizePolicy4.setHeightForWidth(self.cena_3.sizePolicy().hasHeightForWidth())
        self.cena_3.setSizePolicy(sizePolicy4)
        self.cena_3.setFont(font3)
        self.cena_3.setAlignment(Qt.AlignCenter)

        self.pole_3.addWidget(self.cena_3)


        self.gridLayout_2.addLayout(self.pole_3, 0, 2, 1, 1)

        self.pole_7 = QVBoxLayout()
        self.pole_7.setObjectName(u"pole_7")
        self.pole_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_7 = QLabel(self.gra)
        self.nazwa_7.setObjectName(u"nazwa_7")
        sizePolicy4.setHeightForWidth(self.nazwa_7.sizePolicy().hasHeightForWidth())
        self.nazwa_7.setSizePolicy(sizePolicy4)
        self.nazwa_7.setBaseSize(QSize(17, 10))
        self.nazwa_7.setFont(font3)
        self.nazwa_7.setAlignment(Qt.AlignCenter)

        self.pole_7.addWidget(self.nazwa_7)

        self.label_14 = QLabel(self.gra)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(150, 35))
        self.label_14.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_7.addWidget(self.label_14)

        self.gracze_7 = QListView(self.gra)
        self.gracze_7.setObjectName(u"gracze_7")
        sizePolicy2.setHeightForWidth(self.gracze_7.sizePolicy().hasHeightForWidth())
        self.gracze_7.setSizePolicy(sizePolicy2)
        self.gracze_7.setMinimumSize(QSize(0, 0))
        self.gracze_7.setMaximumSize(QSize(150, 100))

        self.pole_7.addWidget(self.gracze_7)

        self.label_15 = QLabel(self.gra)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.pole_7.addWidget(self.label_15)

        self.cena_7 = QLabel(self.gra)
        self.cena_7.setObjectName(u"cena_7")
        sizePolicy4.setHeightForWidth(self.cena_7.sizePolicy().hasHeightForWidth())
        self.cena_7.setSizePolicy(sizePolicy4)
        self.cena_7.setFont(font3)
        self.cena_7.setAlignment(Qt.AlignCenter)

        self.pole_7.addWidget(self.cena_7)


        self.gridLayout_2.addLayout(self.pole_7, 0, 5, 1, 1)

        self.pole_9 = QVBoxLayout()
        self.pole_9.setObjectName(u"pole_9")
        self.pole_9.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_9 = QLabel(self.gra)
        self.nazwa_9.setObjectName(u"nazwa_9")
        sizePolicy4.setHeightForWidth(self.nazwa_9.sizePolicy().hasHeightForWidth())
        self.nazwa_9.setSizePolicy(sizePolicy4)
        self.nazwa_9.setBaseSize(QSize(17, 10))
        self.nazwa_9.setFont(font3)
        self.nazwa_9.setAlignment(Qt.AlignCenter)

        self.pole_9.addWidget(self.nazwa_9)

        self.label_18 = QLabel(self.gra)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(150, 35))
        self.label_18.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_9.addWidget(self.label_18)

        self.gracze_9 = QListView(self.gra)
        self.gracze_9.setObjectName(u"gracze_9")
        sizePolicy2.setHeightForWidth(self.gracze_9.sizePolicy().hasHeightForWidth())
        self.gracze_9.setSizePolicy(sizePolicy2)
        self.gracze_9.setMinimumSize(QSize(0, 0))
        self.gracze_9.setMaximumSize(QSize(150, 100))

        self.pole_9.addWidget(self.gracze_9)

        self.label_19 = QLabel(self.gra)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.pole_9.addWidget(self.label_19)

        self.cena_9 = QLabel(self.gra)
        self.cena_9.setObjectName(u"cena_9")
        sizePolicy4.setHeightForWidth(self.cena_9.sizePolicy().hasHeightForWidth())
        self.cena_9.setSizePolicy(sizePolicy4)
        self.cena_9.setFont(font3)
        self.cena_9.setAlignment(Qt.AlignCenter)

        self.pole_9.addWidget(self.cena_9)


        self.gridLayout_2.addLayout(self.pole_9, 0, 7, 1, 1)

        self.pole_19 = QVBoxLayout()
        self.pole_19.setObjectName(u"pole_19")
        self.pole_19.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_19 = QLabel(self.gra)
        self.nazwa_19.setObjectName(u"nazwa_19")
        sizePolicy4.setHeightForWidth(self.nazwa_19.sizePolicy().hasHeightForWidth())
        self.nazwa_19.setSizePolicy(sizePolicy4)
        self.nazwa_19.setBaseSize(QSize(17, 10))
        self.nazwa_19.setFont(font3)
        self.nazwa_19.setAlignment(Qt.AlignCenter)

        self.pole_19.addWidget(self.nazwa_19)

        self.label_38 = QLabel(self.gra)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(150, 35))
        self.label_38.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_19.addWidget(self.label_38)

        self.gracze_19 = QListView(self.gra)
        self.gracze_19.setObjectName(u"gracze_19")
        sizePolicy2.setHeightForWidth(self.gracze_19.sizePolicy().hasHeightForWidth())
        self.gracze_19.setSizePolicy(sizePolicy2)
        self.gracze_19.setMinimumSize(QSize(0, 0))
        self.gracze_19.setMaximumSize(QSize(150, 100))

        self.pole_19.addWidget(self.gracze_19)

        self.label_39 = QLabel(self.gra)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.pole_19.addWidget(self.label_39)

        self.cena_19 = QLabel(self.gra)
        self.cena_19.setObjectName(u"cena_19")
        sizePolicy4.setHeightForWidth(self.cena_19.sizePolicy().hasHeightForWidth())
        self.cena_19.setSizePolicy(sizePolicy4)
        self.cena_19.setFont(font3)
        self.cena_19.setAlignment(Qt.AlignCenter)

        self.pole_19.addWidget(self.cena_19)


        self.gridLayout_2.addLayout(self.pole_19, 5, 0, 1, 1)

        self.pole_23 = QVBoxLayout()
        self.pole_23.setObjectName(u"pole_23")
        self.pole_23.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_23 = QLabel(self.gra)
        self.nazwa_23.setObjectName(u"nazwa_23")
        sizePolicy4.setHeightForWidth(self.nazwa_23.sizePolicy().hasHeightForWidth())
        self.nazwa_23.setSizePolicy(sizePolicy4)
        self.nazwa_23.setBaseSize(QSize(17, 10))
        self.nazwa_23.setFont(font3)
        self.nazwa_23.setAlignment(Qt.AlignCenter)

        self.pole_23.addWidget(self.nazwa_23)

        self.label_46 = QLabel(self.gra)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(150, 35))
        self.label_46.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_23.addWidget(self.label_46)

        self.gracze_23 = QListView(self.gra)
        self.gracze_23.setObjectName(u"gracze_23")
        sizePolicy2.setHeightForWidth(self.gracze_23.sizePolicy().hasHeightForWidth())
        self.gracze_23.setSizePolicy(sizePolicy2)
        self.gracze_23.setMinimumSize(QSize(0, 0))
        self.gracze_23.setMaximumSize(QSize(150, 100))

        self.pole_23.addWidget(self.gracze_23)

        self.label_47 = QLabel(self.gra)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.pole_23.addWidget(self.label_47)

        self.cena_23 = QLabel(self.gra)
        self.cena_23.setObjectName(u"cena_23")
        sizePolicy4.setHeightForWidth(self.cena_23.sizePolicy().hasHeightForWidth())
        self.cena_23.setSizePolicy(sizePolicy4)
        self.cena_23.setFont(font3)
        self.cena_23.setAlignment(Qt.AlignCenter)

        self.pole_23.addWidget(self.cena_23)

        self.pole_24 = QVBoxLayout()
        self.pole_24.setObjectName(u"pole_24")
        self.pole_24.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_24 = QLabel(self.gra)
        self.nazwa_24.setObjectName(u"nazwa_24")
        sizePolicy4.setHeightForWidth(self.nazwa_24.sizePolicy().hasHeightForWidth())
        self.nazwa_24.setSizePolicy(sizePolicy4)
        self.nazwa_24.setBaseSize(QSize(17, 10))
        self.nazwa_24.setFont(font3)
        self.nazwa_24.setAlignment(Qt.AlignCenter)

        self.pole_24.addWidget(self.nazwa_24)

        self.label_48 = QLabel(self.gra)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(150, 35))
        self.label_48.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_24.addWidget(self.label_48)

        self.gracze_24 = QListView(self.gra)
        self.gracze_24.setObjectName(u"gracze_24")
        sizePolicy2.setHeightForWidth(self.gracze_24.sizePolicy().hasHeightForWidth())
        self.gracze_24.setSizePolicy(sizePolicy2)
        self.gracze_24.setMinimumSize(QSize(0, 0))
        self.gracze_24.setMaximumSize(QSize(150, 100))

        self.pole_24.addWidget(self.gracze_24)

        self.label_49 = QLabel(self.gra)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.pole_24.addWidget(self.label_49)

        self.cena_24 = QLabel(self.gra)
        self.cena_24.setObjectName(u"cena_24")
        sizePolicy4.setHeightForWidth(self.cena_24.sizePolicy().hasHeightForWidth())
        self.cena_24.setSizePolicy(sizePolicy4)
        self.cena_24.setFont(font3)
        self.cena_24.setAlignment(Qt.AlignCenter)

        self.pole_24.addWidget(self.cena_24)


        self.pole_23.addLayout(self.pole_24)


        self.gridLayout_2.addLayout(self.pole_23, 7, 0, 1, 1)

        self.pole_4 = QVBoxLayout()
        self.pole_4.setObjectName(u"pole_4")
        self.pole_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_4 = QLabel(self.gra)
        self.nazwa_4.setObjectName(u"nazwa_4")
        sizePolicy4.setHeightForWidth(self.nazwa_4.sizePolicy().hasHeightForWidth())
        self.nazwa_4.setSizePolicy(sizePolicy4)
        self.nazwa_4.setBaseSize(QSize(17, 10))
        self.nazwa_4.setFont(font3)
        self.nazwa_4.setAlignment(Qt.AlignCenter)

        self.pole_4.addWidget(self.nazwa_4)

        self.label_8 = QLabel(self.gra)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 35))
        self.label_8.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_4.addWidget(self.label_8)

        self.gracze_4 = QListView(self.gra)
        self.gracze_4.setObjectName(u"gracze_4")
        sizePolicy2.setHeightForWidth(self.gracze_4.sizePolicy().hasHeightForWidth())
        self.gracze_4.setSizePolicy(sizePolicy2)
        self.gracze_4.setMinimumSize(QSize(0, 0))
        self.gracze_4.setMaximumSize(QSize(150, 100))

        self.pole_4.addWidget(self.gracze_4)

        self.label_9 = QLabel(self.gra)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.pole_4.addWidget(self.label_9)

        self.cena_4 = QLabel(self.gra)
        self.cena_4.setObjectName(u"cena_4")
        sizePolicy4.setHeightForWidth(self.cena_4.sizePolicy().hasHeightForWidth())
        self.cena_4.setSizePolicy(sizePolicy4)
        self.cena_4.setFont(font3)
        self.cena_4.setAlignment(Qt.AlignCenter)

        self.pole_4.addWidget(self.cena_4)


        self.gridLayout_2.addLayout(self.pole_4, 0, 3, 1, 1)

        self.pole_16 = QVBoxLayout()
        self.pole_16.setObjectName(u"pole_16")
        self.pole_16.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_16 = QLabel(self.gra)
        self.nazwa_16.setObjectName(u"nazwa_16")
        sizePolicy4.setHeightForWidth(self.nazwa_16.sizePolicy().hasHeightForWidth())
        self.nazwa_16.setSizePolicy(sizePolicy4)
        self.nazwa_16.setBaseSize(QSize(17, 10))
        self.nazwa_16.setFont(font3)
        self.nazwa_16.setAlignment(Qt.AlignCenter)

        self.pole_16.addWidget(self.nazwa_16)

        self.label_32 = QLabel(self.gra)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(150, 35))
        self.label_32.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_16.addWidget(self.label_32)

        self.gracze_16 = QListView(self.gra)
        self.gracze_16.setObjectName(u"gracze_16")
        sizePolicy2.setHeightForWidth(self.gracze_16.sizePolicy().hasHeightForWidth())
        self.gracze_16.setSizePolicy(sizePolicy2)
        self.gracze_16.setMinimumSize(QSize(0, 0))
        self.gracze_16.setMaximumSize(QSize(150, 100))

        self.pole_16.addWidget(self.gracze_16)

        self.label_33 = QLabel(self.gra)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.pole_16.addWidget(self.label_33)

        self.cena_16 = QLabel(self.gra)
        self.cena_16.setObjectName(u"cena_16")
        sizePolicy4.setHeightForWidth(self.cena_16.sizePolicy().hasHeightForWidth())
        self.cena_16.setSizePolicy(sizePolicy4)
        self.cena_16.setFont(font3)
        self.cena_16.setAlignment(Qt.AlignCenter)

        self.pole_16.addWidget(self.cena_16)


        self.gridLayout_2.addLayout(self.pole_16, 4, 0, 1, 1)

        self.pole_15 = QVBoxLayout()
        self.pole_15.setObjectName(u"pole_15")
        self.pole_15.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_15 = QLabel(self.gra)
        self.nazwa_15.setObjectName(u"nazwa_15")
        sizePolicy4.setHeightForWidth(self.nazwa_15.sizePolicy().hasHeightForWidth())
        self.nazwa_15.setSizePolicy(sizePolicy4)
        self.nazwa_15.setBaseSize(QSize(17, 10))
        self.nazwa_15.setFont(font3)
        self.nazwa_15.setAlignment(Qt.AlignCenter)

        self.pole_15.addWidget(self.nazwa_15)

        self.label_30 = QLabel(self.gra)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(150, 35))
        self.label_30.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_15.addWidget(self.label_30)

        self.gracze_15 = QListView(self.gra)
        self.gracze_15.setObjectName(u"gracze_15")
        sizePolicy2.setHeightForWidth(self.gracze_15.sizePolicy().hasHeightForWidth())
        self.gracze_15.setSizePolicy(sizePolicy2)
        self.gracze_15.setMinimumSize(QSize(0, 0))
        self.gracze_15.setMaximumSize(QSize(150, 100))

        self.pole_15.addWidget(self.gracze_15)

        self.label_31 = QLabel(self.gra)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.pole_15.addWidget(self.label_31)

        self.cena_15 = QLabel(self.gra)
        self.cena_15.setObjectName(u"cena_15")
        sizePolicy4.setHeightForWidth(self.cena_15.sizePolicy().hasHeightForWidth())
        self.cena_15.setSizePolicy(sizePolicy4)
        self.cena_15.setFont(font3)
        self.cena_15.setAlignment(Qt.AlignCenter)

        self.pole_15.addWidget(self.cena_15)


        self.gridLayout_2.addLayout(self.pole_15, 2, 9, 1, 1)

        self.pole_13 = QVBoxLayout()
        self.pole_13.setObjectName(u"pole_13")
        self.pole_13.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_13 = QLabel(self.gra)
        self.nazwa_13.setObjectName(u"nazwa_13")
        sizePolicy4.setHeightForWidth(self.nazwa_13.sizePolicy().hasHeightForWidth())
        self.nazwa_13.setSizePolicy(sizePolicy4)
        self.nazwa_13.setBaseSize(QSize(17, 10))
        self.nazwa_13.setFont(font3)
        self.nazwa_13.setAlignment(Qt.AlignCenter)

        self.pole_13.addWidget(self.nazwa_13)

        self.label_26 = QLabel(self.gra)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(150, 35))
        self.label_26.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_13.addWidget(self.label_26)

        self.gracze_13 = QListView(self.gra)
        self.gracze_13.setObjectName(u"gracze_13")
        sizePolicy2.setHeightForWidth(self.gracze_13.sizePolicy().hasHeightForWidth())
        self.gracze_13.setSizePolicy(sizePolicy2)
        self.gracze_13.setMinimumSize(QSize(0, 0))
        self.gracze_13.setMaximumSize(QSize(150, 100))

        self.pole_13.addWidget(self.gracze_13)

        self.label_27 = QLabel(self.gra)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.pole_13.addWidget(self.label_27)

        self.cena_13 = QLabel(self.gra)
        self.cena_13.setObjectName(u"cena_13")
        sizePolicy4.setHeightForWidth(self.cena_13.sizePolicy().hasHeightForWidth())
        self.cena_13.setSizePolicy(sizePolicy4)
        self.cena_13.setFont(font3)
        self.cena_13.setAlignment(Qt.AlignCenter)

        self.pole_13.addWidget(self.cena_13)


        self.gridLayout_2.addLayout(self.pole_13, 1, 0, 1, 1)

        self.pole_26 = QVBoxLayout()
        self.pole_26.setObjectName(u"pole_26")
        self.pole_26.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_26 = QLabel(self.gra)
        self.nazwa_26.setObjectName(u"nazwa_26")
        sizePolicy4.setHeightForWidth(self.nazwa_26.sizePolicy().hasHeightForWidth())
        self.nazwa_26.setSizePolicy(sizePolicy4)
        self.nazwa_26.setBaseSize(QSize(17, 10))
        self.nazwa_26.setFont(font3)
        self.nazwa_26.setAlignment(Qt.AlignCenter)

        self.pole_26.addWidget(self.nazwa_26)

        self.label_52 = QLabel(self.gra)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(150, 35))
        self.label_52.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_26.addWidget(self.label_52)

        self.gracze_26 = QListView(self.gra)
        self.gracze_26.setObjectName(u"gracze_26")
        sizePolicy2.setHeightForWidth(self.gracze_26.sizePolicy().hasHeightForWidth())
        self.gracze_26.setSizePolicy(sizePolicy2)
        self.gracze_26.setMinimumSize(QSize(0, 0))
        self.gracze_26.setMaximumSize(QSize(150, 100))

        self.pole_26.addWidget(self.gracze_26)

        self.label_53 = QLabel(self.gra)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.pole_26.addWidget(self.label_53)

        self.cena_26 = QLabel(self.gra)
        self.cena_26.setObjectName(u"cena_26")
        sizePolicy4.setHeightForWidth(self.cena_26.sizePolicy().hasHeightForWidth())
        self.cena_26.setSizePolicy(sizePolicy4)
        self.cena_26.setFont(font3)
        self.cena_26.setAlignment(Qt.AlignCenter)

        self.pole_26.addWidget(self.cena_26)


        self.gridLayout_2.addLayout(self.pole_26, 9, 0, 1, 1)

        self.pole_27 = QVBoxLayout()
        self.pole_27.setObjectName(u"pole_27")
        self.pole_27.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_27 = QLabel(self.gra)
        self.nazwa_27.setObjectName(u"nazwa_27")
        sizePolicy4.setHeightForWidth(self.nazwa_27.sizePolicy().hasHeightForWidth())
        self.nazwa_27.setSizePolicy(sizePolicy4)
        self.nazwa_27.setBaseSize(QSize(17, 10))
        self.nazwa_27.setFont(font3)
        self.nazwa_27.setAlignment(Qt.AlignCenter)

        self.pole_27.addWidget(self.nazwa_27)

        self.label_54 = QLabel(self.gra)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(150, 35))
        self.label_54.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_27.addWidget(self.label_54)

        self.gracze_27 = QListView(self.gra)
        self.gracze_27.setObjectName(u"gracze_27")
        sizePolicy2.setHeightForWidth(self.gracze_27.sizePolicy().hasHeightForWidth())
        self.gracze_27.setSizePolicy(sizePolicy2)
        self.gracze_27.setMinimumSize(QSize(0, 0))
        self.gracze_27.setMaximumSize(QSize(150, 100))

        self.pole_27.addWidget(self.gracze_27)

        self.label_55 = QLabel(self.gra)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.pole_27.addWidget(self.label_55)

        self.cena_27 = QLabel(self.gra)
        self.cena_27.setObjectName(u"cena_27")
        sizePolicy4.setHeightForWidth(self.cena_27.sizePolicy().hasHeightForWidth())
        self.cena_27.setSizePolicy(sizePolicy4)
        self.cena_27.setFont(font3)
        self.cena_27.setAlignment(Qt.AlignCenter)

        self.pole_27.addWidget(self.cena_27)


        self.gridLayout_2.addLayout(self.pole_27, 9, 1, 1, 1)

        self.pole_29 = QVBoxLayout()
        self.pole_29.setObjectName(u"pole_29")
        self.pole_29.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_29 = QLabel(self.gra)
        self.nazwa_29.setObjectName(u"nazwa_29")
        sizePolicy4.setHeightForWidth(self.nazwa_29.sizePolicy().hasHeightForWidth())
        self.nazwa_29.setSizePolicy(sizePolicy4)
        self.nazwa_29.setBaseSize(QSize(17, 10))
        self.nazwa_29.setFont(font3)
        self.nazwa_29.setAlignment(Qt.AlignCenter)

        self.pole_29.addWidget(self.nazwa_29)

        self.label_58 = QLabel(self.gra)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(150, 35))
        self.label_58.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_29.addWidget(self.label_58)

        self.gracze_29 = QListView(self.gra)
        self.gracze_29.setObjectName(u"gracze_29")
        sizePolicy2.setHeightForWidth(self.gracze_29.sizePolicy().hasHeightForWidth())
        self.gracze_29.setSizePolicy(sizePolicy2)
        self.gracze_29.setMinimumSize(QSize(0, 0))
        self.gracze_29.setMaximumSize(QSize(150, 100))

        self.pole_29.addWidget(self.gracze_29)

        self.label_59 = QLabel(self.gra)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.pole_29.addWidget(self.label_59)

        self.cena_29 = QLabel(self.gra)
        self.cena_29.setObjectName(u"cena_29")
        sizePolicy4.setHeightForWidth(self.cena_29.sizePolicy().hasHeightForWidth())
        self.cena_29.setSizePolicy(sizePolicy4)
        self.cena_29.setFont(font3)
        self.cena_29.setAlignment(Qt.AlignCenter)

        self.pole_29.addWidget(self.cena_29)


        self.gridLayout_2.addLayout(self.pole_29, 9, 2, 1, 1)

        self.pole_30 = QVBoxLayout()
        self.pole_30.setObjectName(u"pole_30")
        self.pole_30.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_30 = QLabel(self.gra)
        self.nazwa_30.setObjectName(u"nazwa_30")
        sizePolicy4.setHeightForWidth(self.nazwa_30.sizePolicy().hasHeightForWidth())
        self.nazwa_30.setSizePolicy(sizePolicy4)
        self.nazwa_30.setBaseSize(QSize(17, 10))
        self.nazwa_30.setFont(font3)
        self.nazwa_30.setAlignment(Qt.AlignCenter)

        self.pole_30.addWidget(self.nazwa_30)

        self.label_60 = QLabel(self.gra)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(150, 35))
        self.label_60.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_30.addWidget(self.label_60)

        self.gracze_30 = QListView(self.gra)
        self.gracze_30.setObjectName(u"gracze_30")
        sizePolicy2.setHeightForWidth(self.gracze_30.sizePolicy().hasHeightForWidth())
        self.gracze_30.setSizePolicy(sizePolicy2)
        self.gracze_30.setMinimumSize(QSize(0, 0))
        self.gracze_30.setMaximumSize(QSize(150, 100))

        self.pole_30.addWidget(self.gracze_30)

        self.label_61 = QLabel(self.gra)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.pole_30.addWidget(self.label_61)

        self.cena_30 = QLabel(self.gra)
        self.cena_30.setObjectName(u"cena_30")
        sizePolicy4.setHeightForWidth(self.cena_30.sizePolicy().hasHeightForWidth())
        self.cena_30.setSizePolicy(sizePolicy4)
        self.cena_30.setFont(font3)
        self.cena_30.setAlignment(Qt.AlignCenter)

        self.pole_30.addWidget(self.cena_30)


        self.gridLayout_2.addLayout(self.pole_30, 9, 3, 1, 1)

        self.pole_31 = QVBoxLayout()
        self.pole_31.setObjectName(u"pole_31")
        self.pole_31.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_31 = QLabel(self.gra)
        self.nazwa_31.setObjectName(u"nazwa_31")
        sizePolicy4.setHeightForWidth(self.nazwa_31.sizePolicy().hasHeightForWidth())
        self.nazwa_31.setSizePolicy(sizePolicy4)
        self.nazwa_31.setBaseSize(QSize(17, 10))
        self.nazwa_31.setFont(font3)
        self.nazwa_31.setAlignment(Qt.AlignCenter)

        self.pole_31.addWidget(self.nazwa_31)

        self.label_62 = QLabel(self.gra)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(150, 35))
        self.label_62.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_31.addWidget(self.label_62)

        self.gracze_31 = QListView(self.gra)
        self.gracze_31.setObjectName(u"gracze_31")
        sizePolicy2.setHeightForWidth(self.gracze_31.sizePolicy().hasHeightForWidth())
        self.gracze_31.setSizePolicy(sizePolicy2)
        self.gracze_31.setMinimumSize(QSize(0, 0))
        self.gracze_31.setMaximumSize(QSize(150, 100))

        self.pole_31.addWidget(self.gracze_31)

        self.label_63 = QLabel(self.gra)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.pole_31.addWidget(self.label_63)

        self.cena_31 = QLabel(self.gra)
        self.cena_31.setObjectName(u"cena_31")
        sizePolicy4.setHeightForWidth(self.cena_31.sizePolicy().hasHeightForWidth())
        self.cena_31.setSizePolicy(sizePolicy4)
        self.cena_31.setFont(font3)
        self.cena_31.setAlignment(Qt.AlignCenter)

        self.pole_31.addWidget(self.cena_31)


        self.gridLayout_2.addLayout(self.pole_31, 9, 4, 1, 1)

        self.pole_32 = QVBoxLayout()
        self.pole_32.setObjectName(u"pole_32")
        self.pole_32.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_32 = QLabel(self.gra)
        self.nazwa_32.setObjectName(u"nazwa_32")
        sizePolicy4.setHeightForWidth(self.nazwa_32.sizePolicy().hasHeightForWidth())
        self.nazwa_32.setSizePolicy(sizePolicy4)
        self.nazwa_32.setBaseSize(QSize(17, 10))
        self.nazwa_32.setFont(font3)
        self.nazwa_32.setAlignment(Qt.AlignCenter)

        self.pole_32.addWidget(self.nazwa_32)

        self.label_64 = QLabel(self.gra)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(150, 35))
        self.label_64.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_32.addWidget(self.label_64)

        self.gracze_32 = QListView(self.gra)
        self.gracze_32.setObjectName(u"gracze_32")
        sizePolicy2.setHeightForWidth(self.gracze_32.sizePolicy().hasHeightForWidth())
        self.gracze_32.setSizePolicy(sizePolicy2)
        self.gracze_32.setMinimumSize(QSize(0, 0))
        self.gracze_32.setMaximumSize(QSize(150, 100))

        self.pole_32.addWidget(self.gracze_32)

        self.label_65 = QLabel(self.gra)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.pole_32.addWidget(self.label_65)

        self.cena_32 = QLabel(self.gra)
        self.cena_32.setObjectName(u"cena_32")
        sizePolicy4.setHeightForWidth(self.cena_32.sizePolicy().hasHeightForWidth())
        self.cena_32.setSizePolicy(sizePolicy4)
        self.cena_32.setFont(font3)
        self.cena_32.setAlignment(Qt.AlignCenter)

        self.pole_32.addWidget(self.cena_32)


        self.gridLayout_2.addLayout(self.pole_32, 9, 5, 1, 1)

        self.pole_33 = QVBoxLayout()
        self.pole_33.setObjectName(u"pole_33")
        self.pole_33.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_33 = QLabel(self.gra)
        self.nazwa_33.setObjectName(u"nazwa_33")
        sizePolicy4.setHeightForWidth(self.nazwa_33.sizePolicy().hasHeightForWidth())
        self.nazwa_33.setSizePolicy(sizePolicy4)
        self.nazwa_33.setBaseSize(QSize(17, 10))
        self.nazwa_33.setFont(font3)
        self.nazwa_33.setAlignment(Qt.AlignCenter)

        self.pole_33.addWidget(self.nazwa_33)

        self.label_66 = QLabel(self.gra)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(150, 35))
        self.label_66.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_33.addWidget(self.label_66)

        self.gracze_33 = QListView(self.gra)
        self.gracze_33.setObjectName(u"gracze_33")
        sizePolicy2.setHeightForWidth(self.gracze_33.sizePolicy().hasHeightForWidth())
        self.gracze_33.setSizePolicy(sizePolicy2)
        self.gracze_33.setMinimumSize(QSize(0, 0))
        self.gracze_33.setMaximumSize(QSize(150, 100))

        self.pole_33.addWidget(self.gracze_33)

        self.label_67 = QLabel(self.gra)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignCenter)

        self.pole_33.addWidget(self.label_67)

        self.cena_33 = QLabel(self.gra)
        self.cena_33.setObjectName(u"cena_33")
        sizePolicy4.setHeightForWidth(self.cena_33.sizePolicy().hasHeightForWidth())
        self.cena_33.setSizePolicy(sizePolicy4)
        self.cena_33.setFont(font3)
        self.cena_33.setAlignment(Qt.AlignCenter)

        self.pole_33.addWidget(self.cena_33)


        self.gridLayout_2.addLayout(self.pole_33, 9, 6, 1, 1)

        self.pole_34 = QVBoxLayout()
        self.pole_34.setObjectName(u"pole_34")
        self.pole_34.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_34 = QLabel(self.gra)
        self.nazwa_34.setObjectName(u"nazwa_34")
        sizePolicy4.setHeightForWidth(self.nazwa_34.sizePolicy().hasHeightForWidth())
        self.nazwa_34.setSizePolicy(sizePolicy4)
        self.nazwa_34.setBaseSize(QSize(17, 10))
        self.nazwa_34.setFont(font3)
        self.nazwa_34.setAlignment(Qt.AlignCenter)

        self.pole_34.addWidget(self.nazwa_34)

        self.label_68 = QLabel(self.gra)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(150, 35))
        self.label_68.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_34.addWidget(self.label_68)

        self.gracze_34 = QListView(self.gra)
        self.gracze_34.setObjectName(u"gracze_34")
        sizePolicy2.setHeightForWidth(self.gracze_34.sizePolicy().hasHeightForWidth())
        self.gracze_34.setSizePolicy(sizePolicy2)
        self.gracze_34.setMinimumSize(QSize(0, 0))
        self.gracze_34.setMaximumSize(QSize(150, 100))

        self.pole_34.addWidget(self.gracze_34)

        self.label_69 = QLabel(self.gra)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setAlignment(Qt.AlignCenter)

        self.pole_34.addWidget(self.label_69)

        self.cena_34 = QLabel(self.gra)
        self.cena_34.setObjectName(u"cena_34")
        sizePolicy4.setHeightForWidth(self.cena_34.sizePolicy().hasHeightForWidth())
        self.cena_34.setSizePolicy(sizePolicy4)
        self.cena_34.setFont(font3)
        self.cena_34.setAlignment(Qt.AlignCenter)

        self.pole_34.addWidget(self.cena_34)


        self.gridLayout_2.addLayout(self.pole_34, 9, 7, 1, 1)

        self.pole_35 = QVBoxLayout()
        self.pole_35.setObjectName(u"pole_35")
        self.pole_35.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_35 = QLabel(self.gra)
        self.nazwa_35.setObjectName(u"nazwa_35")
        sizePolicy4.setHeightForWidth(self.nazwa_35.sizePolicy().hasHeightForWidth())
        self.nazwa_35.setSizePolicy(sizePolicy4)
        self.nazwa_35.setBaseSize(QSize(17, 10))
        self.nazwa_35.setFont(font3)
        self.nazwa_35.setAlignment(Qt.AlignCenter)

        self.pole_35.addWidget(self.nazwa_35)

        self.label_70 = QLabel(self.gra)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(150, 35))
        self.label_70.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_35.addWidget(self.label_70)

        self.gracze_35 = QListView(self.gra)
        self.gracze_35.setObjectName(u"gracze_35")
        sizePolicy2.setHeightForWidth(self.gracze_35.sizePolicy().hasHeightForWidth())
        self.gracze_35.setSizePolicy(sizePolicy2)
        self.gracze_35.setMinimumSize(QSize(0, 0))
        self.gracze_35.setMaximumSize(QSize(150, 100))

        self.pole_35.addWidget(self.gracze_35)

        self.label_71 = QLabel(self.gra)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.pole_35.addWidget(self.label_71)

        self.cena_35 = QLabel(self.gra)
        self.cena_35.setObjectName(u"cena_35")
        sizePolicy4.setHeightForWidth(self.cena_35.sizePolicy().hasHeightForWidth())
        self.cena_35.setSizePolicy(sizePolicy4)
        self.cena_35.setFont(font3)
        self.cena_35.setAlignment(Qt.AlignCenter)

        self.pole_35.addWidget(self.cena_35)


        self.gridLayout_2.addLayout(self.pole_35, 9, 8, 1, 1)

        self.pole_36 = QVBoxLayout()
        self.pole_36.setObjectName(u"pole_36")
        self.pole_36.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_36 = QLabel(self.gra)
        self.nazwa_36.setObjectName(u"nazwa_36")
        sizePolicy4.setHeightForWidth(self.nazwa_36.sizePolicy().hasHeightForWidth())
        self.nazwa_36.setSizePolicy(sizePolicy4)
        self.nazwa_36.setBaseSize(QSize(17, 10))
        self.nazwa_36.setFont(font3)
        self.nazwa_36.setAlignment(Qt.AlignCenter)

        self.pole_36.addWidget(self.nazwa_36)

        self.label_72 = QLabel(self.gra)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(150, 35))
        self.label_72.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_36.addWidget(self.label_72)

        self.gracze_36 = QListView(self.gra)
        self.gracze_36.setObjectName(u"gracze_36")
        sizePolicy2.setHeightForWidth(self.gracze_36.sizePolicy().hasHeightForWidth())
        self.gracze_36.setSizePolicy(sizePolicy2)
        self.gracze_36.setMinimumSize(QSize(0, 0))
        self.gracze_36.setMaximumSize(QSize(150, 100))

        self.pole_36.addWidget(self.gracze_36)

        self.label_73 = QLabel(self.gra)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setAlignment(Qt.AlignCenter)

        self.pole_36.addWidget(self.label_73)

        self.cena_36 = QLabel(self.gra)
        self.cena_36.setObjectName(u"cena_36")
        sizePolicy4.setHeightForWidth(self.cena_36.sizePolicy().hasHeightForWidth())
        self.cena_36.setSizePolicy(sizePolicy4)
        self.cena_36.setFont(font3)
        self.cena_36.setAlignment(Qt.AlignCenter)

        self.pole_36.addWidget(self.cena_36)


        self.gridLayout_2.addLayout(self.pole_36, 9, 9, 1, 1)

        self.pole_37 = QVBoxLayout()
        self.pole_37.setObjectName(u"pole_37")
        self.pole_37.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_37 = QLabel(self.gra)
        self.nazwa_37.setObjectName(u"nazwa_37")
        sizePolicy4.setHeightForWidth(self.nazwa_37.sizePolicy().hasHeightForWidth())
        self.nazwa_37.setSizePolicy(sizePolicy4)
        self.nazwa_37.setBaseSize(QSize(17, 10))
        self.nazwa_37.setFont(font3)
        self.nazwa_37.setAlignment(Qt.AlignCenter)

        self.pole_37.addWidget(self.nazwa_37)

        self.label_74 = QLabel(self.gra)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMaximumSize(QSize(150, 35))
        self.label_74.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_37.addWidget(self.label_74)

        self.gracze_37 = QListView(self.gra)
        self.gracze_37.setObjectName(u"gracze_37")
        sizePolicy2.setHeightForWidth(self.gracze_37.sizePolicy().hasHeightForWidth())
        self.gracze_37.setSizePolicy(sizePolicy2)
        self.gracze_37.setMinimumSize(QSize(0, 0))
        self.gracze_37.setMaximumSize(QSize(150, 100))

        self.pole_37.addWidget(self.gracze_37)

        self.label_75 = QLabel(self.gra)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setAlignment(Qt.AlignCenter)

        self.pole_37.addWidget(self.label_75)

        self.cena_37 = QLabel(self.gra)
        self.cena_37.setObjectName(u"cena_37")
        sizePolicy4.setHeightForWidth(self.cena_37.sizePolicy().hasHeightForWidth())
        self.cena_37.setSizePolicy(sizePolicy4)
        self.cena_37.setFont(font3)
        self.cena_37.setAlignment(Qt.AlignCenter)

        self.pole_37.addWidget(self.cena_37)


        self.gridLayout_2.addLayout(self.pole_37, 8, 9, 1, 1)

        self.pole_38 = QVBoxLayout()
        self.pole_38.setObjectName(u"pole_38")
        self.pole_38.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_38 = QLabel(self.gra)
        self.nazwa_38.setObjectName(u"nazwa_38")
        sizePolicy4.setHeightForWidth(self.nazwa_38.sizePolicy().hasHeightForWidth())
        self.nazwa_38.setSizePolicy(sizePolicy4)
        self.nazwa_38.setBaseSize(QSize(17, 10))
        self.nazwa_38.setFont(font3)
        self.nazwa_38.setAlignment(Qt.AlignCenter)

        self.pole_38.addWidget(self.nazwa_38)

        self.label_76 = QLabel(self.gra)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMaximumSize(QSize(150, 35))
        self.label_76.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_38.addWidget(self.label_76)

        self.gracze_38 = QListView(self.gra)
        self.gracze_38.setObjectName(u"gracze_38")
        sizePolicy2.setHeightForWidth(self.gracze_38.sizePolicy().hasHeightForWidth())
        self.gracze_38.setSizePolicy(sizePolicy2)
        self.gracze_38.setMinimumSize(QSize(0, 0))
        self.gracze_38.setMaximumSize(QSize(150, 100))

        self.pole_38.addWidget(self.gracze_38)

        self.label_77 = QLabel(self.gra)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setAlignment(Qt.AlignCenter)

        self.pole_38.addWidget(self.label_77)

        self.cena_38 = QLabel(self.gra)
        self.cena_38.setObjectName(u"cena_38")
        sizePolicy4.setHeightForWidth(self.cena_38.sizePolicy().hasHeightForWidth())
        self.cena_38.setSizePolicy(sizePolicy4)
        self.cena_38.setFont(font3)
        self.cena_38.setAlignment(Qt.AlignCenter)

        self.pole_38.addWidget(self.cena_38)


        self.gridLayout_2.addLayout(self.pole_38, 7, 9, 1, 1)

        self.pole_39 = QVBoxLayout()
        self.pole_39.setObjectName(u"pole_39")
        self.pole_39.setSizeConstraint(QLayout.SetMinimumSize)
        self.nazwa_39 = QLabel(self.gra)
        self.nazwa_39.setObjectName(u"nazwa_39")
        sizePolicy4.setHeightForWidth(self.nazwa_39.sizePolicy().hasHeightForWidth())
        self.nazwa_39.setSizePolicy(sizePolicy4)
        self.nazwa_39.setBaseSize(QSize(17, 10))
        self.nazwa_39.setFont(font3)
        self.nazwa_39.setAlignment(Qt.AlignCenter)

        self.pole_39.addWidget(self.nazwa_39)

        self.label_78 = QLabel(self.gra)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(150, 35))
        self.label_78.setStyleSheet(u"background-color: rgb(153, 0, 0);")

        self.pole_39.addWidget(self.label_78)

        self.gracze_39 = QListView(self.gra)
        self.gracze_39.setObjectName(u"gracze_39")
        sizePolicy2.setHeightForWidth(self.gracze_39.sizePolicy().hasHeightForWidth())
        self.gracze_39.setSizePolicy(sizePolicy2)
        self.gracze_39.setMinimumSize(QSize(0, 0))
        self.gracze_39.setMaximumSize(QSize(150, 100))

        self.pole_39.addWidget(self.gracze_39)

        self.label_79 = QLabel(self.gra)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.pole_39.addWidget(self.label_79)

        self.cena_39 = QLabel(self.gra)
        self.cena_39.setObjectName(u"cena_39")
        sizePolicy4.setHeightForWidth(self.cena_39.sizePolicy().hasHeightForWidth())
        self.cena_39.setSizePolicy(sizePolicy4)
        self.cena_39.setFont(font3)
        self.cena_39.setAlignment(Qt.AlignCenter)

        self.pole_39.addWidget(self.cena_39)


        self.gridLayout_2.addLayout(self.pole_39, 6, 9, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.Tura = QLabel(self.gra)
        self.Tura.setObjectName(u"Tura")
        self.Tura.setFont(font2)

        self.verticalLayout_4.addWidget(self.Tura)

        self.plansze.addWidget(self.gra)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1188, 20))
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
        self.KupDomekButton.setText(QCoreApplication.translate("MainWindow", u"Kup domek", None))
        self.RzutButton.setText(QCoreApplication.translate("MainWindow", u"Rzu\u0107 kostk\u0105", None))
        self.WynikRzutu.setText("")
        self.nazwa.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.cena.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.cena_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText("")
        self.label_23.setText("")
        self.cena_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText("")
        self.label_29.setText("")
        self.cena_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText("")
        self.label_45.setText("")
        self.cena_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText("")
        self.label_35.setText("")
        self.cena_17.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.cena_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText("")
        self.label_37.setText("")
        self.cena_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText("")
        self.label_21.setText("")
        self.cena_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText("")
        self.label_17.setText("")
        self.cena_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText("")
        self.label_13.setText("")
        self.cena_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText("")
        self.label_43.setText("")
        self.cena_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText("")
        self.label_25.setText("")
        self.cena_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_50.setText("")
        self.label_51.setText("")
        self.cena_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.cena_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.cena_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.cena_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText("")
        self.label_39.setText("")
        self.cena_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText("")
        self.label_47.setText("")
        self.cena_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText("")
        self.label_49.setText("")
        self.cena_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.cena_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText("")
        self.label_33.setText("")
        self.cena_16.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.cena_15.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText("")
        self.label_27.setText("")
        self.cena_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText("")
        self.label_53.setText("")
        self.cena_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_54.setText("")
        self.label_55.setText("")
        self.cena_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_58.setText("")
        self.label_59.setText("")
        self.cena_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText("")
        self.label_61.setText("")
        self.cena_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_62.setText("")
        self.label_63.setText("")
        self.cena_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText("")
        self.label_65.setText("")
        self.cena_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_66.setText("")
        self.label_67.setText("")
        self.cena_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_68.setText("")
        self.label_69.setText("")
        self.cena_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_70.setText("")
        self.label_71.setText("")
        self.cena_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_72.setText("")
        self.label_73.setText("")
        self.cena_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_74.setText("")
        self.label_75.setText("")
        self.cena_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_76.setText("")
        self.label_77.setText("")
        self.cena_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.nazwa_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_78.setText("")
        self.label_79.setText("")
        self.cena_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Tura.setText(QCoreApplication.translate("MainWindow", u"Tura gracza: ", None))
    # retranslateUi

