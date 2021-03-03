# Example 01: overloading built-in functions __len__, overloading operator __eq__ and __contains__ __add__
class Book:

    def __init__(self, isbn, name, author):
        self.isbn = isbn
        self.name = name
        self.author = author

    def add_to_library(self, library):
        self.library = library

    def __eq__(self, other):
        """
        Method that checks if two books are the same.
        :param other: book we want to compare to existing books in the library
        :return: True if two books have the same ISBN, otherwise False
        """
        if isinstance(other, Book) and self.isbn == other.isbn:
            return True
        return False


class Address:

    def __init__(self, street, number, city):
        self.street = street
        self.number = number
        self.city = city


class Library:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def __len__(self):
        """
        Method that overloads the built-in function len()
        Usage: len(library)
        :return: number of books in the library
        """
        return len(self.books)

    def add_a_book(self, book):
        if book in self:
            return f"Cannot add book with isbn: {book.isbn} to library!"
        book.add_to_library(self)
        self.books.append(book)
        return f"Book with isbn {book.isbn} successfully added!"


    def __add__(self, other):
        """
        Method that overloads the operator +
        When called library + book it will add the book to the library
        :param other: Book that we want to add to the library
        :return: Message that indicates if the book was added or not
        """
        if other in self:
            return f"Cannot add book with isbn: {other.isbn} to library!"
        other.add_to_library(self)
        self.books.append(other)
        return f"Book with isbn {other.isbn} successfully added!"

    # in and is not: is a membership operator
    def __contains__(self, item):
        """
        Method that overloads the operator in
        Checks if the library has a book with the same ISBN
        :param item: new book we want to add to the library
        :return: True if the book successfully added, otherwise False
        """
        for book in self.books:
            if book == item:
                return True
        return False


# Example 02: overloading custom functions
class Person:

    # ssn - social security number
    def __init__(self, ssn):
        self.ssn = ssn

    # None keyword used to define null variable or an object.
    # None is an object with a NoneType data type
    def introduction(self, name, age=None, profession=None):
        intro = ""
        self.name = name
        intro += f"Person: {self.name}"
        if age is not None:
            self.age = age
            intro += f"\t Age: {self.age}"

        if profession is not None:
            self.profession = profession
            intro += f"\t Profession: {self.profession}"

        return intro


def creat_add_book(library: Library, book: Book):
    """
    Getting rid of boilerplate code
    :param library:
    :param book:
    :return:
    """
    #print(library.add_a_book(book))
    print(library + book)
    print(f"Total number of books in library: {len(library)}")


if __name__ == "__main__":
    print(__name__)
    # Example 01
    address1 = Address("Street1", 1, "City1")
    library1 = Library("library1", address1)

    book1 = Book("isbn1", "Title1", "Author1")
    book2 = Book("isbn1", "Title2", "Author2")
    book3 = Book("isbn2", "Title2", "Author2")

    '''
    print(library1.add_a_book(book1))
    #print(library1 + book1)
    print(f"Total number of books in library: {len(library1)}")

    msg = library1.add_a_book(book2)
    #msg = library1 + book2
    print(msg)
    print(f"Total number of books in library: {len(library1)}")

    print(library1.add_a_book(book3))
    # print(library1 + book3)
    print(f"Total number of books in library: {len(library1)}")
    '''

    creat_add_book(library1, book1)
    creat_add_book(library1, book2)
    creat_add_book(library1, book3)

    # Example 02
    person1 = Person(111111111)
    print(person1.introduction("Kevin"))

    person2 = Person(222222222)
    print(person1.introduction("John", 21))

    person2 = Person(333333333)
    print(person1.introduction("Anna", 23, "teacher"))
