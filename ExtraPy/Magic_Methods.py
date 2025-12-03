# Magic methods are the special kind of methods that starts and ends with double underscore __
# Python calls them automatically under certain situation so they are called magic methods

# __init__
# __str__
# __len__
# __add__ => +
# __sub__ => -
# __mul__ => *


class Student:
    def __init__(self, name, marks, roll):
        self.name = name
        self.roll = roll
        self.marks = marks
        
    def __str__(self):
        return "This message is coming from str method"
        
s1 = Student("Ujjwal", 95, 1)
print(s1.name)

print(Student)
print(s1)

print(5*10)