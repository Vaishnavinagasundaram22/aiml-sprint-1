#!/usr/bin/env python
# coding: utf-8

# <h1>Variables</h1>
# 
# <h3>Definition</h3>
# 
# <p>A variable is a name used to store a value in Python.</p>
# 
# <p>The value of a variable can be changed when needed.</p>
# 
# <p>It is like a box that stores some information.</p>
# 
# <h3>Why do we use Variables?</h3>
# 
# <p>Variables are used to store and use data easily.</p>
# 
# <p>We can use the variable name instead of writing the value again.</p>
# 
# <h3>Real-World Example</h3>
# 
# <ul>
# <li>name → Preethi</li>
# <li>age → 24</li>
# <li>city → Chennai</li>
# </ul>
# 
# <p>Here, each variable stores one piece of information.</p>
# 
# 
# <h3>Implementation</h3>
# 
# <p>This program stores and displays student information.</p>

# In[1]:


name = "Preethi"
age = 24
city = "Chennai"

print(name)
print(age)
print(city)


# <h1>Data Types</h1>
# 
# <h3>Definition</h3>
# 
# <p>A data type tells what kind of value is stored in a variable.</p>
# 
# <h3>Types of Data Types</h3>
# 
# <ul>
# <li><b>int</b> → Used to store whole numbers.</li>
# <li><b>float</b> → Used to store decimal numbers.</li>
# <li><b>str</b> → Used to store text or characters.</li>
# <li><b>bool</b> → Used to store True or False values.</li>
# </ul>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi's age can be int, mark can be float, name can be str and result can be bool.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program shows different data types.</p>

# In[2]:


name = "Preethi"
age = 24
mark = 85.5
passed = True

print(name)
print(age)
print(mark)
print(passed)


# <h1>Type Casting</h1>
# 
# <h3>Definition</h3>
# 
# <p>Type casting means changing one data type into another data type.</p>
# 
# <h3>Why do we use Type Casting?</h3>
# 
# <p>It is used when we need to change a value from one data type to another.</p>
# 
# <h3>Types of Type Casting</h3>
# 
# <ul>
# <li><b>int()</b> → Converts a value into an integer.</li>
# <li><b>float()</b> → Converts a value into a float.</li>
# <li><b>str()</b> → Converts a value into a string.</li>
# <li><b>bool()</b> → Converts a value into a boolean.</li>
# </ul>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi enters her age as text, so we can convert it into an integer for calculations.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program converts a string value into an integer.</p>

# In[1]:


age = "24"

print(type(age))

age = int(age)

print(type(age))
print(age)


# <h1>Operators</h1>
# 
# <h3>Definition</h3>
# 
# <p>Operators are symbols used to perform operations on values.</p>
# 
# <h3>Types of Operators</h3>
# 
# <ul>
# <li><b>Arithmetic Operators</b> → Used for calculations.</li>
# <li><b>Comparison Operators</b> → Used to compare two values.</li>
# <li><b>Logical Operators</b> → Used to combine conditions.</li>
# <li><b>Assignment Operators</b> → Used to assign values to variables.</li>
# </ul>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi has 50 marks and gets 20 more marks.</p>
# 
# <p>We can use the + operator to find her total marks.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program demonstrates arithmetic and comparison operators.</p>

# In[2]:


marks = 50
extra_marks = 20

total = marks + extra_marks

print("Total Marks:", total)
print("Is total greater than 60?", total > 60)


# <h1>Input and Output</h1>
# 
# <h3>Definition</h3>
# 
# <p>Input means giving data to a Python program.</p>
# 
# <p>Output means displaying the result from the program.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi enters her age as input and the program displays her age as output.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program gets the age from the user and displays it.</p>

# In[3]:


name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)


# <h1>Comments</h1>
# 
# <h3>Definition</h3>
# 
# <p>Comments are notes written in a Python program.</p>
# 
# <p>Python does not execute comments.</p>
# 
# <h3>Types of Comments</h3>
# 
# <ul>
# <li><b>Single-line Comment</b> → Uses the # symbol.</li>
# <li><b>Multi-line Comment</b> → Can be written using triple quotes.</li>
# </ul>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi writes a note near her code to remember what the code does.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program shows how comments are used in Python.</p>

# In[5]:


# Store student name
name = "Preethi"

# Display student name
print(name)


# <h1>if / elif / else</h1>
# 
# <h3>Definition</h3>
# 
# <p>if, elif and else are used to make decisions in Python.</p>
# 
# <p>if checks the first condition.</p>
# 
# <p>elif checks another condition.</p>
# 
# <p>else runs when all conditions are false.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi's mark is checked to find whether she passed or failed.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program checks the student's mark.</p>

