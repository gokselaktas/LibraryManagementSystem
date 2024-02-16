class Library:
    def __init__(self, filename='books.txt'):
        self.file = open(filename, 'a+')# Ekleme ve okuma modunda. Dosya mevcut değilse otomatik olarak oluşacak.

    def liste_kitap(self):
        #kitap listelenecek kitap ismi yazari sayfa sayisi ? baska ne olabilir.
        # Go to the start of the file
        self.file.seek(0)
        # Read all lines and split them into a list
        lines = self.file.read().splitlines()
        # Print book names and authors
        for line in lines:
            book_info = line.split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def ekle_kitap(self):
        # kitap icin ne kadar bilgi tutulacaksa o kadar kullanicidan input iste
        # kitap ismi ve yazari kesinlikle olmali
        # diger degerleri bos birakabilir mi kullanici?
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        pages = input("Enter number of pages: ")
        book_str = f"{title},{author},{pages}\n"
        #String olusturduk
        self.file.write(book_str)
        self.file.flush()

    def sil_kitap(self):
        # kitap ismini sor ve direkt o kitaba ait butun bilgileri sil
        # kitap ismi unique degilse 2. degiskeni sor (yazari)
        # mevcut butun kitaplari sildigimizde books.txt'ye bir yazi belki...
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        # kitabi bul
        lines = [line for line in lines if not line.startswith(title_to_remove)]
        # Clear the file and rewrite the list
        self.file.seek(0)
        self.file.truncate()
        for line in lines:
            self.file.write(f"{line}\n")
        self.file.flush()
    

    #basit bir GUI yapilabilir mi.


if __name__ == "__main__":
    lib = Library()  # Library Sınıfından lib nesnesi tanımlandı.

while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        #ekstra fonksiyon gelebilir mi?
        print("q) Exit")
        choice = input()

        if choice == 'q':
            break
        elif choice == '1':
            lib.liste_kitap()
        elif choice == '2':
            lib.ekle_kitap()
        elif choice == '3':
            lib.sil_kitap()
        else:
            print("Invalid choice.")
