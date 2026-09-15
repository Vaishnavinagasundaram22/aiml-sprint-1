#!/usr/bin/env python
# coding: utf-8

# # Object
# 
# ### Definition
# 
# An object is an instance of a class. It represents a real entity created using the class.
# 
# ### Real-World Example
# 
# A class is like a student form design. When we create a student using that design, the created student is an object.
# 
# ### Implementation
# 
# The following program creates an object from the Student class.
# 
# ### Explanation
# 
# Student is the class and student1 is the object created from that class. The object can access the data and methods defined inside the class.

# In[ ]:


class Student:
    name = "Rahul"
    age = 22

student1 = Student()

print(student1.name)
print(student1.age)


# # Constructor (__init__)
# 
# ### Definition
# 
# A constructor is a special method that runs automatically when an object is created.
# 
# ### Real-World Example
# 
# When a student joins a college, their basic details are entered automatically. Similarly, a constructor initializes object details when the object is created.
# 
# ### Implementation
# 
# The following program uses __init__() to initialize student details.
# 
# ### Explanation
# 
# __init__() runs automatically when student1 is created. It assigns the name and age values to the object.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
# student1 = Student("Rahul", 22)
# 
# print(student1.name)
# print(student1.age)

# # Instance Variables
# 
# ### Definition
# 
# Instance variables are variables that belong to a particular object. Each object can have its own values.
# 
# ### Real-World Example
# 
# Two students can have different names and ages. These individual details are stored as instance variables.
# 
# ### Implementation
# 
# The following program creates instance variables for student objects.
# 
# ### Explanation
# 
# name and age are instance variables. Each student object stores its own values.

# In[2]:


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 22)
student2 = Student("Priya", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)


# ### Program Explanation
# 
# In this program, the Student class has two instance variables: name and age.
# 
# student1 and student2 are two different objects, so each object stores its own name and age values.
# 
# self.name and self.age are used to store the values for each object.

# # Class Variables
# 
# ### Definition
# 
# A class variable is a variable that is shared by all objects of a class.
# 
# ### Real-World Example
# 
# All students in a college may belong to the same college name. This common information can be stored as a class variable.
# 
# ### Implementation
# 
# The following program uses a class variable to store the college name.
# 
# ### Explanation
# 
# college is a class variable because it is shared by all Student objects.

# In[3]:


class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Rahul")
student2 = Student("Priya")

print(student1.name, student1.college)
print(student2.name, student2.college)


# # Instance Methods
# 
# ### Definition
# 
# Instance methods are functions defined inside a class that work with the data of an object.
# 
# ### Real-World Example
# 
# A student can perform actions like displaying their details. Similarly, an instance method performs an action using object data.
# 
# ### Implementation
# 
# The following program uses an instance method to display student details.
# 
# ### Explanation
# 
# display_details() is an instance method. It uses self to access the data of the student object.

# In[5]:


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Rahul", 22)

student1.display_details()


# ### Program Explanation
# 
# In this program, display_details() is an instance method.
# 
# student1 calls the method using the dot operator.
# 
# self.name and self.age access the values stored in the student1 object.

# # Static Methods
# 
# ### Definition
# 
# A static method is a method inside a class that does not depend on object data.
# 
# It is created using the @staticmethod decorator.
# 
# ### Real-World Example
# 
# A college may have a common method to check whether a number is even or odd. This does not depend on any particular student's details.
# 
# ### Implementation
# 
# The following program uses a static method to check whether a number is even.
# 
# ### Explanation
# 
# is_even() is a static method because it does not use self or any object data.

# In[6]:


class Student:

    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(Student.is_even(10))


# ### Program Explanation
# 
# In this program, is_even() is a static method.
# 
# It works independently without using object data.
# 
# The method can be called directly using the class name.

# # Class Methods
# 
# ### Definition
# 
# A class method is a method that works with class-level data.
# 
# It is created using the @classmethod decorator and uses cls to refer to the class.
# 
# ### Real-World Example
# 
# A college has one common college name shared by all students. A class method can be used to access or change this common information.
# 
# ### Implementation
# 
# The following program uses a class method to display the college name.
# 
# ### Explanation
# 
# display_college() is a class method. It uses cls to access the class variable college.

