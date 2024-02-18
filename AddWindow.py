# Bu dosya, kitap ekleme penceresi icin tasarlanmis olan arayuz kodlarini icerir.
import os
from FileManager import FileManager # Dosya islemleri icin FileManager sinifini import ettik.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    FileManager = FileManager() # Dosya islemi yapacagimiz icin FileManager nesnesi olusturuldu.
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(415, 247)

        Form.setWindowTitle("Book Addition Screen") # Pencere basligi
        Form.setWindowIcon(QtGui.QIcon("./icons/globalaihub.jpeg")) # Pencere iconu eklendi
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 16))

        font = QtGui.QFont() # Font ayarlamasi yapildi. hepsi icin ayni font kullanildi.
        font.setPointSize(12)

        self.label.setFont(font)
        self.label.setText("Title") # Kitap ismi icin yazi
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.label_2.setFont(font)
        self.label_2.setText("Author") # Yazar ismi icin yazi
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.label_3.setFont(font)
        self.label_3.setText("Release year") # Yayin yili icin yazi 
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.label_4.setFont(font)
        self.label_4.setText("Page") # Sayfa sayisi icin yazi
        
        self.TitleEdit = QtWidgets.QLineEdit(Form) # Kitap ismi icin input alanı
        self.TitleEdit.setGeometry(QtCore.QRect(160, 30, 221, 31))
        self.TitleEdit.setFont(font)
        
        self.AuthorEdit = QtWidgets.QLineEdit(Form) # yazar ismi icin input alanı
        self.AuthorEdit.setGeometry(QtCore.QRect(160, 70, 221, 31))
        self.AuthorEdit.setFont(font)
        
        self.YearEdit = QtWidgets.QLineEdit(Form) # yayin yili icin input alanı
        self.YearEdit.setGeometry(QtCore.QRect(160, 110, 221, 31))
        self.YearEdit.setFont(font)
        
        self.PageEdit = QtWidgets.QLineEdit(Form) # sayfa sayisi icin input alanı
        self.PageEdit.setGeometry(QtCore.QRect(160, 150, 221, 31))
        self.PageEdit.setFont(font)
        
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.AddButton.setFont(font)
        self.AddButton.setText("Add") # Add butonu etiketi eklendi

        self.AddButton.clicked.connect(lambda:self.AddButtonFunction(Form)) # Ekleme butonuna tıklanınca Ekleme fonksiyonu cagiriliyor.

    def AddButtonFunction(self,Form): # Eklemeler burada gerceklesiyor
        self.FileManager.append_to_file( f"{self.TitleEdit.text()},{self.AuthorEdit.text()},{self.YearEdit.text()},{self.PageEdit.text()}\n") # Dosya islemi icin append_to_file fonksiyonu cagirdik.
        Form.hide()

