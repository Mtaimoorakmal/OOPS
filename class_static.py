# Creat a Class
class Book:
    # properties defined at classlevel are shared by All instances
    BOOK_TYPES = ("HARDCOVER" ,"PAPERBACK","EBOOK")
    # double_Underscore properties are hidden from other instances
    __booklist = None
    # creat a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # creat a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist





    #instance methods recived a specific Object instance as an argument
    #and operate on data specific to that object instance

    def setTitle(self , newTitle):
        self.title = newTitle

    def __init__(self, title , booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book Type")
        else:
            self.booktype = booktype


# access the class attribute

print( "BOOK types : ", Book.getbooktypes())

# creat come Book instances
b1=Book("Title 1" , "HARDCOVER")
# b2=Book("Title 2" , "COMIC") # this will raise an ValueError: COMIC is not a valid book Type
#lest corret this

b2=Book("Title 2" , "PAPERBACK")

# USe the Static method to access a singlton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
