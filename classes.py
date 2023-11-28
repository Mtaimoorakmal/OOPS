# Creat a Class
class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized

    def __init__(self , title , author, pages , price):
        self.title = title
        # add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret  = "This is a secret attribute"



    # creat instances methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount


# Creat instances of the Class i.e Book instances

b1 = Book("War and Peace","Leo Tolstoy" , 1225 , 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger" , 234  , 29.95)


# Print the price of b1 

print(b1.getPrice())

# try setting the discount
print(f"Price of b2 Before discount: {b2.getPrice()}")
b2.setDiscount(0.25)
print(f"Price of b2 After 25% discount: {b2.getPrice()}")

# Properties with double IUnderscore are hidden by the interpreter
print(b2.__secret) # cannot be accussed and gives an attributeError
# comment the above line to see the next lines result
print(b2._Book__secret) # this will give the output for hidden attributes