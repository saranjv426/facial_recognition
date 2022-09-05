

from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import re,os
import sys
from random import randint
class Ui_PersonDetails(object):


    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Photo")
        print(fileName)
        self.lineEdit.setText(fileName)

    def addinfo(self):
        try:
            photo = self.lineEdit.text()
            pathh, filename = os.path.split(photo)
            name = self.lineEdit_2.text()
            age = self.lineEdit_3.text()
            gender = self.lineEdit_5.text()
            adrs = self.lineEdit_6.text()
            if name == "" or name == "null" or photo == "" or photo == "null" or age == "" or age == "null"  or gender == "" or gender == "null" or adrs == "" or adrs == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sno= str(name) +"_"+str(randint(1000, 9999))
                imgid = str(name) + ".jpg"

                path = "../FaceMaskDetector/photos/" + sno + "/"
                if not os.path.exists(os.path.dirname(path)):
                    try:
                        os.makedirs(os.path.dirname(path))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                database = DBConnection.getConnection()
                cursor = database.cursor()
                query = "insert into personinfo values(%s,%s,%s,%s,%s,%s)"
                values = (sno, name,age,gender,adrs,imgid)
                cursor.execute(query, values)
                database.commit()
                imgdata = self.read_file(photo)
                self.write_file(imgdata, imgid, path)
                self.showMessageBox("Information", "Person Details added Successfully..!")

                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def write_file(self, data, imgid, path):
        with open(path + imgid, 'wb') as f:
            f.write(data)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 587)
        Dialog.setStyleSheet("background-color: rgb(154, 138, 47);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 40, 271, 91))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 420, 191, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 420, 271, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 420, 121, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 135, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 490, 131, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.addinfo)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 191, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 271, 41))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 210, 181, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 210, 271, 41))
        self.lineEdit_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 280, 161, 41))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 280, 271, 41))
        self.lineEdit_5.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 350, 161, 41))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 350, 271, 41))
        self.lineEdit_6.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Person Details"))
        self.label.setText(_translate("Dialog", "Person Details"))
        self.label_2.setText(_translate("Dialog", "Photo"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_2.setText(_translate("Dialog", "Submit"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Age"))
        self.label_6.setText(_translate("Dialog", "Gender"))
        self.label_7.setText(_translate("Dialog", "Address"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_PersonDetails()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
