# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(812, 522)
        icon = QIcon()
        icon.addFile(u"icons/diary.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralWidget {\n"
"background-color: rgb(236, 212, 157);\n"
"}\n"
"\n"
"#addEventButton {\n"
"border: 1px solid rgba(94, 94, 94, 0.5);\n"
"height: 35px;\n"
"border-radius: 17px;\n"
"background-color: rgb(255, 241, 128);\n"
"}\n"
"\n"
"#addEventButton:hover {\n"
"border: 1px solid rgba(94, 94, 94, 0.5);\n"
"border-radius: 17px;\n"
"background-color: rgb(202, 196, 123);\n"
"}\n"
"\n"
"#rightSize, #leftSize {\n"
"border: 2px solid rgb(241, 196, 82) ;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#timeToEventLabel {\n"
"color: rgb(255, 212, 103);\n"
"}\n"
"\n"
"#calendarWidget QWidget {\n"
"background-color: rgb(255, 225, 103);\n"
"}\n"
"\n"
"#centralwidget {\n"
"background-color: rgb(253, 255, 221)\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 7)
        self.leftSize = QWidget(self.main)
        self.leftSize.setObjectName(u"leftSize")
        self.verticalLayout = QVBoxLayout(self.leftSize)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendarWidget = QCalendarWidget(self.leftSize)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout.addWidget(self.calendarWidget)

        self.addEventButton = QPushButton(self.leftSize)
        self.addEventButton.setObjectName(u"addEventButton")
        self.addEventButton.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Segoe UI Variable Small Semibol")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.addEventButton.setFont(font)
        self.addEventButton.setCursor(QCursor(Qt.ArrowCursor))
        self.addEventButton.setIconSize(QSize(14, 14))

        self.verticalLayout.addWidget(self.addEventButton)


        self.horizontalLayout_2.addWidget(self.leftSize)

        self.rightSize = QWidget(self.main)
        self.rightSize.setObjectName(u"rightSize")
        self.verticalLayout_2 = QVBoxLayout(self.rightSize)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.rightSize)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamily(u"Nirmala UI Semilight")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_2.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.timeToEventLabel = QLabel(self.rightSize)
        self.timeToEventLabel.setObjectName(u"timeToEventLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Variable Display")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.timeToEventLabel.setFont(font2)

        self.verticalLayout_2.addWidget(self.timeToEventLabel, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.rightSize)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0429\u043e\u0434\u0435\u043d\u043d\u0438\u043a", None))
        self.addEventButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0437\u0430\u0445\u0456\u0434", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u0445\u043e\u0434\u0456\u0432", None))
        self.timeToEventLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e \u043d\u0430\u0439\u0431\u043b\u0438\u0436\u0447\u043e\u0433\u043e \u0437\u0430\u0445\u043e\u0434\u0443: XX \u0434\u043d\u0456\u0432", None))
    # retranslateUi

