# Inheritance
# The child class can access the attributes ad methods of the parent class


# class Book:
#     name = "Book1"
#     def display(self):
#         print(f"The book name is {self.name}")
        
# class eBook(Book): # This is Single Inheritance => The child class is inheriting from a singal parent class
#     def display(self):
#         print("Displaying from eBook.")
    
# # eBook is a child class and Book is a parent class
# e1 = eBook()
# print(e1.name)
# e1.display()


# class ABC:
#     name = "ABC"
    
# class DEF:
#     name1 = "DEF"
    
# class GHI(ABC,DEF): # This is Multiple Ineritance => A child class inherita from multiple parent classes
#     pass

# g1 = GHI()
# print(g1.name)


# Multilevel Inheritance => A child class inherits from multi level parent class
# class GrandParentParent:
#     namegpp = "GrandParentParent"
#     def display(self):
#         print("Display from Grandparentparent")

# class GrandParent(GrandParentParent):
#     name = "GrandParent"
#     def display(self):
#         print("Display from Grandparent")
    
# class Parent(GrandParent):
#     namep = "Parent"
    
    
# class Child(Parent):
#     namec = "Child"
    
#     name = "Name from Child" # Attribute / method overwriting
#     def display(self):
#         print("Display from Child")
    
# c1 = Child()
# print(c1.namec)
# print(c1.namep) 
# print(c1.name) 
# print(c1.namegpp) 
# print(c1.display()) 


# p1 = Parent()
# p1.display()

class A:
    print("A")

class ABC(A):
    name = "ABC"
    def display(self):
        print("Displaying from ABC")
        
    
class DEF:
    name1 = "DEF"
    def display(self):
        print("Displaying from DEF")
    
class GHI(ABC,DEF): # This is Multiple Ineritance => A child class inherita from multiple parent classes
    pass

g1 = GHI()
print(g1.name)
g1.display()

# To tackle this confusion, Python Implements MRO
# Method Resolution Order
# MRO defines which class to visit next
# We always find MRO of the class not of the object
# To fidnd the MRO, we have a method clalled mro()

print(GHI.mro())