# In[6]:


mark = 75

if mark >= 90:
    print("Grade A")
elif mark >= 50:
    print("Pass")
else:
    print("Fail")


# <h1>for Loop</h1>
# 
# <h3>Definition</h3>
# 
# <p>A for loop is used to repeat a block of code for each item in a sequence.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi checks the names of students one by one.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program prints student names one by one.</p>

# In[8]:


students = ["Preethi", "Divya", "Keerthana"]

for name in students:
    print(name)


# <h1>while Loop</h1>
# 
# <h3>Definition</h3>
# 
# <p>A while loop repeats the code as long as the condition is True.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi keeps studying while the exam is not completed.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program prints numbers from 1 to 5.</p>

# In[9]:


i = 1

while i <= 5:
    print(i)
    i += 1


# <h1>break</h1>
# 
# <h3>Definition</h3>
# 
# <p>break is used to stop a loop immediately.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi is searching for a student and stops searching when the student is found.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program stops the loop when it finds Preethi.</p>

# In[10]:


students = ["Divya", "Keerthana", "Preethi", "Anu"]

for name in students:
    if name == "Preethi":
        print("Preethi found")
        break


# <h1>continue</h1>
# 
# <h3>Definition</h3>
# 
# <p>continue is used to skip the current iteration and move to the next iteration.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi skips one student and continues checking the other students.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program skips the name Preethi and prints the other names.</p>

# In[12]:


students = ["Divya", "Preethi", "Keerthana", "Anu"]

for name in students:
    if name == "Preethi":
        continue
    print(name)


# <h1>pass</h1>
# 
# <h3>Definition</h3>
# 
# <p>pass is used as a placeholder when we do not want to write any code.</p>
# 
# <h3>Real-World Example</h3>
# 
# <p>Preethi leaves a task for later and continues with the program.</p>
# 
# <h3>Implementation</h3>
# 
# <p>This program uses pass when no action is needed.</p>

# In[13]:


name = "Preethi"

if name == "Preethi":
    pass

print("Program completed")


# # Collections
# 
# ### Definition
# 
# Collections are used to store multiple values in a single variable.
# 
# Python has four main collection types:
# 
# - List – Ordered and mutable
# - Tuple – Ordered and immutable
# - Set – Unordered and unique
# - Dictionary – Key-value pairs
# 
# ### Real-World Example
# 
# A shopping basket stores multiple items in one place. Similarly, collections store multiple values in one variable.
# 
# ### Implementation
# 
# The following program stores multiple student names using a collection.

# In[15]:


students = ["Aishu", "Brindha", "Celine", "Divya"]

print(students)


# # List
# 
# ### Definition
# 
# A list is an ordered and mutable collection used to store multiple values. It allows duplicate values and its items can be changed.
# 
# ### Real-World Example
# 
# A shopping list contains items that can be added, removed, or changed.
# 
# ### Implementation
# 
# The following program creates a list of student names and adds a new student.

# In[16]:


students = ["Aishu", "Brindha", "Celine", "Divya"]

students.append("Arthi")

print(students)


# # Tuple
# 
# ### Definition
# 
# A tuple is an ordered and immutable collection used to store multiple values. Once created, its values cannot be changed.
# 
# ### Real-World Example
# 
# A person's date of birth does not normally change. Similarly, tuple values cannot be modified.
# 
# ### Implementation
# 
# The following program creates a tuple and accesses its values.

# In[17]:


fruits = ("Apple", "Banana", "Mango")

print(fruits)
print(fruits[0])


# # Set
# 
# ### Definition
# 
# A set is an unordered collection that stores unique values. It automatically removes duplicate values.
# 
# ### Real-World Example
# 
# If a class has students with repeated names, a set can be used to keep only unique names.
# 
# ### Implementation
# 
# The following program stores numbers with duplicate values in a set.

# In[18]:


numbers = {1, 2, 2, 3, 4, 4}

print(numbers)


# # Dictionary
# 
# ### Definition
# 
# A dictionary stores data as key-value pairs. Each key is used to access its corresponding value.
# 
# ### Real-World Example
# 
# A student record can have a name, age, and city. The field name is the key and the stored information is the value.
# 
# ### Implementation
# 
# The following program stores student details using a dictionary.

# In[19]:


student = {
    "name": "Vaishu",
    "age": 24,
    "city": "Chennai"
}

