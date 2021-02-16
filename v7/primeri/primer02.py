import v7.primer01 as primer01

print(primer01.__name__)
address1 = primer01.Address("Street1", 1, "City1")
library1 = primer01.Library("library1", address1)

book1 = primer01.Book("isbn1", "Title1", "Author1")
book2 = primer01.Book("isbn1", "Title2", "Author2")
book3 = primer01.Book("isbn2", "Title2", "Author2")

primer01.creat_add_book(library1, book1)
primer01.creat_add_book(library1, book2)
primer01.creat_add_book(library1, book3)
