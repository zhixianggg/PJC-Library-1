class Fiction(Book):

	def __init__(self, CatalogueNo, Title, Author, Format, Classification, Genre):
		'''inherit Book class with additional attribute, Genre'''
		Book.__init__(self, CatalogueNo, Title, Author, Format, Classification)
		self.Genre = Genre
		
	def __str__(self):
                return ("{0} | {1} | {2} | {3} | {4} | {5}".format(self.CatalogueNo, self.Title, self.Author, self.Format, self.Classification, self.Genre))
    
class NonFiction(Book):

	def __init__(self, CatalogueNo, Title, Author, Format, Classification, DeweyNumber):
		'''inherit Book class with additional attribute, Genre'''
		Book.__init__(self, CatalogueNo, Title, Author, Format, Classification)
		self.DeweyNumber = DeweyNumber
		
	def __str__(self):
                return ("{0} | {1} | {2} | {3} | {4} | {5}".format(self.CatalogueNo, self.Title, self.Author, self.Format, self.Classification, self.DeweyNumber))

def UPDATEBOOKS():
    # check if BOOK.DAT exists
    if not path.isfile("BOOK.DAT"):
        print("*Error: The file BOOK.DAT does not exist.*")
        return

    with open("BOOK.DAT", "r") as infile:
    	outfile = "UBOOK.DAT"
        # display the creation date and number of book data stored in the file
        CreationDate, NumberOfBooks = infile.readline().split(" | ")


        CreationDate = CreationDate[8:] + CreationDate[3:5] + CreationDate[:2]
        print("Creation Date: {0}".format(CreationDate))
        print("# Books: {0}".format(NumberOfBooks))
        print()
        
        #write creation date and number of book data stored in the file on UBOOK.DAT
        print("Creation Date: {0}".format(CreationDate), file=outfile)
        print("# Books: {0}".format(NumberOfBooks), file=outfile)
        print()


        # display the headings
        print("{0:<20}{1:<30}{2:<30}{3:<15}{4:<11}{5:<11}{6:<11}"
              .format("Catalogue No", "Title", "Author", "Book Type", "Classification", "DeweyNumber", "Genre"))
        print('-'*95)
        
        #write headings on UBOOK.DAT
        print("{0:<20}{1:<30}{2:<30}{3:<15}{4:<11}{5:<11}{6:<11}"
              .format("Catalogue No", "Title", "Author", "Book Type", "Classification", "DeweyNumber", "Genre"), file=outfile)
        print('-'*95, file = outfile)

        # display the info for each book data stored in the file and write on UBOOK.DAT whilst asking for additional input
        for line in infile:
            CatalogueNo, Title, Author, Format = line.split(" | ")
            getClassification()
            if Classification[0] == F:
            	DeweyNumber = 000.000
            	getGenre()
            elif Classification[0] == N:
            	Genre = 'NONE'
            	getDeweyNumber()
            Format = str(formatFullName(Format[:-1]))
            print("{0:<20}{1:<30}{2:<30}{3:<15}{4:<11}{5:<11}{6:<11}"
                  .format(CatalogueNo, Title, Author, Format ,Classification, DeweyNumber, Genre))
            print("{0:<20}{1:<30}{2:<30}{3:<15}{4:<11}{5:<11}{6:<11}"
                  .format(CatalogueNo, Title, Author, Format ,Classification, DeweyNumber, Genre),file =outfile)
        
        #write everything into a file
        
    
                  
                  
def getClassification():
	while True:
        Classification = input("Enter Classification: ")
        if (Classification.isalpha()):
                    print()
                    return Classification
        print("*Invalid input. Classification should be alphabetic*")
        
def getGenre():
	while True:
        Genre = input("Enter Genre: ")
        if (Genreisalpha()):
                    print()
                    return Genre
        print("*Invalid input. Genre should be alphabetic*")

def getDeweyNumber():
    while True:
        DeweyNumber = input("Enter DeweyNumber: ")
        if (len(DeweyNumber) == 7
                and DeweyNumber[3] == '.'):
                    print()
                    return DeweyNumber
        print("*Invalid input. DeweyNumber is in the form 999.999.*")
