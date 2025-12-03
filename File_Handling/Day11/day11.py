# OOP - Object Oriented Programming

# In OOP, everything is represented as class and objects

# Till now we have learned functional programming
# Now in OOP we will learn about classes and objects

# Class - Class is a blueprint to create an objects
# class keyword is used to define a class 
# Objects - Objects are the instance of a class 
# We need to call a class in order to create a object if a class
# We use () while calling a class

# Example

# Class Attributes / Class Methods
# The attributes and methods donot change according to the objects
# class Student:
#     name = "Saugat Bikram" # They are called attributes
#     age = 21 # Attributes are the variables defined inside the class
#     position = "Data Scientist"
    
#     def abc(self): # Methods are the functions defined inside the class
#         print("ABC")
#     def printself(self):
#         print(self)
# s1 = Student()
# print(s1.position)
# s1.abc()
# print(s1)
# s1.printself()

# s2 = Student()
# print(s2.age)
# print(s2)
# s2.printself()

# s3 = Student()
# s3.abc()
# print(s3.position)
# print(s3)
# s3.printself()


# Object Attributes / Object Methods
# The attributes and methods change according to the object
class Student:
    def abc(self): # Methods are the functions defined inside the class
        print("ABC")
    def set_info(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Position: ", self.position)

s1 = Student()
s1.set_info("Saugat",21,"Data Scientist")
s1.display()

s2 = Student()
s2.set_info("Ram",28,"Developer")
s2.display()

s1.set_info("Hari",50,"abc")
s1.display()


# Create a class and objects
# Perform all the instructions that we studied today

# Create a class student and create different objects
# Use class attributes and object attributes