from book import Book
from datetime import date

global(UNIQUE_CATNO)
UNIQUE_CATNO = set()
# set containing all the unique catalogue numbers already used


def getCatalogueNo():
    """Asks for the catalogue number of a book until input is valid,
    and returns a string."""
    while True:
        CatalogueNo = input("Enter catalogue number: ")
        if (CatalogueNo.isdigit()
                and len(CatalogueNo) == 7
                and int(CatalogueNo[:4]) >= 1999    # year PJC founded
                and int(CatalogueNo[:4]) <= int(str(date.today())[:4])
                and CatalogueNo not in UNIQUE_CATNO):
                    print()
                    UNIQUE_CATNO.add(CatalogueNo)
                    return CatalogueNo
        print("*Invalid input. Catalogue number is 7 digits.*")
        print("*1st 4 - year placed in library, last 3 - unique identifier.*")


def getTitle():
    """Asks for the title of a book until input is valid,
    and returns a string."""
    while True:
        Title = input("Enter title: ").title()
        if len(Title) <= 30:
            print()
            return Title
        print("*Invalid input. Title is at most 30 characters.*")


def getAuthor():
    """Asks for the author of a book until input is valid,
    and returns a string."""
    while True:
        Author = input("Enter author name: ").title()
        if len(Author) <= 30:
            print()
            return Author
        print("*Invalid input. Author name is at most 30 characters.*")


def getFormat():
    """Asks for the format of a book until input is valid,
    and returns a string."""
    while True:
        Format = input("Enter book format (S, L, O, P): ").upper()
        if Format == 'S' or Format == 'L' or Format == 'O' or Format == 'P':
            print()
            return Format
        print("*Invalid input. Format is a single character (S, L, O, P).*")


def getNumberOfBooks():
    """Asks for the number of books about to be entered until input is valid,
    and returns an int."""
    while True:
        NumberOfBooks = input("Enter number of books to input: ")
        if NumberOfBooks.isdigit() and int(NumberOfBooks) > 0:
            print()
            return int(NumberOfBooks)
        print("*Invalid input. Try again.*")


def getDate():
    """Returns today's date in the format DD-MM-YYYY"""
    today = str(date.today())
    CreationDate = today[8:] + "-" + today[5:7] + "-" + today[:4]
    return CreationDate


def CREATEBOOK():
    NumberOfBooks = getNumberOfBooks()
    bookCount = 1   # the i-th book about to be entered

    with open("BOOK.DAT", "a") as outfile:
        # write today's date and number of books to top of outfile
        print("{0} | {1}".format(getDate(), NumberOfBooks), file=outfile)

        while NumberOfBooks > 0:
            print("--- Book #{0} ---".format(bookCount))

            # obtain user input and write to outfile
            book = Book(getCatalogueNo(), getTitle(), getAuthor(), getFormat())
            print(book, file=outfile)

            bookCount += 1
            NumberOfBooks -= 1

	
	print("* Data written to BOOK.DAT *")
    