# In[7]:


class Student:

    college = "ABC College"

    @classmethod
    def display_college(cls):
        print(cls.college)

Student.display_college()


# # Properties (@property)
# 
# ### Definition
# 
# A property allows us to access a method like a normal variable.
# 
# It is created using the @property decorator.
# 
# ### Real-World Example
# 
# A student can access their full name directly without calling a method. Similarly, @property allows a method to be accessed like an attribute.
# 
# ### Implementation
# 
# The following program uses @property to get a student's name.
# 
# ### Explanation
# 
# full_name() is converted into a property using @property. It can be accessed like a normal variable without using ().

# In[8]:


class Student:

    def __init__(self, name):
        self.name = name

    @property
    def full_name(self):
        return self.name

student1 = Student("Rahul")

print(student1.full_name)


# ### Program Explanation
# 
# In this program, full_name is a property of the Student class.
# 
# @property allows us to access full_name without using parentheses.
# 
# student1.full_name directly returns the student's name.

# # Encapsulation
# 
# ### Definition
# 
# Encapsulation means keeping data and the methods that work with that data together inside a class.
# 
# It also helps to protect data from direct access.
# 
# ### Real-World Example
# 
# An ATM allows us to use a PIN to access the account instead of directly accessing the bank's internal data.
# 
# ### Implementation
# 
# The following program protects the student's marks using a private variable.
# 
# ### Explanation
# 
# __marks is a private variable. It is accessed through a method instead of directly from outside the class.

# In[9]:


class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student1 = Student(85)

print(student1.get_marks())


# ### Program Explanation
# 
# In this program, __marks is a private variable.
# 
# The get_marks() method is used to access the marks.
# 
# This shows how encapsulation keeps data protected inside the class.

# # Abstraction
# 
# ### Definition
# 
# Abstraction means hiding unnecessary internal details and showing only the required information.
# 
# ### Real-World Example
# 
# When we use an ATM, we only see options like Withdraw and Deposit. We do not see the internal banking process.
# 
# ### Implementation
# 
# The following program uses an abstract class to define a required method.
# 
# ### Explanation
# 
# The `pay()` method is defined in the abstract class. The actual payment process is implemented in the child class.

# In[11]:


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment completed using UPI")


payment = UPI()
payment.pay()


# ### Program Explanation
# 
# Payment is an abstract class.
# 
# The @abstractmethod tells the child class that the pay() method must be implemented.
# 
# UPI provides the actual implementation of the pay() method.
# 
# The internal payment process is hidden from the user.

# # Inheritance
# 
# ### Definition
# 
# Inheritance allows one class to use the properties and methods of another class.
# 
# The existing class is called the parent class and the new class is called the child class.
# 
# ### Real-World Example
# 
# A child can inherit common characteristics from their parent. Similarly, a child class can inherit features from a parent class.
# 
# ### Implementation
# 
# The following program shows a child class inheriting a method from the parent class.
# 
# ### Explanation
# 
# Student is the parent class and EngineeringStudent is the child class. EngineeringStudent inherits the display() method from Student.

# In[14]:


class Student:

    def display(self):
        print("Student details")


class EngineeringStudent(Student):

    def show_course(self):
        print("Engineering Course")


student = EngineeringStudent()

student.display()
student.show_course()


# # Multiple Inheritance
# 
# ### Definition
# 
# Multiple inheritance means a child class inherits properties and methods from more than one parent class.
# 
# ### Real-World Example
# 
# A student can learn skills from two different teachers. Similarly, a child class can get features from multiple parent classes.
# 
# ### Implementation
# 
# The following program shows a child class inheriting methods from two parent classes.
# 
# ### Explanation
# 
# Student inherits from both Sports and Music. So, the Student object can use methods from both classes.

# In[17]:


class Sports:

    def play(self):
        print("Playing cricket")


class Music:

    def sing(self):
        print("Singing a song")


