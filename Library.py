class Library:
    def __init__(self, filename='books.txt'):
        self.file = open(filename, 'a+')# Ekleme ve okuma modunda. Dosya mevcut değilse otomatik olarak oluşacak.

    def liste_kitap(self):
        #kitap listelenecek kitap ismi yazari sayfa sayisi ? baska ne olabilir.
        return null

    def ekle_kitap(self):
        # kitap icin ne kadar bilgi tutulacaksa o kadar kullanicidan input iste
        # kitap ismi ve yazari kesinlikle olmali
        # diger degerleri bos birakabilir mi kullanici?
        return null

    def sil_kitap(self):
        # kitap ismini sor ve direkt o kitaba ait butun bilgileri sil
        # kitap ismi unique degilse 2. degiskeni sor (yazari)
        # mevcut butun kitaplari sildigimizde books.txt'ye bir yazi belki...
        return null
    

    #basit bir GUI yapilabilir mi.


if __name__ == "__main__":
    lib = Library()  # Library Sınıfından lib nesnesi tanımlandı.

    while True:
        print("*** MENU ***")
        print("1) Kitapları listele")
        print("2) Kitap Ekleme")
        print("3) Kitap Silme")
        #ekstra fonksiyon gelebilir mi?
        print("q) Çıkış")
        kullaniciInput = input()

        if kullaniciInput == 'q':
            break
        elif kullaniciInput == '1':
            lib.liste_kitap()
        elif kullaniciInput == '2':
            lib.ekle_kitap()
        elif kullaniciInput == '3':
            lib.sil_kitap()
        else:
            print("Yanlış girdiniz.")
