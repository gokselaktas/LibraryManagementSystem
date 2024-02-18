import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from FileManager import FileManager # Dosya islemleri icin FileManager sinifini import ettik.

class Ui_MainWindow(object):
    FileManager = FileManager() # Dosya islemi yapacagimiz icin FileManager nesnesi olusturuldu.
    def setupUi(self, MainWindow):
        MainWindow.resize(641, 687)
        MainWindow.setWindowTitle("Library Management System") # Pencere basligi
        MainWindow.setWindowIcon(QtGui.QIcon('./icons/globalaihub.jpeg')) # GlobalAIHub logosu eklendi

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GlobalAiButton = QtWidgets.QPushButton(self.centralwidget)
        self.GlobalAiButton.setGeometry(QtCore.QRect(30, 30, 121, 131)) 
        self.GlobalAiButton.setIcon(QtGui.QIcon("./icons/globalaihub.jpeg")) # GlobalAIHub logosu eklendi
        self.GlobalAiButton.setIconSize(QtCore.QSize(121, 131)) # icon boyutu ayarlamasi
        self.GlobalAiButton.clicked.connect(lambda: os.system("start https://globalaihub.com/"))# GlobalAIHub logosuna tıklanınca siteye yönlendirme yapiyor.
        # sertifika aldigimda oraya yonlendirecegim :)

        self.ListPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ListPushButton.setGeometry(QtCore.QRect(30, 180, 121, 131))
        self.ListPushButton.setIcon(QtGui.QIcon('./icons/list.png')) # Listeleme logosu eklendi
        self.ListPushButton.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.AddPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddPushButton.setGeometry(QtCore.QRect(30, 330, 121, 131))
        self.AddPushButton.setIcon(QtGui.QIcon('./icons/add.png')) # Ekleme logosu eklendi
        self.AddPushButton.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.DelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.DelPushButton.setGeometry(QtCore.QRect(30, 480, 121, 131))
        self.DelPushButton.setIcon(QtGui.QIcon('./icons/delete.png')) #Silme logosu eklendi
        self.DelPushButton.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(225, 31, 391, 541))

        self.ExitPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitPushButton.setGeometry(QtCore.QRect(520, 590, 93, 28))
        self.ExitPushButton.setText("Exit") # Exit butonu eklendi

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ListPushButton.clicked.connect(self.load_books_into_listview)
        self.AddPushButton.clicked.connect(self.AddWindow) # Ekleme ekrani cagiriliyor
        self.DelPushButton.clicked.connect(self.DelWindow) # Silme ekrani cagiriliyor
        self.ExitPushButton.clicked.connect(lambda:self.ExitFunction())# exit butonuna tıklanınca

    def load_books_into_listview(self):
        books = self.FileManager.read_books_from_file()  # Dosyadan kitapları okuyan fonksiyon
        # Model tabanli bir widget kullandigimiz icin bir model olusturuyoruz
        model = QStandardItemModel(self.listView)
        for book in books:
            # Her bir kitap için bir QStandardItem oluşturduk ve modelimize ekledik
            item = QStandardItem(book)
            model.appendRow(item)
        # Modeli ListView'a bağladık
        self.listView.setModel(model)

    def ExitFunction(self):# exit butonuna tıklanınca her şeyi kapatır.
        sys.exit()

    def AddWindow(self):# kitap eklemek için çıkacak ekran
        from AddWindow import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def DelWindow(self): # kitap silmek için çıkacak ekran	
        from DelWindow import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__": # ekranı çalıştırır
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