class Student(Sports, Music):
    pass


student = Student()

student.play()
student.sing()


# ### Program Explanation
# 
# Sports and Music are the two parent classes.
# 
# Student is the child class that inherits from both parent classes.
# 
# The student object can use both play() and sing() methods.

# # Multilevel Inheritance
# 
# ### Definition
# 
# Multilevel inheritance means a class inherits from another child class, creating a chain of inheritance.
# 
# ### Real-World Example
# 
# A grandfather passes a property to a parent, and the parent passes it to a child. Similarly, inheritance can happen through multiple levels.
# 
# ### Implementation
# 
# The following program shows three levels of inheritance.
# 
# ### Explanation
# 
# Student is the base class. EngineeringStudent inherits from Student, and ComputerStudent inherits from EngineeringStudent.

# In[18]:


class Student:

    def study(self):
        print("Student is studying")


class EngineeringStudent(Student):

    def coding(self):
        print("Learning coding")


class ComputerStudent(EngineeringStudent):

    def programming(self):
        print("Learning programming")


student = ComputerStudent()

student.study()
student.coding()
student.programming()


# ### Program Explanation
# 
# Student is the base class.
# 
# EngineeringStudent inherits from Student.
# 
# ComputerStudent inherits from EngineeringStudent.
# 
# So, ComputerStudent can access methods from both parent levels.

# # Hierarchical Inheritance
# 
# ### Definition
# 
# Hierarchical inheritance means multiple child classes inherit from the same parent class.
# 
# ### Real-World Example
# 
# One teacher can teach multiple students. Similarly, multiple child classes can inherit from one parent class.
# 
# ### Implementation
# 
# The following program shows two child classes inheriting from one parent class.
# 
# ### Explanation
# 
# Student is the parent class. EngineeringStudent and ArtsStudent are child classes that inherit from Student.

# In[21]:


class Student:

    def study(self):
        print("Student is studying")


class EngineeringStudent(Student):

    def coding(self):
        print("Learning coding")


class ArtsStudent(Student):

    def drawing(self):
        print("Learning drawing")


engineering = EngineeringStudent()
arts = ArtsStudent()

engineering.study()
engineering.coding()

arts.study()
arts.drawing()


# ### Program Explanation
# 
# Student is the parent class.
# 
# EngineeringStudent and ArtsStudent are two child classes.
# 
# Both child classes inherit the study() method from the Student class.

# # Polymorphism
# 
# ### Definition
# 
# Polymorphism means one method can perform different actions depending on the object using it.
# 
# ### Real-World Example
# 
# The same person can perform different roles, such as a teacher at college and a customer in a shop.
# 
# ### Implementation
# 
# The following program shows the same method behaving differently for different objects.
# 
# ### Explanation
# 
# Both classes have the same method name `sound()`, but each class gives a different implementation.

# In[23]:


class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# ### Program Explanation
# 
# Dog and Cat both have the same method called sound().
# 
# The Dog object produces "Dog barks" and the Cat object produces "Cat meows".
# 
# The same method name behaves differently for different objects. This is polymorphism.

# # Method Overriding
# 
# ### Definition
# 
# Method overriding happens when a child class provides its own implementation of a method already defined in the parent class.
# 
# ### Real-World Example
# 
# A parent may have a general rule, but a child can change how that rule is performed. Similarly, a child class can redefine a parent method.
# 
# ### Implementation
# 
# The following program shows a child class overriding a parent method.
# 
# ### Explanation
# 
# Both classes have a display() method. The child class provides its own version of the parent method.

# In[25]:


class Student:

    def display(self):
        print("Student details")


class EngineeringStudent(Student):

    def display(self):
        print("Engineering student details")


student = EngineeringStudent()

student.display()


# ### Program Explanation
# 
# Student has a display() method.
# 
# EngineeringStudent overrides the display() method with its own implementation.
# 
# When the EngineeringStudent object calls display(), the child class method is executed.

