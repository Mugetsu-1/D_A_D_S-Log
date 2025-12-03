# Encapsulation
# The concept of Data hiding
# We use doube underscore __ to ide the method and attribute
# The hidden data can be acessed only from inside the class. EVen the object of the class cannot access the hidden data


# class Credential:
#     username = "Saugat"
#     __password = "Saugat123"
#     new_password = __password
    
#     def __abc(self):
#         return self.__password
    
#     def ghi(self):
#         return self.__abc()
    
# c1 = Credential()
# print(c1.new_password)

# print(c1.ghi())


# Polymorphism
# Same action different behaviour

# => +

# a = 10
# b = 5
# print(a+b)

# a = '10'
# b = '5'
# print(a+b)


# class Bird:
#     name = "Bird"
#     def sound(self):
#         print("Bird Sound")
        
# class Dog:
#     name = "Dog"
#     def sound(self):
#         print("Dog Sound")
        
# class Cat:
#     name = "Cat"
#     def sound(self):
#         print("Cat Sound")
        
# b1 = Bird()
# print(b1.name)
# b1.sound()

# d1 = Dog()
# print(d1.name)
# d1.sound()

# c1 = Cat()
# print(c1.name)
# c1.sound()


# Abstraction
# Showing what is needed, hiding the implementation details

# @abstractmethod
# We should import abstractmethod from abc module

from abc import abstractmethod, ABC #=> Abstract Base Class

# abstractmethod defines hard and fast rule 
# if the parent class has inherited from ABC class and have used abstractmethod decorator
# Every child class that has inherited the parent class should have same abstratmethod

class ParentClass(ABC):
    
    @abstractmethod
    def show(self):
        print("Showing the data")
        
        
class Child1(ParentClass):
    def show(self):
        for i in range(10):
            print(i ,end=" ")

c1 = Child1()
c1.show()
    
    
class Child2(ParentClass):
    name = "ABC"
    
    # def show(self):
    #     print(1)

c2 = Child2()
print(c2.name)
c2.show()