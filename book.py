class Book:

    def __init__(self, CatalogueNo, Title, Author, Format,Classification):
        self.CatalogueNo = CatalogueNo
        self.Title = Title
        self.Author = Author
        self.Format = Format
        self.Classification = Classification

    def getCatalogueNo(self):
        return self.CatalogueNo

    def setCatalogueNo(self, CatalogueNo):
        self.CatalogueNo = CatalogueNo

    def getTitle(self):
        return self.Title()

    def setTitle(self, Title):
        self.Title = Title

    def getAuthor(self):
        return self.Author

    def setAuthor(self, Author):
        self.Author = Author

    def getFormat(self):
        return self.Format

    def setFormat(self, Format):
        self.Format = Format
    
    def getClassification(self):
    	return self.Classification()
    
    def setClassification(self):
    	self.Classification = Classification

    def __str__(self):
        return "{0} | {1} | {2} | {3}" \
               .format(self.CatalogueNo, self.Title, self.Author, self.Format)
    
    