# # Method Overloading
# 
# ### Definition
# 
# Method overloading means using the same method name with different numbers or types of arguments.
# 
# Python does not support traditional method overloading directly. We can achieve similar behavior using default arguments or *args.
# 
# ### Real-World Example
# 
# A calculator can perform addition with two numbers or three numbers using the same operation.
# 
# ### Implementation
# 
# The following program uses *args to accept different numbers of arguments.
# 
# ### Explanation
# 
# The same add() method can work with different numbers of values because *args accepts multiple arguments.

# In[26]:


class Calculator:

    def add(self, *numbers):
        return sum(numbers)


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))


# ### Program Explanation
# 
# The add() method uses *args to accept any number of values.
# 
# It can add two numbers or three numbers using the same method.
# 
# This is how Python can achieve method overloading behavior.

# # Composition
# 
# ### Definition
# 
# Composition means creating a strong relationship where one class contains an object of another class.
# 
# The contained object is created inside the main class.
# 
# ### Real-World Example
# 
# A car has an engine. The engine is an important part of the car.
# 
# ### Implementation
# 
# The following program shows a Car class containing an Engine object.
# 
# ### Explanation
# 
# The Car class creates and uses an Engine object inside it. This represents a composition relationship.

# In[28]:


class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start_car()


# ### Program Explanation
# 
# Engine is a separate class.
# 
# The Car class creates an Engine object inside its __init__() method.
# 
# The Car uses the Engine object to start the car. This represents composition.

# # Aggregation
# 
# ### Definition
# 
# Aggregation means one class uses an object of another class, but both objects can exist independently.
# 
# ### Real-World Example
# 
# A college has students, but a student can exist even if they leave the college.
# 
# ### Implementation
# 
# The following program shows a College using Student objects.
# 
# ### Explanation
# 
# The Student objects are created outside the College class and then passed to it. So, both can exist independently.

# In[30]:


class Student:

    def __init__(self, name):
        self.name = name


class College:

    def __init__(self, student):
        self.student = student

    def display_student(self):
        print("Student:", self.student.name)


student = Student("Rahul")

college = College(student)

college.display_student()


# ### Program Explanation
# 
# Student and College are two separate classes.
# 
# The student object is created outside the College class and passed to it.
# 
# The College uses the Student object, but the Student can exist independently. This represents aggregation.

# # Association
# 
# ### Definition
# 
# Association means a relationship between two separate classes where one object interacts with another object.
# 
# ### Real-World Example
# 
# A teacher teaches a student. Both teacher and student can exist independently.
# 
# ### Implementation
# 
# The following program shows a Teacher interacting with a Student.
# 
# ### Explanation
# 
# Teacher and Student are separate classes. The Teacher uses the Student object to perform an action.

# In[32]:


class Student:

    def __init__(self, name):
        self.name = name


class Teacher:

    def teach(self, student):
        print("Teacher is teaching", student.name)


student = Student("Rahul")
teacher = Teacher()

teacher.teach(student)


# ### Program Explanation
# 
# Student and Teacher are independent classes.
# 
# The Teacher interacts with the Student object through the teach() method.
# 
# Both objects can exist independently, so this represents association.

# # Magic (Dunder) Methods
# 
# ### Definition
# 
# Magic methods are special methods in Python that start and end with double underscores.
# 
# They are automatically called by Python for specific operations.
# 
# ### Real-World Example
# 
# When we use + between numbers, Python automatically performs addition. Similarly, magic methods control how objects behave during certain operations.
# 
# ### Implementation
# 
# The following program uses the __str__() magic method to define how an object is displayed.
# 
# ### Explanation
# 
# __str__() is automatically called when the object is passed to print().

# In[34]:


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Rahul")

print(student)


# ### Program Explanation
# 
# __str__() is a magic method.
# 
# When print(student) is used, Python automatically calls __str__().
# 
# It returns the student's name instead of showing the default object information.

# # super()
# 
# ### Definition
# 
# super() is used to access methods or the constructor of the parent class from the child class.
# 
# ### Real-World Example
# 
# A child can use something provided by their parent and then add their own features. Similarly, a child class can use the parent class using super().
# 
# ### Implementation
# 
# The following program uses super() to call the parent class constructor.
# 
# ### Explanation
# 
# The child class uses super() to initialize the name from the parent class and then adds its own course value.

