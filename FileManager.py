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