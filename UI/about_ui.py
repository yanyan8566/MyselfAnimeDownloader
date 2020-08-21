# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.ApplicationModal)
        About.resize(400, 275)
        self.image_label = QtWidgets.QLabel(About)
        self.image_label.setGeometry(QtCore.QRect(30, 0, 128, 128))
        self.image_label.setStyleSheet("")
        self.image_label.setObjectName("image_label")
        self.github_label = QtWidgets.QLabel(About)
        self.github_label.setGeometry(QtCore.QRect(230, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.github_label.setFont(font)
        self.github_label.setAlignment(QtCore.Qt.AlignCenter)
        self.github_label.setOpenExternalLinks(True)
        self.github_label.setObjectName("github_label")
        self.dudulu_label = QtWidgets.QLabel(About)
        self.dudulu_label.setGeometry(QtCore.QRect(200, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dudulu_label.setFont(font)
        self.dudulu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dudulu_label.setObjectName("dudulu_label")
        self.note_label = QtWidgets.QLabel(About)
        self.note_label.setGeometry(QtCore.QRect(10, 130, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.note_label.setFont(font)
        self.note_label.setObjectName("note_label")
        self.close_pushButton = QtWidgets.QPushButton(About)
        self.close_pushButton.setGeometry(QtCore.QRect(320, 240, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close_pushButton.setFont(font)
        self.close_pushButton.setStyleSheet("")
        self.close_pushButton.setObjectName("close_pushButton")
        self.Myself_label = QtWidgets.QLabel(About)
        self.Myself_label.setGeometry(QtCore.QRect(210, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Myself_label.setFont(font)
        self.Myself_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Myself_label.setOpenExternalLinks(True)
        self.Myself_label.setObjectName("Myself_label")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "關於"))
        self.image_label.setText(_translate("About", "image_label"))
        self.github_label.setText(
            _translate("About", "<a href=\"https://github.com/hgalytoby/MyselfAnimeDownloader\">Github</a>"))
        self.dudulu_label.setText(_translate("About", "組件與設計者：嘟嘟嚕"))
        self.note_label.setText(_translate("About", "感謝您使用非MyselfAnume官方下載應用程式。\n"
                                                    "\n"
                                                    " 請支持正版！\n"
                                                    "「下載的影片僅供交流使用，請於24小時內刪除。」\n"
                                                    "若私作為其他及商業用途而觸犯法律違法。\n"
                                                    "後果請自行負責，概與本人無關。"))
        self.close_pushButton.setText(_translate("About", "關閉"))
        self.Myself_label.setText(_translate("About", "<a href=\"https://myself-bbs.com/portal.php\">Myself 官網</a>"))
