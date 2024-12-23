import fibo
# import introcengmodule as nm

fibo.fib(1000)

# fibo.__name__


# from fibo import fib, fib2
# fib(500)


# from fibo import *
# fib(500)

# import fibo as fib

# from fibo import fib as fibonacci
# fibonacci(500)



# run from command window main.py test1 test2 test2  

# import sys
# print("You entered: ",sys.argv[1], sys.argv[2], sys.argv[3])

import sys

for module_name in sys.modules.keys():
    print(module_name)

# print(nm.add(1, 2))

# Define a class named 'Person'
class Person:
    # Constructor method to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("John", 34)
person1.display()


# # Define a derived class named 'Student' that inherits from 'Person'
# class Student(Person):
#     # Constructor method to initialize the object
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)  # Call the constructor of the base class
#         self.student_id = student_id

#     # Method to display the student's details
#     def display(self):
#         super().display()  # Call the display method of the base class
#         print(f"Student ID: {self.student_id}")

# # Create an instance of the Student class
# student1 = Student("Eyup", 30, "S12345")

# # Call the display method to print the student's details
# student1.display()