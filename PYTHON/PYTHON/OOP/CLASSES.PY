'''
Abstraction - interface that allows a user to turn 
on or off of functionality.
Hide the implementation and only show necessary details
to the user.

Constructors - create or initialize an object of a class 
with or without starting values

Default Constructors 
- without it
automatically created:
def __init__(self):
    pass

No Argument Constructors
def __init__(self):
    print("No arguments")

Parameter Constructors
def __init__(self,variable):
    self.variable = variable

self - refers to the current class / object

arguments are class attributes
'''

class Example:
    def __init__(self,variable):
        self.variable = variable


new_object = Example('new_object_name')



'''
Encapsulation - bundling of data and hide state

Public are by default 
__ means private

'''

class Example2:
    def __init__(self,variable):
        self.__variable = variable

    def get_variable(self):
        return self.__variable

    def set_variable(self,variable):
        self__variable = variable


'''
Inheritance - process of acquiring properties from one 
class to other classes

'''

class Animal:
    age: int 
    def eat(self):
        print('Animal eating')

class Dog(Animal):
    # all Animal attributes
    race: str 

    # all Animal methods
    def talk(self):
        print('Bark!')

    # override 
    def eat(self):
        print("Chews on bone!")

    
'''
self - refer to the current object that is created or 
being instantiated.
Used to differentiate between the instance variables
& parameters with the same name.

super - used to refer to the parent class.
Call parent class methods and constructors.

'''

class Person:
    def __init__(self,name):
        self.name = name 

class Student(Person):
    def __init__(self, name, degree):
        super().__init__(name=name)
        self.degree = degree

'''
Polymorphism - many forms

For different child classes are used same functions
'''

def new_function(e: Person):
    e.function1()
    e.function2()


'''
Composition - create objects made up of other objects
'''

Class Engine:
    def __init__(self,engineType):
        self.engineType = engineType 
    def startEngine(self):
        print("Engine is running")

Class Vehicle:
    def __init__(self,type,engine):
        self.type = type 
        self.engine = engine

engine = Engine("V6")
vehicle = Vehicle("Car",engine)
vehicle.engine.startEngine()