print(student)
print(student["name"])


# # List Comprehension
# 
# ### Definition
# 
# List comprehension is a short way to create a new list using a loop and optional condition in a single line.
# 
# ### Real-World Example
# 
# A teacher wants to create a list of students who passed an exam. Instead of checking and adding each student separately, the required students can be selected directly.
# 
# ### Implementation
# 
# The following program creates a list containing the squares of numbers.

# In[20]:


numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)


# # Dictionary Comprehension
# 
# ### Definition
# 
# Dictionary comprehension is a short way to create a new dictionary using a loop and optional condition in a single line.
# 
# ### Real-World Example
# 
# A teacher wants to create a dictionary containing each student's name and marks. Dictionary comprehension can create these key-value pairs in a simple way.
# 
# ### Implementation
# 
# The following program creates a dictionary containing numbers and their squares.

# In[21]:


numbers = [1, 2, 3, 4, 5]

squares = {num: num * num for num in numbers}

print(squares)


# # Function Definition
# 
# ### Definition
# 
# A function is a reusable block of code that performs a specific task. It helps avoid writing the same code multiple times.
# 
# ### Real-World Example
# 
# A calculator has a button for addition. Whenever we press it, the same addition operation is performed.
# 
# ### Implementation
# 
# The following program defines a function to add two numbers.

# In[22]:


def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print(result)


# # Arguments
# 
# ### Definition
# 
# Arguments are the values passed to a function when it is called. They provide input to the function.
# 
# ### Real-World Example
# 
# When ordering food, we give our food choice to the restaurant. Similarly, arguments give input to a function.
# 
# ### Implementation
# 
# The following program passes two numbers as arguments to a function.

# In[23]:


def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print(result)


# # Default Arguments
# 
# ### Definition
# 
# A default argument is a value given to a function parameter when the function is defined. If no value is passed, Python uses the default value.
# 
# ### Real-World Example
# 
# A restaurant may have a standard quantity of rice. If the customer does not specify the quantity, the standard quantity is used.
# 
# ### Implementation
# 
# The following program uses a default value for the `city` parameter.

# In[24]:


def student_details(name, city="Chennai"):
    print(name, city)

student_details("vaishu")
student_details("kesavarthini", "Madurai")


# # Keyword Arguments
# 
# ### Definition
# 
# Keyword arguments are arguments passed to a function using the parameter name. They allow us to provide values in any order.
# 
# ### Real-World Example
# 
# When filling an application form, we enter information under specific labels such as Name, Age, and City.
# 
# ### Implementation
# 
# The following program passes values using parameter names.

# In[25]:


def student_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student_details(age=24, city="Chennai", name="vaishu")


# # Variable-Length Arguments (*args)
# 
# ### Definition
# 
# `*args` allows a function to accept any number of positional arguments. It is useful when we do not know how many values will be passed.
# 
# ### Real-World Example
# 
# A teacher may have different numbers of students in different classes. The function can accept any number of student names.
# 
# ### Implementation
# 
# The following program accepts multiple student names using `*args`.

# In[26]:


def students(*args):
    for name in args:
        print(name)

students("Aishu", "Brindha", "Celine", "Divya")


# # Variable-Length Arguments (**kwargs)
# 
# ### Definition
# 
# `**kwargs` allows a function to accept any number of keyword arguments. The arguments are stored as key-value pairs in a dictionary.
# 
# ### Real-World Example
# 
# A student registration form may contain different details such as name, age, city, and course.
# 
# ### Implementation
# 
# The following program accepts multiple student details using `**kwargs`.

# In[27]:


def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Rahul", age=22, city="Chennai", course="Python")


# # Lambda Functions
# 
# ### Definition
# 
# A lambda function is a small anonymous function written in a single line. It is mainly used for simple operations.
# 
# ### Real-World Example
# 
# A calculator quickly performs a simple calculation when we give it numbers. Similarly, a lambda function performs a simple operation quickly.
# 
# ### Implementation
# 
# The following program uses a lambda function to calculate the square of a number.

# In[28]:


square = lambda x: x * x

print(square(5))


# # Recursive Functions
# 
# ### Definition
# 
# A recursive function is a function that calls itself to solve a problem. It continues until a condition called the base condition is reached.
# 
# ### Real-World Example
# 
# Imagine standing between two mirrors. The reflection appears again and again. Similarly, a recursive function calls itself repeatedly until the stopping condition is reached.
# 
# ### Implementation
# 
# The following program calculates the factorial of a number using recursion.

