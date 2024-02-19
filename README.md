
# Library Management System - Akbank Python Bootcamp Project

This repository contains the Library Management System project developed for the Global AI Hub's Python Bootcamp in collaboration with Akbank. The project demonstrates the application of object-oriented programming principles in Python to manage a collection of books.

## Project Overview
![libsystem](https://github.com/gokselaktas/LibraryManagementSystem/assets/33264492/cd9d3953-a028-4e0b-a024-7517b368c7d9)

The Library Management System is designed to interface with a text file books.txt, which acts as a database for storing book details. Each line in this file represents a single book entry with attributes including the book name, author, release date, and the number of pages, all separated by commas.

The system is encapsulated in a Library class, which provides the following functionalities:

Initialization and Termination: The constructor initializes the system by opening the books.txt file, and the destructor ensures proper closure of the file.

 - Listing Books: A method to read and display all book entries from the books.txt file.

 - Adding a Book: A method to add a new book entry to the file,    capturing user input for the book's details.

 - Removing a Book: A method to delete a book entry from the file based on a given title.

## User Interaction

The system provides a user-friendly graphical interface (GUI) to interact with the library database, which utilizes the `books.txt` file. Through the GUI, users can effortlessly:

- View a list of all books currently stored in the `books.txt` file.
- Add a new book entry, inputting details such as the title, author, release date, and number of pages.
- Remove an existing book by specifying its title.

This intuitive GUI streamlines the process of managing the book database, making it accessible for users without the need to interact with a text-based terminal.


## Technical Implementation

The project is implemented in Python and extends its functionality with a simple GUI design, created using PyQt5 to enhance user experience beyond the terminal-based interaction. This graphical interface provides a more intuitive and user-friendly way to interact with the library system, allowing for operations such as listing, adding, and removing books through a visual medium. The backend of the system showcases proficient use of file handling, string manipulation, and control structures such as if-elif-else statements for executing commands via both the terminal menu and the GUI. The code is structured to be clean and readable, with a modular design that supports easy maintenance and future enhancements.



## Getting Started

### To run the Library Management System:

Clone this repository to your local machine.

To start the program, first ensure that `Python` and `PyQt5` are installed on your computer.

Run the `MainWindow.py` script. 


## Function descriptions

The project includes four distinct classes. The first, `Mainwindow.py`, is the file we need to open to start the program. When the `Add` button is clicked, it invokes the class found in `AddWindow.py`, which brings up the corresponding screen. Similarly, clicking the `Delete` button brings up `DelWindow.py`. In addition to these, there is a class in `FileManager.py` that is designed for file operations such as reading, writing, and deleting, and this class is utilized across the other three windows.
- Adding a Book
```python
    #-------------------------------------------------------------------
    #AddWindow.py
    FileManager = FileManager() # FileManager object created for file operations

    #-------------------------------------------------------------------
    #AddWindow.py
    
    self.AddButton.clicked.connect(lambda:self.AddButtonFunction(Form)) # when the AddButton clicked

    #-------------------------------------------------------------------
    def AddButtonFunction(self,Form):
        self.FileManager.append_to_file( f"{self.TitleEdit.text()},{self.AuthorEdit.text()},{self.YearEdit.text()},{self.PageEdit.text()}\n") # calling the append_to_file method
        Form.hide()
    #-------------------------------------------------------------------
    def append_to_file(self, content): # Function that adds a book to 'Books.txt'
        with open(self.filename, 'a+') as file:
            file.write(content)
```

- Deleting a Book
```python
    #-------------------------------------------------------------------
    #DelWindow.py
    FileManager = FileManager() # FileManager object created for file operations

    #-------------------------------------------------------------------
    #DelWindow.py
    self.DelButton.clicked.connect(lambda:self.DelButtonFunction(Form)) # when the DelButton clicked

    #-------------------------------------------------------------------
    #DelWindow.py

    def DelButtonFunction(self,Form):
        self.FileManager.delete_book(self.DelEdit.text()) # calling the delete_book method
        Form.hide() #hides the page when the DelButton is clicked.

    #-------------------------------------------------------------------
    #FileManager.py

    def delete_book(self, title_to_remove):
        # Open the file in read mode and reading the books
        with open(self.filename, 'r') as file:
            lines = file.read().splitlines()

        # Deleting a book with that title.
        lines = [line for line in lines if not line.startswith(title_to_remove)]

        # Open the file in write mode and write the updated content.
        with open(self.filename, 'w') as file:
            for line in lines:
                file.write(f"{line}\n")
```

- Listing Books
```python
    #MainWindow.py
    FileManager = FileManager() # FileManager object created for file operation

    #-------------------------------------------------------------------
    #MainWindow.py
    self.ListPushButton.clicked.connect(self.load_books_into_listview)

    #-------------------------------------------------------------------
    #MainWindow.py

    def load_books_into_listview(self):
        books = self.FileManager.read_books_from_file()
        
        # ListView is a model-based widget, Created a model for listing books
        model = QStandardItemModel(self.listView)
        for book in books:
            item = QStandardItem(book) # Created a QStandardItem for each book and added it to model
            model.appendRow(item)
        
        self.listView.setModel(model) # Connecting the model to the ListView

    #-------------------------------------------------------------------
    #FileManager.py

    def read_books_from_file(self): # Function that reads books from file
        with open(self.filename, 'r') as file:
            lines = file.read().splitlines()
        return lines

```
