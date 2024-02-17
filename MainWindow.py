from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class FileManager:
    def __init__(self, filename='books.txt'):
        self.filename = filename

    def append_to_file(self, content):
        with open(self.filename, 'a+') as file:
            file.write(content)

    def read_books_from_file(self):
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
    #FileManager.append_to_file("GlobalAI, Python, 2021, 300")


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 687)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 121, 131))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 180, 121, 131))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 330, 121, 131))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 480, 121, 131))
        self.pushButton_4.setObjectName("pushButton_4")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(225, 31, 391, 541))
        self.listView.setObjectName("listView")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 590, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.load_books_into_listview)
        self.pushButton_3.clicked.connect(self.AddWindow)# add window fonksiyonu eklenecek
        self.pushButton_4.clicked.connect(self.DelWindow)# del window fonksiyonu eklenecek
        self.pushButton_5.clicked.connect(lambda:self.closeScreen())# exit butonuna tıklanınca

    def load_books_into_listview(self):
        # Dosyadan kitapları okuyun
        books = self.FileManager.read_books_from_file()  # Dosyadan kitapları okuyan fonksiyon
        
        # Model tabanli bir widget kullandigimiz icin bir model olusturuyoruz
        model = QStandardItemModel(self.listView)
        
        for book in books:
            # Her bir kitap için bir QStandardItem oluşturduk ve modelimize ekledik
            item = QStandardItem(book)
            model.appendRow(item)
        
        # Modeli ListView'a bağladık
        self.listView.setModel(model)
        

        

    def closeScreen(self):# exit butonuna tıklanınca her şeyi kapatır.
        sys.exit()

    def AddWindow(self):# kitap eklemek için çıkacak ekran
        from AddWindow import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        print("")

    def DelWindow(self): # kitap silmek için çıkacak ekran	
        from DelWindow import Ui_Form
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management System"))
        self.pushButton.setText(_translate("MainWindow", "GlobalAI LOGO"))
        self.pushButton_2.setText(_translate("MainWindow", "List Books"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Book"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete Book"))
        self.pushButton_5.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