# In[35]:


class Student:

    def __init__(self, name):
        self.name = name


class EngineeringStudent(Student):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


student = EngineeringStudent("Rahul", "Python")

print(student.name)
print(student.course)


# ### Program Explanation
# 
# Student is the parent class and EngineeringStudent is the child class.
# 
# super().__init__(name) calls the parent class constructor.
# 
# The child class then adds its own course variable.

# # __str__()
# 
# ### Definition
# 
# __str__() is a magic method that defines what should be displayed when an object is printed.
# 
# ### Real-World Example
# 
# Instead of showing a complicated object identity, we can display useful information such as a student's name.
# 
# ### Implementation
# 
# The following program uses __str__() to display student details.
# 
# ### Explanation
# 
# When the student object is passed to print(), Python automatically calls the __str__() method.

# In[38]:


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


student = Student("Rahul", 22)

print(student)


# ### Program Explanation
# 
# __str__() returns a readable string containing the student's name and age.
# 
# When print(student) is used, Python automatically calls __str__().
# 
# It makes the object easier to understand when displayed.

# # __repr__()
# 
# ### Definition
# 
# __repr__() is a magic method that provides a detailed string representation of an object.
# 
# ### Real-World Example
# 
# A student record can show detailed information when we inspect the object.
# 
# ### Implementation
# 
# The following program uses __repr__() to represent a student object.
# 
# ### Explanation
# 
# __repr__() returns a string that represents the object clearly for developers.

# In[40]:


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"


student = Student("Rahul", 22)

print(repr(student))


# ### Program Explanation
# 
# __repr__() returns a detailed representation of the Student object.
# 
# repr(student) calls the __repr__() method and displays the object's information in a readable format.

# # __len__()
# 
# ### Definition
# 
# __len__() is a magic method used to define the length of an object.
# 
# ### Real-World Example
# 
# A classroom has a certain number of students. Similarly, __len__() can be used to find the number of items in an object.
# 
# ### Implementation
# 
# The following program uses __len__() to find the number of students.
# 
# ### Explanation
# 
# __len__() returns the number of students stored in the Student class.

# In[41]:


class Students:

    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)


students = Students(["Rahul", "Priya", "Arun"])

print(len(students))


# ### Program Explanation
# 
# __len__() returns the number of students stored in the names list.
# 
# When len(students) is used, Python automatically calls the __len__() method.
# 
# The result is the total number of students.

# # Dataclasses
# 
# ### Definition
# 
# A dataclass is a special type of class used to store data easily with less code.
# 
# It automatically provides useful methods such as __init__() and __repr__().
# 
# ### Real-World Example
# 
# A student record contains details like name and age. A dataclass makes it easy to create and store these details.
# 
# ### Implementation
# 
# The following program creates a Student dataclass.
# 
# ### Explanation
# 
# @dataclass automatically creates the constructor and other useful methods for the Student class.

# In[42]:


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int


student = Student("Rahul", 22)

print(student)


# ### Program Explanation
# 
# Student is created using the @dataclass decorator.
# 
# The dataclass automatically creates the __init__() method.
# 
# We can create the student object directly by providing the name and age.

# # Singleton Pattern
# 
# ### Definition
# 
# Singleton Pattern ensures that only one object of a class is created during the program.
# 
# ### Real-World Example
# 
# A company may have one main database connection shared by different parts of an application.
# 
# ### Implementation
# 
# The following program creates only one object of the class.
# 
# ### Explanation
# 
# The class stores the first created object and returns the same object when another object is requested.

# In[44]:


class Database:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


db1 = Database()
db2 = Database()

print(db1 is db2)


# ### Program Explanation
# 
# _db1 and db2 are created from the Database class.
# 
# The __new__() method ensures that only one object is created.
# 
# db1 is db2 returns True because both variables refer to the same object.

# In[ ]:




