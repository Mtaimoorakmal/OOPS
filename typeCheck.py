# Creat a Class
class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self , name ):
        self.title = name
       
    # creat instances methods

#Creat another Class
class NewsPaper:
    def __init__(self , name):
        self.title = name

# Creat Some instances of the Classes
b1 = Book("The Catcher in the Rye")
b2 = Book("THe Grapes of Wrath")
n1 = NewsPaper("The Dawn")
n2 = NewsPaper("The News")

# use type() to inspect the Object type

print(type(b1))
print(type(n1))

# Compare Two types togather

print(type(b1) == type(b2))
print(type(b1) == type(n2))

# use "isinstance" to compare a specific instance tp a knowm type
print(isinstance(b1 , Book))
print(isinstance(n1 , NewsPaper))
print(isinstance(b1 , NewsPaper))
print(isinstance(n2 , object)) #object is default in python as every thing in pytho is an object