# In[30]:


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# # Iterators
# 
# ### Definition
# 
# An iterator is an object used to access elements one at a time. It uses `iter()` to create an iterator and `next()` to get the next value.
# 
# ### Real-World Example
# 
# A teacher checks students one by one from an attendance list. Each student is accessed one at a time.
# 
# ### Implementation
# 
# The following program accesses list elements one by one using an iterator.

# In[31]:


students = ["Rahul", "Priya", "Arun"]

students_iterator = iter(students)

print(next(students_iterator))
print(next(students_iterator))
print(next(students_iterator))


# # Generators
# 
# ### Definition
# 
# A generator is a special type of function that produces values one at a time instead of storing all values in memory at once.
# 
# ### Real-World Example
# 
# A ticket counter gives one ticket to each person when their turn comes instead of giving all tickets at once.
# 
# ### Implementation
# 
# The following program generates numbers one at a time.

# In[32]:


def numbers():
    for i in range(1, 4):
        yield i

for num in numbers():
    print(num)


# # yield
# 
# ### Definition
# 
# `yield` is used in a generator function to return a value one at a time. It pauses the function and continues from the same place when the next value is requested.
# 
# ### Real-World Example
# 
# A teacher gives students their certificates one by one instead of giving all certificates at once.
# 
# ### Implementation
# 
# The following program uses `yield` to generate numbers one at a time.

# In[33]:


def numbers():
    yield 10
    yield 20
    yield 30

for num in numbers():
    print(num)


# # Decorators
# 
# ### Definition
# 
# A decorator is a function that adds extra functionality to another function without changing its original code.
# 
# ### Real-World Example
# 
# A gift wrapper adds an extra layer to a gift without changing the gift itself.
# 
# ### Implementation
# 
# The following program uses a decorator to display a message before and after a function runs.

# In[34]:


def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()


# # Closures
# 
# ### Definition
# 
# A closure is a function that remembers and can access variables from its outer function even after the outer function has finished executing.
# 
# ### Real-World Example
# 
# A person remembers information given by a teacher even after leaving the classroom. Similarly, a closure remembers values from its outer function.
# 
# ### Implementation
# 
# The following program demonstrates a closure using a number from the outer function.

# In[36]:


def outer_function(number):
    def inner_function():
        print(number)
    return inner_function

result = outer_function(10)

result()


# # global
# 
# ### Definition
# 
# The `global` keyword is used to access and modify a variable defined outside a function.
# 
# ### Real-World Example
# 
# A school notice board is accessible to all teachers. Similarly, a global variable can be accessed from different parts of a program.
# 
# ### Implementation
# 
# The following program modifies a global variable inside a function.

# In[37]:


count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)


# # nonlocal
# 
# ### Definition
# 
# The `nonlocal` keyword is used to modify a variable from an outer function inside a nested function.
# 
# ### Real-World Example
# 
# A team member can update a value maintained by their team leader. Similarly, a nested function can modify a variable from its outer function.
# 
# ### Implementation
# 
# The following program modifies an outer function's variable using `nonlocal`.

# In[38]:


def outer_function():
    count = 10

    def inner_function():
        nonlocal count
        count = 20

    inner_function()
    print(count)

outer_function()


# # Modules
# 
# ### Definition
# 
# A module is a Python file that contains functions, variables, or classes that can be reused in another Python program.
# 
# ### Real-World Example
# 
# A toolbox contains different tools that can be used whenever needed. Similarly, a module contains reusable Python code.
# 
# ### Implementation
# 
# The following program imports and uses a function from a module.

# In[ ]:


def add(a, b):
    return a + b
import calculator

result = calculator.add(10, 20)

print(result)


# # Packages
# 
# ### Definition
# 
# A package is a collection of related Python modules organized in a folder.
# 
# ### Real-World Example
# 
# A library has different sections for different subjects. Similarly, a package contains related modules in one folder.
# 
# ### Implementation
# 
# The following program imports a package and uses one of its modules.

# In[43]:


import math

print(math.sqrt(16))
print(math.factorial(5))


# # Virtual Environments
# 
# ### Definition
# 
# A virtual environment is an isolated Python environment used to install and manage packages separately for a project.
# 
# ### Real-World Example
# 
# Different projects may need different versions of the same tool. A separate workspace keeps each project's requirements independent.
# 
# ### Implementation
# 
# The following command creates a virtual environment named `myenv`.

# In[44]:


import venv

venv.create("myenv")

print("Virtual environment created")


