class Book:
    def __init__(self, name, author, page):

        #init shows to us default informations about class object
        self.name = name
        self.author = author
        self.page = page
        self.available = True
        self.user = None

    def show_info(self):
        print("Book Name: ", self.name)
        print("Author Name: ", self.author)
        print("Page: ", self.page)
        print("Is it available for borrowing? ", self.available)
        

    def borrow(self, user):
        if self.available:
            self.available = True
            self.user = user
            print("You borrow it, enjoy!")

        else:
            print("This book is not avalible now, sorry 🙁")

    def return_book(self):
        self.available = True
        self.user = None
        print("You returned this book, thank you 😊")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, Book):
        self.books.append(Book)

    def remove_book(self, Book):
        self.books.remove(Book)

    def list_books(self):
        for i in self.books:
            i.show_info()

    def borrow(self, Book, user):
        Book.borrow(user)

    def return_book(self, Book):
        Book.return_book()


Book1 = Book("Python ile Veri Bilimi", "Jake VanderPlas", 544)
Book2 = Book("Veri Bilimi İçin İstatistik", "Erdem Karabulut", 320)
Book3 = Book("Makine Öğrenmesi", "Alpaydin Ethem", 583,)

Library = Library()
Library.add_book(Book1)
Library.add_book(Book2)
Library.add_book(Book3)
Library.list_books()
