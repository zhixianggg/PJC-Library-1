from os import path


def formatFullName(Format):
    """Returns the full name of the format character (S, L, O, P) given."""
    if Format == 'S':
        return "Standard size"
    if Format == 'L':
        return "Large print"
    if Format == 'O':
        return "Oversize"
    if Format == 'P':
        return "Paperback"


def DISPLAYBOOKS():
    # check if BOOK.DAT exists
    if not path.isfile("BOOK.DAT"):
        print("*Error: The file BOOK.DAT does not exist.*")
        return

    with open("BOOK.DAT", "r") as infile:
        # display the creation date and number of book data stored in the file
        CreationDate, NumberOfBooks = infile.readline().split(" | ")
        CreationDate = CreationDate[8:] + CreationDate[3:5] + CreationDate[:2]
        print("Creation Date: {0}".format(CreationDate))
        print("# Books: {0}".format(NumberOfBooks))
        print()

        # display the headings
        print("{0:<20}{1:<30}{2:<30}{3:<15}"
              .format("Catalogue No", "Title", "Author", "Book Type"))
        print('-'*95)

        # display the info for each book data stored in the file
        for line in infile:
            CatalogueNo, Title, Author, Format = line.split(" | ")
            Format = str(formatFullName(Format[:-1]))
            print("{0:<20}{1:<30}{2:<30}{3:<15}"
                  .format(CatalogueNo, Title, Author, Format))
