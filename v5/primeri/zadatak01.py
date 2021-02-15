# Assignment 1: Implement a library system

class Book:

    def __init__(self, isbn, name, author, genres):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.genres = genres

    def to_string(self):
        return f"{self.isbn:20} {self.name:20} {self.author:15} {self.__list_all_genres()}"

    def __list_all_genres(self):
        return ''.join(self.genres)

    def add_book_to_library(self, new_library):
        self.library = new_library
        self.library.add_book(self)

    def equals(self, other_book):
        return self.isbn == other_book.isbn


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def to_string(self):
        return f"{self.name:10} \n {self.__list_all_books()}"

    def __list_all_books(self):
        out_str = ''
        for book in self.books:
            out_str += book.to_string() + '\n'
        return out_str

    def add_book(self, new_book):
        for book in self.books:
            if not book.equals(new_book):
                self.books.append(book)


def add_new_book_to_library():
    isbn = input("1. Enter isbn")
    name = input("2. Enter name")
    author = input("2. Enter author")

    book = Book(isbn, name, author, [])
    book.add_book_to_library(library)


def list_all_books_in_library():
    print(library.to_string())


if __name__ == '__main__':

    global library
    library = Library('Library1')

    while True:
        print("1. Create new book and add it to the library")
        print("2. List all books in library")
        option = input('Option>>>')

        if option == '1':
            add_new_book_to_library()
        elif option == '2':
            list_all_books_in_library()