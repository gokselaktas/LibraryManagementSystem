import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class FileManager: # Dosya islemleri icin FileManager sinifi olusturuldu
    def __init__(self, filename='books.txt'): # Dosya adı belirtilmezse varsayılan olarak books.txt dosyası oluşturacak
        self.filename = filename

    def append_to_file(self, content): # Dosyaya kitap ekleyen fonksiyon
        with open(self.filename, 'a+') as file:
            file.write(content)

    def read_books_from_file(self): # Dosyadan kitapları okuyan fonksiyon
        with open(self.filename, 'r') as file:
            lines = file.read().splitlines()
        return lines
        
    def delete_book(self, title_to_remove):
        # Dosyayı okuma modunda açıp içeriğini okuyoruz.
        with open(self.filename, 'r') as file:
            lines = file.read().splitlines()

        # Başlığı verilen kitabı çıkartıyoruz.
        lines = [line for line in lines if not line.startswith(title_to_remove)]

        # Dosyayı yazma modunda açıp güncellenmiş içeriği yazıyoruz.
        with open(self.filename, 'w') as file:
            for line in lines:
                file.write(f"{line}\n")


class Ui_MainWindow(object):
    FileManager = FileManager()

    def setupUi(self, MainWindow):
        MainWindow.resize(641, 687)
        MainWindow.setWindowTitle("Library Management System") # Pencere basligi
        MainWindow.setWindowIcon(QtGui.QIcon('./icons/globalaihub.jpeg')) # GlobalAIHub logosu eklendi

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 121, 131))
        self.pushButton.setIcon(QtGui.QIcon("./icons/globalaihub.jpeg")) # GlobalAIHub logosu eklendi
        self.pushButton.setIconSize(QtCore.QSize(121, 131)) # icon boyutu ayarlamasi
        self.pushButton.clicked.connect(lambda: os.system("start https://globalaihub.com/"))# GlobalAIHub logosuna tıklanınca siteye yönlendirme yapiyor.
        # sertifika aldigimda oraya yonlendirecegim :)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 180, 121, 131))
        self.pushButton_2.setIcon(QtGui.QIcon('./icons/list.png')) # Listeleme logosu eklendi
        self.pushButton_2.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 330, 121, 131))
        self.pushButton_3.setIcon(QtGui.QIcon('./icons/add.png')) # Ekleme logosu eklendi
        self.pushButton_3.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 480, 121, 131))
        self.pushButton_4.setIcon(QtGui.QIcon('./icons/delete.png')) #Silme logosu eklendi
        self.pushButton_4.setIconSize(QtCore.QSize(121, 131)) #icon boyutu ayarlamasi

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(225, 31, 391, 541))

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 590, 93, 28))
        self.pushButton_5.setText("Exit") # Exit butonu eklendi

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.load_books_into_listview)
        self.pushButton_3.clicked.connect(self.AddWindow) # Ekleme ekrani cagiriliyor
        self.pushButton_4.clicked.connect(self.DelWindow) # Silme ekrani cagiriliyor
        self.pushButton_5.clicked.connect(lambda:self.ExitFunction())# exit butonuna tıklanınca

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
