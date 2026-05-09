####### Class
'''
# define a class
class Dog:
    sound = "bark"  # class attribute

###Object
dog1 = Dog() # Creating object from class
print(dog1.sound) # Accessing the class
'''


# Initiate Object with __init__()
'''
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, x, y):
        self.name = x  # Instance attribute
        self.age = y  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)

'''


# __str__() Method

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"{self.name} is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)
