


from PyQt5 import QtCore, QtGui, QtWidgets
from BuildFaceMaskModel import build
from Prediction import Ui_Prediction
from facemask_detection import mask_detection
from FaceRecognition import Ui_Recognition
from BuildFaceRecogModel import train
from AddPersonDetails import Ui_PersonDetails
class Ui_Admin(object):

    def add_personInfo(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_PersonDetails()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def buildmodel_facemask(self):
         build()
         self.showMessageBox("Successfull", "FaceMask Detection model created successfull")


    def buildmodel_FaceRecog(self):
        train("../FaceMaskDetector/photos", model_save_path="trained_knn_model.clf", n_neighbors=1)
        self.showMessageBox("Successfull","FaceRecognition model created successfull")


    def face_mask_detection(self):
        mask_detection()

    def face_recogniton(self):

        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Recognition()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()



    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        Dialog.setStyleSheet("QDialog{background-image: url(../FaceMaskDetector/ui_img/nxt.jpg);}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 175, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 171, 182);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 260, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 171, 182);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 350, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 171, 182);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 440, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 171, 182);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 540, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 171, 182);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 581, 101))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(194, 194, 194, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.add_personInfo)
        self.pushButton_2.clicked.connect(self.buildmodel_facemask)
        self.pushButton_3.clicked.connect(self.buildmodel_FaceRecog)
        self.pushButton_4.clicked.connect(self.face_mask_detection)
        self.pushButton_5.clicked.connect(self.face_recogniton)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AdminHome"))
        self.pushButton.setText(_translate("Dialog", "Add Person Details"))
        self.pushButton_2.setText(_translate("Dialog", "Build FaceMask DetectionModel"))
        self.pushButton_3.setText(_translate("Dialog", "Build FaceRecognition Model"))
        self.pushButton_4.setText(_translate("Dialog", "Face Mask Detection"))
        self.pushButton_5.setText(_translate("Dialog", "FaceRecognition System"))
        self.label.setText(_translate("Dialog", "Real Time Face Mask Detection\n"
"and Face Recognition System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
