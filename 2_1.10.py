class Patron:
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = 0

    def checkOut(self):
        self.booksCheckedOut += 1

    def returnBook(self):
        self.booksCheckedOut -= 1

    def __str__(self):
        return self.name


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checkedOutTo = None
        self.waitingList = []

    def checkOut(self, patron):
        if self.checkedOutTo is None:
            patron.checkOut()
            self.checkedOutTo = patron
        else:
            if patron not in self.waitingList and patron != self.checkedOutTo:
                self.waitingList.append(patron)

    def returnBook(self):
        self.checkedOutTo.returnBook()
        self.checkedOutTo = None
        if len(self.waitingList) > 0:
            self.checkOut(self.waitingList.pop(0))

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nChecked out to: {self.checkedOutTo}\nWaiting list: {self.waitingList}"


class Library:
    sds = 0

    def __init__(self):
        self.books = []
        self.patrons = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)

    def findBook(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def addPatron(self, patron):
        self.patrons.append(patron)

    def removePatron(self, patron):
        self.patrons.remove(patron)

    def findPatron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        print("EEE")
        return None

    def borrowBook(self, title, name):
        book = self.findBook(title)
        patron = self.findPatron(name.name)
        if book is None:
            print("Book not found.")
        elif patron is None:
            print("Patron not found.")
        elif patron.booksCheckedOut > 3:
            print("Patron has too many books checked out.")
        else:
            book.checkOut(patron)

    def returnBook(self, title):
        book = self.findBook(title)
        if book is None:
            print("Book not found.")
        else:
            book.returnBook()

    def __str__(self):
        return f"Books: {self.books}\nPatrons: {self.patrons}"


def main():
    person1 = Patron("John")
    person2 = Patron("Jane")

    book1 = Book("The Great Gatsby", "person2")
    book2 = Book("The Catcher in the Rye", "person2")
    book3 = Book("The Grapes of Wrath", "person2")

    library = Library()
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)

    library.addPatron(person1)
    library.addPatron(person2)

    library.borrowBook("The Great Gatsby", person2)
    library.borrowBook("The Catcher in the Rye", person2)
    library.borrowBook("The Grapes of Wrath", person2)
    library.returnBook("The Great Gatsby")
    library.borrowBook("The Great Gatsby", person1)
    library.borrowBook("The Great Gatsby", person1)

    for book in library.books:
        print(book)
        print()


if __name__ == "__main__":
    main()
