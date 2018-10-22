"""
The Four Pillars of OOP in Python 3 for Beginners
Created by Febin George
EXERCISE - CLASSES AND OBJECTS
Write and object oriented program that performs the following tasks:
1. Define a class called "Employee" and create an instance of that class
2. Create an attribute called name and assign it with a value
3. Change the name you previously defined within a method and call this method by making use of the object you created
"""

#class definition
class Employee:
    #Initialize name
    name = "Robert"


#Create new object named Bob
Bob = Employee()

print(Bob.name)

#Change new objects name
Bob.name = "Bob"

print(Bob.name)