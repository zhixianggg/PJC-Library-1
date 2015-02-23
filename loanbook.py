from datetime import date
import datetime
import createbook


def getLoanDate():
    """Asks for date that the book is taken out on loan"""
    while True:
    	day = input("Enter day:  ")
    	month = input("Enter month:  ")
    	year = input("Enter year:  ")
    	if (int(day) < 31       #maximum day
    			and len(day) == 2
				and int(month) < 12
				and len(month) == 2
				and len(year) == 4
				and int(year) >= 1999
				and int(year) <= int(str(date.today())[:4] ):
					LoanDate = day + "-" + month + "-" + year
					print(LoanDate)
					return LoanDate
		print("*Invalid input. Date should be 8 digits *")

def getCatalogueNo():
    """Asks for the catalogue number of a book until input is valid,
    and returns a string."""
    while True:
        CatalogueNo = input("Enter catalogue number: ")
        if (CatalogueNo.isdigit()
                and len(CatalogueNo) == 7
                and int(CatalogueNo[:4]) >= 1999    # year PJC founded
                and int(CatalogueNo[:4]) <= int(str(date.today())[:4])
                and CatalogueNo in createbook.UNIQUE_CATNO):
                    print()
                    return CatalogueNo
        print("*Invalid input. Catalogue number is 7 digits.*")
        print("*1st 4 - year placed in library, last 3 - unique identifier.*")
		
def getBorrowerID():
	"""Asks for identifier for the user"""
	while True:
		BorrowerID = input("Enter borrower ID:  ")
		if (BorrowerID.isdigit()
				and len(BorrowerID) <= 5):
					print()
					return BorrowerID
		print("*Invalid input. BorrowerID is at most 5 digits.*")

def getBorrowerName():
	"""Asks for name of the user"""
	while True:
        BorrowerName = input("Enter your name:  ")
        if len(BorrowerName) <= 20:
            print()
            return BorrowerName
        print("*Invalid input. Name is at most 20 characters.*")

def getLoanType():
	"""Asks for type of loan"""
	while True:
        LoanType = input("Enter LoanType (Overnight, Three Days, Seven Days, Fourteen Days): ")
        if (LoanType[0] in [O, T, S, F]): 
            print()
            return LoanType
        print("*Invalid input. There are four loan types. Overnight, Three Days, Seven Days, Fourteen Days.*")
        
def getReturnDate():
	"""Generate the date by which the book should be returned"""
	while True:
		one_day = datetime.timedelta(days = 1)
		if LoanType[0] == O:
			ReturnDate = LoanDate + one_day
		elif LoanType[0] == T:
			ReturnDate = LoanDate + 3*(one_day)
		elif LoanType[0] == S:
			ReturnDate = LoanDate + 7*(one_day)
		elif LoanType[0] == F:
			ReturnDate = LoanDate + 14*(one_day)
		return ReturnDate

def CREATELOAN():

	with open("LOAN.DAT", "a") as outfile:
            # obtain user input and write to outfile
            book = Book(getLoanDate(), getCatalogueNo(),getBorrowerID(), getBorrowerName(),getReturnDate(),getLoanType())
            print(book, file=outfile)


	
	print("* Data written to LOAN.DAT *")
	
def REPORT():
	
	UNIQUE_LOANDATElist = []
	with open("LOAN.DAT", "r") as infile:
		#Title not accounted for. 
		## append everything into a list
		LoanDatelist=[]
		CatalogueNolist = []
		BorrowerIDlist = []
		BorrowerNamelist =[]
		ReturnDatelist =[]
		for line in infile:
            LoanDate, CatalogueNo, BorrowerID, BorrowerName, ReturnDate, LoanType = line.split(" | ")
            LoanDatelist.append(LoanDate)
            CatalogueNolist.append(CatalogueNo)
            BorrowerIDlist.append(BorrowerID)
            BorrowerNamelist.append(BorrowerName)
            ReturnDatelist.append(ReturnDate)
            if LoanDate not in UNIQUE_LOANDATE:
            	UNIQUE_LOANDATElist.append(LoanDate)
        #search through LoanDatelist for the various positions in which LOANDATE reoccurs
        for position, item in enumerate(LoanDatelist):
        	print("Date: {0}".format(UNIQUE_LOANDATElist[i]))
            print("-"*95)
            noofbooks = 0
            if item == UNIQUE_LOANDATElist[i]:
                noofbooks += 1
                print("{0}", \t, "{1}" , \t " {2} ", " {3} ", " {4} ", " {5} ".format(noofbooks, CatalogueNo[position], Title, BorrowerID[position], BorrowerName[position], ReturnDate[position]))
            print(UNIQUE_LOANDATElist[i][-4] , noofbooks)
        
                
            
	
