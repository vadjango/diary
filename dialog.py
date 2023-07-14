# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(607, 468)
        icon = QIcon()
        icon.addFile(u"icons/book.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainWidget = QWidget(Dialog)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setMinimumSize(QSize(490, 300))
        self.mainWidget.setMaximumSize(QSize(16777215, 16777215))
        self.mainWidget.setBaseSize(QSize(0, 0))
        self.mainWidget.setStyleSheet(u"#mainWidget {\n"
"background-color: rgb(251, 255, 207)\n"
"}\n"
"\n"
"#eventName, #groupBox_2, #groupBox, #groupBox_3, #groupBox_4 {\n"
"border: none;\n"
"}\n"
"\n"
"#eventName, #eventDescription, #placeEdit {\n"
"background-color: rgb(240, 223, 137);\n"
"border-radius: 6px;\n"
"margin-left: 6px;\n"
"}\n"
"\n"
"#minuteSpin, #hourSpin, #durationSpin, #comboBoxDuration {\n"
"background-color: rgb(240, 223, 137);\n"
"}\n"
"\n"
"#Dialog {\n"
"backround-color: rgb(247, 255, 148)\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 16, -1)
        self.leftWidget = QWidget(self.mainWidget)
        self.leftWidget.setObjectName(u"leftWidget")
        self.verticalLayout_2 = QVBoxLayout(self.leftWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, -1, -1, -1)
        self.nameBox = QGroupBox(self.leftWidget)
        self.nameBox.setObjectName(u"nameBox")
        self.nameBox.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nameBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.nameBox)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.eventName = QLineEdit(self.nameBox)
        self.eventName.setObjectName(u"eventName")
        self.eventName.setMinimumSize(QSize(0, 22))
        self.eventName.setBaseSize(QSize(0, 0))

        self.verticalLayout_5.addWidget(self.eventName)


        self.verticalLayout_2.addWidget(self.nameBox)

        self.descriptionBox = QGroupBox(self.leftWidget)
        self.descriptionBox.setObjectName(u"descriptionBox")
        self.descriptionBox.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.descriptionBox)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.eventDescription = QPlainTextEdit(self.descriptionBox)
        self.eventDescription.setObjectName(u"eventDescription")

        self.verticalLayout_4.addWidget(self.eventDescription)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.saveButton = QPushButton(self.descriptionBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Historic")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.saveButton.setFont(font1)
        self.saveButton.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.saveButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.descriptionBox)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 16)

        self.horizontalLayout.addWidget(self.leftWidget)

        self.rightWidget = QWidget(self.mainWidget)
        self.rightWidget.setObjectName(u"rightWidget")
        self.verticalLayout_3 = QVBoxLayout(self.rightWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.timeBox = QGroupBox(self.rightWidget)
        self.timeBox.setObjectName(u"timeBox")
        self.timeBox.setMinimumSize(QSize(0, 0))
        self.timeBox.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.timeBox)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 8, 6)
        self.timeWidget = QWidget(self.timeBox)
        self.timeWidget.setObjectName(u"timeWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.timeWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hourSpin = QSpinBox(self.timeWidget)
        self.hourSpin.setObjectName(u"hourSpin")
        self.hourSpin.setMaximum(23)

        self.horizontalLayout_3.addWidget(self.hourSpin)

        self.hourLabel = QLabel(self.timeWidget)
        self.hourLabel.setObjectName(u"hourLabel")

        self.horizontalLayout_3.addWidget(self.hourLabel)

        self.minuteSpin = QSpinBox(self.timeWidget)
        self.minuteSpin.setObjectName(u"minuteSpin")
        self.minuteSpin.setMaximum(59)

        self.horizontalLayout_3.addWidget(self.minuteSpin)

        self.minuteLabel = QLabel(self.timeWidget)
        self.minuteLabel.setObjectName(u"minuteLabel")

        self.horizontalLayout_3.addWidget(self.minuteLabel)


        self.verticalLayout_6.addWidget(self.timeWidget)


        self.verticalLayout_3.addWidget(self.timeBox)

        self.durationBox = QGroupBox(self.rightWidget)
        self.durationBox.setObjectName(u"durationBox")
        self.durationBox.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.durationBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.durationWidget = QWidget(self.durationBox)
        self.durationWidget.setObjectName(u"durationWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.durationWidget)
        self.horizontalLayout_5.setSpacing(31)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 60, -1)
        self.durationSpin = QSpinBox(self.durationWidget)
        self.durationSpin.setObjectName(u"durationSpin")

        self.horizontalLayout_5.addWidget(self.durationSpin)

        self.comboBoxDuration = QComboBox(self.durationWidget)
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.setObjectName(u"comboBoxDuration")

        self.horizontalLayout_5.addWidget(self.comboBoxDuration)


        self.verticalLayout_7.addWidget(self.durationWidget)


        self.verticalLayout_3.addWidget(self.durationBox)

        self.placeBox = QGroupBox(self.rightWidget)
        self.placeBox.setObjectName(u"placeBox")
        self.placeBox.setFont(font)
        self.placeEdit = QLineEdit(self.placeBox)
        self.placeEdit.setObjectName(u"placeEdit")
        self.placeEdit.setGeometry(QRect(7, 34, 221, 21))

        self.verticalLayout_3.addWidget(self.placeBox)


        self.horizontalLayout.addWidget(self.rightWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.mainWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0437\u0430\u0445\u0456\u0434", None))
        self.nameBox.setTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430 \u0437\u0430\u0445\u043e\u0434\u0443", None))
        self.eventName.setText("")
        self.descriptionBox.setTitle(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441 \u0437\u0430\u0445\u043e\u0434\u0443", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
        self.timeBox.setTitle(QCoreApplication.translate("Dialog", u"\u0427\u0430\u0441 \u0437\u0430\u0445\u043e\u0434\u0443", None))
        self.hourLabel.setText(QCoreApplication.translate("Dialog", u"\u0433", None))
        self.minuteLabel.setText(QCoreApplication.translate("Dialog", u"\u0445\u0432", None))
        self.durationBox.setTitle(QCoreApplication.translate("Dialog", u"\u0422\u0440\u0438\u0432\u0430\u043b\u0456\u0441\u0442\u044c \u0437\u0430\u0445\u043e\u0434\u0443", None))
        self.comboBoxDuration.setItemText(0, QCoreApplication.translate("Dialog", u"\u0433\u043e\u0434", None))
        self.comboBoxDuration.setItemText(1, QCoreApplication.translate("Dialog", u"\u0445\u0432", None))

        self.placeBox.setTitle(QCoreApplication.translate("Dialog", u"\u041c\u0456\u0441\u0446\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f", None))
    # retranslateUi

