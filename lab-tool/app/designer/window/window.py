# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LabToolWindow(object):
    def setupUi(self, LabToolWindow):
        LabToolWindow.setObjectName("LabToolWindow")
        LabToolWindow.resize(740, 329)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LabToolWindow.sizePolicy().hasHeightForWidth())
        LabToolWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(LabToolWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.device_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_page.sizePolicy().hasHeightForWidth())
        self.device_page.setSizePolicy(sizePolicy)
        self.device_page.setObjectName("device_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.device_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.refresh = QtWidgets.QPushButton(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        self.refresh.setMinimumSize(QtCore.QSize(40, 40))
        self.refresh.setStyleSheet("QPushButton {\n"
"    border-image: url(:/refresh/refresh_normal.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/refresh/refresh_hover.png);\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-image: url(:/refresh/refresh_pressed.png);\n"
"    background-repeat: no-repeat;\n"
"}")
        self.refresh.setText("")
        self.refresh.setIconSize(QtCore.QSize(16, 16))
        self.refresh.setObjectName("refresh")
        self.horizontalLayout_6.addWidget(self.refresh, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label = QtWidgets.QLabel(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.generators = QtWidgets.QComboBox(self.device_page)
        self.generators.setObjectName("generators")
        self.gridLayout.addWidget(self.generators, 1, 2, 1, 1)
        self.oscilloscopes = QtWidgets.QComboBox(self.device_page)
        self.oscilloscopes.setObjectName("oscilloscopes")
        self.gridLayout.addWidget(self.oscilloscopes, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.widget = QtWidgets.QWidget(self.device_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.connection_status = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.connection_status.setFont(font)
        self.connection_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.connection_status.setWordWrap(True)
        self.connection_status.setObjectName("connection_status")
        self.gridLayout_3.addWidget(self.connection_status, 0, 0, 1, 1)
        self.connection = QtWidgets.QPushButton(self.widget)
        self.connection.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection.sizePolicy().hasHeightForWidth())
        self.connection.setSizePolicy(sizePolicy)
        self.connection.setObjectName("connection")
        self.gridLayout_3.addWidget(self.connection, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.stackedWidget.addWidget(self.device_page)
        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setObjectName("setting_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.setting_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.setting_page)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.disconnection = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.disconnection.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/disconnect_button/forbidden.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.disconnection.setIcon(icon)
        self.disconnection.setIconSize(QtCore.QSize(50, 50))
        self.disconnection.setObjectName("disconnection")
        self.horizontalLayout_5.addWidget(self.disconnection)
        self.oscilloscope_settings = QtWidgets.QPushButton(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oscilloscope_settings.sizePolicy().hasHeightForWidth())
        self.oscilloscope_settings.setSizePolicy(sizePolicy)
        self.oscilloscope_settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/osc_button/osc_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.oscilloscope_settings.setIcon(icon1)
        self.oscilloscope_settings.setIconSize(QtCore.QSize(50, 50))
        self.oscilloscope_settings.setObjectName("oscilloscope_settings")
        self.horizontalLayout_5.addWidget(self.oscilloscope_settings)
        self.generator_settings = QtWidgets.QPushButton(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generator_settings.sizePolicy().hasHeightForWidth())
        self.generator_settings.setSizePolicy(sizePolicy)
        self.generator_settings.setMinimumSize(QtCore.QSize(0, 0))
        self.generator_settings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/settings_button/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.generator_settings.setIcon(icon2)
        self.generator_settings.setIconSize(QtCore.QSize(50, 50))
        self.generator_settings.setObjectName("generator_settings")
        self.horizontalLayout_5.addWidget(self.generator_settings)
        self.horizontalLayout_3.addWidget(self.horizontalWidget_2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.oscilloscope_used = QtWidgets.QLineEdit(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oscilloscope_used.sizePolicy().hasHeightForWidth())
        self.oscilloscope_used.setSizePolicy(sizePolicy)
        self.oscilloscope_used.setMinimumSize(QtCore.QSize(400, 0))
        self.oscilloscope_used.setReadOnly(True)
        self.oscilloscope_used.setObjectName("oscilloscope_used")
        self.horizontalLayout.addWidget(self.oscilloscope_used)
        self.verticalLayout_6.addWidget(self.horizontalWidget)
        self.horizontalWidget_21 = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_21.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_21.setSizePolicy(sizePolicy)
        self.horizontalWidget_21.setObjectName("horizontalWidget_21")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.horizontalWidget_21)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.generator_used = QtWidgets.QLineEdit(self.horizontalWidget_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generator_used.sizePolicy().hasHeightForWidth())
        self.generator_used.setSizePolicy(sizePolicy)
        self.generator_used.setMinimumSize(QtCore.QSize(400, 0))
        self.generator_used.setReadOnly(True)
        self.generator_used.setObjectName("generator_used")
        self.horizontalLayout_2.addWidget(self.generator_used)
        self.verticalLayout_6.addWidget(self.horizontalWidget_21)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.measure_input_impedance = QtWidgets.QPushButton(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_input_impedance.sizePolicy().hasHeightForWidth())
        self.measure_input_impedance.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/impedance/omega.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.measure_input_impedance.setIcon(icon3)
        self.measure_input_impedance.setIconSize(QtCore.QSize(50, 50))
        self.measure_input_impedance.setObjectName("measure_input_impedance")
        self.gridLayout_4.addWidget(self.measure_input_impedance, 0, 1, 1, 1)
        self.measure_bode = QtWidgets.QPushButton(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_bode.sizePolicy().hasHeightForWidth())
        self.measure_bode.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/bode/Band-pass_filter_symbol.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.measure_bode.setIcon(icon4)
        self.measure_bode.setIconSize(QtCore.QSize(50, 50))
        self.measure_bode.setObjectName("measure_bode")
        self.gridLayout_4.addWidget(self.measure_bode, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.stackedWidget.addWidget(self.setting_page)
        self.measure_page = QtWidgets.QWidget()
        self.measure_page.setObjectName("measure_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.measure_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget.addWidget(self.measure_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        LabToolWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LabToolWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LabToolWindow)

    def retranslateUi(self, LabToolWindow):
        _translate = QtCore.QCoreApplication.translate
        LabToolWindow.setWindowTitle(_translate("LabToolWindow", "MainWindow"))
        self.label_2.setText(_translate("LabToolWindow", "Device Connection"))
        self.label.setText(_translate("LabToolWindow", "You need to connect both an oscilloscope and a generator via USB, then update or refresh with the button and select for each device those that have been detected. Only supported devices will be detected."))
        self.label_3.setText(_translate("LabToolWindow", "Oscilloscope Device"))
        self.label_4.setText(_translate("LabToolWindow", "Generator Device"))
        self.connection_status.setText(_translate("LabToolWindow", "Remember using the refresh button whenever you want to update the Device\'s lists."))
        self.connection.setText(_translate("LabToolWindow", "Connect"))
        self.label_5.setText(_translate("LabToolWindow", "LabTool Main Menu"))
        self.label_9.setText(_translate("LabToolWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0084ff;\">1. </span><span style=\" color:#00264a;\">Verify you have the correct devices connected.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0081fa;\">2</span><span style=\" color:#0081fa;\">.</span><span style=\" color:#00264a;\"> Use the top right corner buttons to configure the oscilloscope, generator and other preferences.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0084ff;\">3.</span><span style=\" color:#00264a;\"> Select what you want to measure with the bottom buttons.</span></p></body></html>"))
        self.groupBox.setTitle(_translate("LabToolWindow", "Devices Info"))
        self.label_7.setText(_translate("LabToolWindow", "Oscilloscope Device"))
        self.label_8.setText(_translate("LabToolWindow", "Generator Device"))
        self.measure_input_impedance.setText(_translate("LabToolWindow", "Input Impedance"))
        self.measure_bode.setText(_translate("LabToolWindow", "Bode Plot"))

from app.designer.resources import window_resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LabToolWindow = QtWidgets.QMainWindow()
    ui = Ui_LabToolWindow()
    ui.setupUi(LabToolWindow)
    LabToolWindow.show()
    sys.exit(app.exec_())
