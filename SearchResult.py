from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import sys
class Ui_SearchResults(object):

    def view(self,sno):

        try:

            database = DBConnection.getConnection()
            cursor = database.cursor()


            sql2 = "select *from personinfo where sno='" + sno+ "' "
            cursor.execute(sql2)
            res = cursor.fetchall()

            for row in res:
                name = row[1]
                age = row[2]
                gen = row[3]
                adrs = row[4]
                photo = row[5]


                self.name.setText(name)
                self.age.setText(age)
                self.gender.setText(gen)
                self.adrs.setText(adrs)

                self.camera.setStyleSheet("image: url(../FaceMaskDetector/testimg/testingimg.jpg);")
                self.camera_2.setStyleSheet("image: url(../FaceMaskDetector/photos/"+str(sno)+"/"+str(photo)+");")


        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)







    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 584)
        Dialog.setStyleSheet("background-color: rgb(136, 45, 68);")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(70, 90, 161, 131))
        self.camera.setStyleSheet("image: url(:/image/MissingChild/user.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 181, 41))
        self.label_5.setStyleSheet("font: 11pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.camera_2 = QtWidgets.QLabel(Dialog)
        self.camera_2.setGeometry(QtCore.QRect(370, 90, 171, 131))
        self.camera_2.setStyleSheet("image: url(:/image/MissingChild/question-mark-face.jpg);")
        self.camera_2.setText("")
        self.camera_2.setObjectName("camera_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 40, 181, 41))
        self.label_6.setStyleSheet("color: rgb(85, 170, 0);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 250, 141, 41))
        self.label.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 290, 141, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 340, 141, 41))
        self.label_3.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 390, 141, 41))
        self.label_4.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(480, 240, 141, 51))
        self.name.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.name.setText("")
        self.name.setObjectName("name")
        self.age = QtWidgets.QLabel(Dialog)
        self.age.setGeometry(QtCore.QRect(480, 290, 131, 41))
        self.age.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.age.setText("")
        self.age.setObjectName("age")

        self.gender = QtWidgets.QLabel(Dialog)
        self.gender.setGeometry(QtCore.QRect(480, 340, 251, 41))
        self.gender.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.gender.setText("")
        self.gender.setObjectName("gender")

        self.adrs = QtWidgets.QLabel(Dialog)
        self.adrs.setGeometry(QtCore.QRect(480, 390, 251, 41))
        self.adrs.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.adrs.setText("")
        self.adrs.setObjectName("adrs")


        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(310, 450, 141, 41))
        self.label_11.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")


        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(310, 500, 141, 41))
        self.label_13.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search Results"))
        self.label_5.setText(_translate("Dialog", "Searching Photo"))
        self.label_6.setText(_translate("Dialog", "Matching Found"))
        self.label.setText(_translate("Dialog", "Name      :"))
        self.label_2.setText(_translate("Dialog", "Age          :"))
        self.label_3.setText(_translate("Dialog", "Gender      :"))
        self.label_4.setText(_translate("Dialog", "Address     :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
