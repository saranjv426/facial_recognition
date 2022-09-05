from PyQt5 import QtCore, QtGui, QtWidgets
from AdminHome import Ui_Admin


class Ui_Main(object):
    def showMessageBox(self, title, message):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle(title)
            msgBox.setText(message)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
    def admin(self):
        uid = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if uid == "" or uid =="null" or pwd=="" or pwd == "null":
            self.showMessageBox("Error","Please enter required fields")
        elif uid=="admin" and pwd=="admin":
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Admin()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        else:
            self.showMessageBox("failed","Wrong Credentials")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        Dialog.setStyleSheet("QDialog{background-image: url(../FaceMaskDetector/ui_img/adm.jpg);}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(370, 210, 321, 401))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 125, 190, 43), stop:1 rgba(255, 255, 255, 255));}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(221, 252, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 230, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(179, 84, 95);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 971, 111))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.admin)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Real Time Face Mask Detection\n"
"and Face Recognition System"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
