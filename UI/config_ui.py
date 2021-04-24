# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/config.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.setWindowModality(QtCore.Qt.ApplicationModal)
        Config.resize(660, 290)
        font = QtGui.QFont()
        font.setPointSize(16)
        Config.setFont(font)
        Config.setToolTip("")
        Config.setStyleSheet("")
        self.save_pushButton = QtWidgets.QPushButton(Config)
        self.save_pushButton.setGeometry(QtCore.QRect(20, 250, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_pushButton.setFont(font)
        self.save_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_pushButton.setObjectName("save_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(Config)
        self.cancel_pushButton.setGeometry(QtCore.QRect(590, 250, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_pushButton.setFont(font)
        self.cancel_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.general_groupBox = QtWidgets.QGroupBox(Config)
        self.general_groupBox.setGeometry(QtCore.QRect(10, 20, 641, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.general_groupBox.setFont(font)
        self.general_groupBox.setObjectName("general_groupBox")
        self.download_path_label = QtWidgets.QLabel(self.general_groupBox)
        self.download_path_label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.download_path_label.setFont(font)
        self.download_path_label.setObjectName("download_path_label")
        self.download_path_lineEdit = QtWidgets.QLineEdit(self.general_groupBox)
        self.download_path_lineEdit.setGeometry(QtCore.QRect(100, 20, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.download_path_lineEdit.setFont(font)
        self.download_path_lineEdit.setObjectName("download_path_lineEdit")
        self.browse_pushButton = QtWidgets.QPushButton(self.general_groupBox)
        self.browse_pushButton.setGeometry(QtCore.QRect(580, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.browse_pushButton.setFont(font)
        self.browse_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_pushButton.setStyleSheet("")
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.status_bar_checkBox = QtWidgets.QCheckBox(self.general_groupBox)
        self.status_bar_checkBox.setGeometry(QtCore.QRect(20, 60, 211, 16))
        self.status_bar_checkBox.setChecked(True)
        self.status_bar_checkBox.setObjectName("status_bar_checkBox")
        self.chekc_update_checkBox = QtWidgets.QCheckBox(self.general_groupBox)
        self.chekc_update_checkBox.setGeometry(QtCore.QRect(20, 90, 211, 16))
        self.chekc_update_checkBox.setChecked(True)
        self.chekc_update_checkBox.setObjectName("chekc_update_checkBox")
        self.download_groupBox = QtWidgets.QGroupBox(Config)
        self.download_groupBox.setGeometry(QtCore.QRect(10, 150, 641, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.download_groupBox.setFont(font)
        self.download_groupBox.setObjectName("download_groupBox")
        self.slow_radioButton = QtWidgets.QRadioButton(self.download_groupBox)
        self.slow_radioButton.setEnabled(True)
        self.slow_radioButton.setGeometry(QtCore.QRect(20, 30, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.slow_radioButton.setFont(font)
        self.slow_radioButton.setChecked(True)
        self.slow_radioButton.setObjectName("slow_radioButton")
        self.genera_radioButton = QtWidgets.QRadioButton(self.download_groupBox)
        self.genera_radioButton.setGeometry(QtCore.QRect(110, 30, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.genera_radioButton.setFont(font)
        self.genera_radioButton.setObjectName("genera_radioButton")
        self.high_radioButton = QtWidgets.QRadioButton(self.download_groupBox)
        self.high_radioButton.setGeometry(QtCore.QRect(200, 30, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.high_radioButton.setFont(font)
        self.high_radioButton.setObjectName("high_radioButton")
        self.starburst_radioButton = QtWidgets.QRadioButton(self.download_groupBox)
        self.starburst_radioButton.setGeometry(QtCore.QRect(290, 30, 83, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.starburst_radioButton.setFont(font)
        self.starburst_radioButton.setObjectName("starburst_radioButton")
        self.simultaneous_download_label = QtWidgets.QLabel(self.download_groupBox)
        self.simultaneous_download_label.setGeometry(QtCore.QRect(460, 27, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.simultaneous_download_label.setFont(font)
        self.simultaneous_download_label.setObjectName("simultaneous_download_label")
        self.simultaneous_download_lineEdit = QtWidgets.QLineEdit(self.download_groupBox)
        self.simultaneous_download_lineEdit.setGeometry(QtCore.QRect(580, 28, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.simultaneous_download_lineEdit.setFont(font)
        self.simultaneous_download_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.simultaneous_download_lineEdit.setObjectName("simultaneous_download_lineEdit")
        self.note_pushButton = QtWidgets.QPushButton(self.download_groupBox)
        self.note_pushButton.setGeometry(QtCore.QRect(550, 50, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.note_pushButton.setFont(font)
        self.note_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.note_pushButton.setStyleSheet("QPushButton{\n"
                                           "background: transparent;\n"
                                           "border-radius:6px;\n"
                                           "color: #0055ff;\n"
                                           "text-decoration: underline;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "background: transparent;\n"
                                           "      color: #0055ff;\n"
                                           "      }\n"
                                           "      QPushButton:pressed{\n"
                                           "      background: transparent;\n"
                                           "      color: #0055ff;\n"
                                           "      }\n"
                                           "     ")
        self.note_pushButton.setObjectName("note_pushButton")
        self.re_download_Checkbox = QtWidgets.QCheckBox(self.download_groupBox)
        self.re_download_Checkbox.setGeometry(QtCore.QRect(20, 60, 281, 16))
        self.re_download_Checkbox.setChecked(True)
        self.re_download_Checkbox.setTristate(False)
        self.re_download_Checkbox.setObjectName("re_download_Checkbox")
        self.re_download_lineEdit = QtWidgets.QLineEdit(self.download_groupBox)
        self.re_download_lineEdit.setGeometry(QtCore.QRect(300, 58, 61, 20))
        self.re_download_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.re_download_lineEdit.setObjectName("re_download_lineEdit")
        self.label = QtWidgets.QLabel(self.download_groupBox)
        self.label.setGeometry(QtCore.QRect(360, 60, 47, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)
        Config.setTabOrder(self.download_path_lineEdit, self.browse_pushButton)
        Config.setTabOrder(self.browse_pushButton, self.status_bar_checkBox)
        Config.setTabOrder(self.status_bar_checkBox, self.chekc_update_checkBox)
        Config.setTabOrder(self.chekc_update_checkBox, self.slow_radioButton)
        Config.setTabOrder(self.slow_radioButton, self.genera_radioButton)
        Config.setTabOrder(self.genera_radioButton, self.high_radioButton)
        Config.setTabOrder(self.high_radioButton, self.starburst_radioButton)
        Config.setTabOrder(self.starburst_radioButton, self.simultaneous_download_lineEdit)
        Config.setTabOrder(self.simultaneous_download_lineEdit, self.note_pushButton)
        Config.setTabOrder(self.note_pushButton, self.re_download_Checkbox)
        Config.setTabOrder(self.re_download_Checkbox, self.re_download_lineEdit)
        Config.setTabOrder(self.re_download_lineEdit, self.save_pushButton)
        Config.setTabOrder(self.save_pushButton, self.cancel_pushButton)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "設定"))
        self.save_pushButton.setToolTip(_translate("Config", "儲存"))
        self.save_pushButton.setText(_translate("Config", "儲存"))
        self.cancel_pushButton.setToolTip(_translate("Config", "取消"))
        self.cancel_pushButton.setText(_translate("Config", "取消"))
        self.general_groupBox.setToolTip(_translate("Config", "一般選項"))
        self.general_groupBox.setTitle(_translate("Config", "一般選項"))
        self.download_path_label.setToolTip(_translate("Config", "下載路徑"))
        self.download_path_label.setText(_translate("Config", "下載路徑:"))
        self.download_path_lineEdit.setToolTip(_translate("Config", "下載位置"))
        self.browse_pushButton.setToolTip(_translate("Config", "瀏覽"))
        self.browse_pushButton.setText(_translate("Config", "瀏覽"))
        self.status_bar_checkBox.setText(_translate("Config", "最下化到狀態列"))
        self.chekc_update_checkBox.setText(_translate("Config", "檢查更新"))
        self.download_groupBox.setToolTip(_translate("Config", "下載選項"))
        self.download_groupBox.setTitle(_translate("Config", "下載選項"))
        self.slow_radioButton.setText(_translate("Config", "慢速"))
        self.genera_radioButton.setToolTip(_translate("Config", "1次3個連接"))
        self.genera_radioButton.setText(_translate("Config", "一般"))
        self.high_radioButton.setToolTip(_translate("Config", "1次6個連接"))
        self.high_radioButton.setText(_translate("Config", "高速"))
        self.starburst_radioButton.setToolTip(_translate("Config", "1次10個連接"))
        self.starburst_radioButton.setText(_translate("Config", "星爆"))
        self.simultaneous_download_label.setToolTip(_translate("Config", "同時下載的數量"))
        self.simultaneous_download_label.setText(_translate("Config", "同時下載的數量:"))
        self.simultaneous_download_lineEdit.setToolTip(_translate("Config", "輸入數字"))
        self.simultaneous_download_lineEdit.setText(_translate("Config", "5"))
        self.note_pushButton.setToolTip(_translate("Config", "重要事項"))
        self.note_pushButton.setText(_translate("Config", "注意事項"))
        self.re_download_Checkbox.setText(_translate("Config", "如有下載失敗，重新嘗試下載每隔"))
        self.re_download_lineEdit.setText(_translate("Config", "2"))
        self.label.setText(_translate("Config", "分"))
