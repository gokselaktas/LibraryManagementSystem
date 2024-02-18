# Bu dosya, kitap silme penceresi icin tasarlanmis olan arayuz kodlarini icerir.
from FileManager import FileManager # Dosya islemleri icin FileManager sinifini import ettik.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    FileManager = FileManager() # Dosya islemi yapacagimiz icin FileManager nesnesi olusturuldu.
    def setupUi(self, Form):
        Form.resize(339, 119)
        Form.setWindowTitle("Book Deletion Screen") # Pencere basligi
        Form.setWindowIcon(QtGui.QIcon('./icons/globalaihub.jpeg')) # GlobalAIHub logosu eklendi

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 16))

        font = QtGui.QFont() # Font ayarlamasi yapildi.
        font.setPointSize(12) 

        self.label.setFont(font)
        self.label.setText("Title")  #Silme ekranindaki Title yazisi
        
        self.DelEdit = QtWidgets.QLineEdit(Form)
        self.DelEdit.setGeometry(QtCore.QRect(100, 30, 221, 31))

        self.DelButton = QtWidgets.QPushButton(Form)
        self.DelButton.setGeometry(QtCore.QRect(230, 70, 93, 28))
        self.DelButton.setFont(font)
        self.DelButton.setText("Delete")

        self.DelButton.clicked.connect(lambda:self.DelButtonFunction(Form))# delete butonuna tıklanınca silme fonksiyonu cagiriliyor.

    def DelButtonFunction(self,Form):# delete butonuna tıklanınca sayfayı saklar.
        self.FileManager.delete_book(self.DelEdit.text())
        Form.hide()