# # Type Hinting
# 
# ### Definition
# 
# Type hinting is used to specify the expected data type of variables, function parameters, and return values. It improves code readability and understanding.
# 
# ### Real-World Example
# 
# A form may specify that an age field should contain a number. Similarly, type hints show what type of data a function expects.
# 
# ### Implementation
# 
# The following program uses type hints for function parameters and the return value.

# In[47]:


def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(10, 20)

print(result)


# # map()
# 
# ### Definition
# 
# `map()` applies a function to every item in an iterable and returns the transformed values.
# 
# ### Real-World Example
# 
# A teacher applies the same calculation to every student's mark. Similarly, `map()` applies the same function to each item.
# 
# ### Implementation
# 
# The following program doubles each number using `map()`.

# In[48]:


numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)


# # filter()
# 
# ### Definition
# 
# `filter()` is used to select items from an iterable based on a condition. It returns only the items for which the condition is True.
# 
# ### Real-World Example
# 
# A teacher selects only students who scored above 50 marks. Similarly, `filter()` selects only the values that satisfy a condition.
# 
# ### Implementation
# 
# The following program selects even numbers from a list.

# In[49]:


numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# # zip()
# 
# ### Definition
# 
# `zip()` combines elements from two or more iterables based on their position.
# 
# ### Real-World Example
# 
# A teacher has one list of student names and another list of marks. `zip()` can pair each student with their corresponding mark.
# 
# ### Implementation
# 
# The following program combines student names with their marks.

# In[50]:


names = ["Rahul", "Priya", "Arun"]
marks = [85, 90, 78]

result = list(zip(names, marks))

print(result)


# # enumerate()
# 
# ### Definition
# 
# `enumerate()` adds an index number to each item in an iterable while looping through it.
# 
# ### Real-World Example
# 
# A teacher gives a roll number to each student in the attendance list. Similarly, `enumerate()` provides an index for each item.
# 
# ### Implementation
# 
# The following program displays the index and name of each student.

# In[51]:


students = ["Rahul", "Priya", "Arun"]

for index, name in enumerate(students):
    print(index, name)


# # sorted()
# 
# ### Definition
# 
# `sorted()` is a built-in function used to return the items of an iterable in sorted order. It creates a new sorted list without changing the original data.
# 
# ### Real-World Example
# 
# A teacher arranges student names in alphabetical order. Similarly, `sorted()` arranges values in order.
# 
# ### Implementation
# 
# The following program sorts student names alphabetically.

# In[52]:


students = ["Rahul", "Arun", "Priya", "Karthik"]

result = sorted(students)

print(result)


# # any()
# 
# ### Definition
# 
# any() returns True if at least one item in a collection satisfies the condition.
# 
# ### Real-World Example
# 
# If at least one student passes the exam, the teacher can say that at least one student passed.
# 
# ### Implementation
# 
# The following program checks whether at least one mark is above 50.
# 
# ### Explanation
# 
# any() checks all the marks. If at least one mark is above 50, it returns True.

# In[53]:


marks = [35, 42, 65, 40]

result = any(mark > 50 for mark in marks)

print(result)


# # all()
# 
# ### Definition
# 
# all() returns True only if all items in a collection satisfy the condition.
# 
# ### Real-World Example
# 
# If all students pass the exam, the teacher can say that every student passed.
# 
# ### Implementation
# 
# The following program checks whether all marks are above 50.
# 
# ### Explanation
# 
# all() checks every mark. If all marks satisfy the condition, it returns True.

# In[54]:


marks = [65, 72, 80, 90]

result = all(mark > 50 for mark in marks)

print(result)


# # isinstance()
# 
# ### Definition
# 
# isinstance() checks whether a value belongs to a particular data type.
# 
# ### Real-World Example
# 
# A teacher checks whether a student's age is a number.
# 
# ### Implementation
# 
# The following program checks whether the given value is an integer.
# 
# ### Explanation
# 
# isinstance() checks the value and returns True if it belongs to the specified data type.

# In[55]:


age = 25

result = isinstance(age, int)

print(result)


# # id()
# 
# ### Definition
# 
# id() returns the unique identity number of an object in Python.
# 
# ### Real-World Example
# 
# A student has a unique ID number to identify them. Similarly, Python gives each object a unique identity.
# 
# ### Implementation
# 
# The following program displays the identity of a variable.
# 
# ### Explanation
# 
# id() returns the unique identity number of the object stored in the variable.

# In[56]:


name = "Rahul"

result = id(name)

print(result)


# In[ ]:




