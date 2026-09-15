#!/usr/bin/env python
# coding: utf-8

# # Exception Handling
# 
# ### Definition
# 
# Exception Handling is a way of handling errors that occur while a Python program is running.
# 
# It prevents the program from stopping suddenly and allows us to handle the error properly.
# 
# ### Real-World Example
# 
# If a person enters an invalid value in a form, the system shows an error message instead of completely stopping.
# 
# Similarly, Python uses Exception Handling to handle errors during program execution.
# 
# ### Implementation
# 
# The following program handles an error using try and except.
# 
# ### Explanation
# 
# The program tries to perform a division. If division by zero occurs, the error is handled using except.

# # try
# 
# ### Definition
# 
# try is used to write code that may cause an exception.
# 
# It tells Python to try running the code inside the block.
# 
# ### Real-World Example
# 
# Before opening a file, we are not sure whether the file exists. So, we can place the file operation inside a try block.
# 
# ### Implementation
# 
# The following program uses a try block to perform a division operation.
# 
# ### Explanation
# 
# The code inside the try block is executed normally.
# 
# If an exception occurs, Python looks for a suitable way to handle that exception.

# In[2]:


try:
    number = 10
    result = number / 0
    print(result)


# ### Program Explanation
# 
# In this program, 10 is divided by 0.
# 
# This causes a ZeroDivisionError.
# 
# The division code is placed inside the try block because it is the code that may cause an exception.

# # except
# 
# ### Definition
# 
# except is used to handle an exception that occurs inside the try block.
# 
# It prevents the program from stopping when an expected error occurs.
# 
# ### Real-World Example
# 
# If a calculator gets a division by zero, instead of stopping the program, it can display a proper error message.
# 
# ### Implementation
# 
# The following program handles a ZeroDivisionError using except.
# 
# ### Explanation
# 
# The try block contains the code that may cause an error. The except block handles the error and displays a message.

# In[3]:


try:
    number = 10
    result = number / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# ### Program Explanation
# 
# The try block attempts to divide 10 by 0.
# 
# This causes a ZeroDivisionError.
# 
# The except block catches the error and displays a proper message instead of stopping the program.

# # else
# 
# ### Definition
# 
# else is used with try and except. It runs only when no exception occurs in the try block.
# 
# ### Real-World Example
# 
# If a payment is completed without any error, the system shows a success message.
# 
# ### Implementation
# 
# The following program uses else when the division is successful.
# 
# ### Explanation
# 
# The try block runs successfully without an error, so the else block is executed.

# In[5]:


try:
    number = 10
    result = number / 2
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division completed successfully")


# ### Program Explanation
# 
# The try block successfully divides 10 by 2.
# 
# Since no exception occurs, the except block is skipped.
# 
# The else block runs and displays the success message.

# # finally
# 
# ### Definition
# 
# finally is used with try and except. It always runs whether an exception occurs or not.
# 
# ### Real-World Example
# 
# After using a file, the file should be closed whether the operation succeeds or fails.
# 
# ### Implementation
# 
# The following program uses finally after handling an exception.
# 
# ### Explanation
# 
# The finally block runs after the try and except blocks, regardless of whether an error occurs.

# In[7]:


try:
    number = 10
    result = number / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")


# ### Program Explanation
# 
# The try block causes a ZeroDivisionError.
# 
# The except block handles the error.
# 
# The finally block runs after that, even though an exception occurred.

# # raise
# 
# ### Definition
# 
# raise is used to manually create an exception in Python.
# 
# It is used when we want to stop the program or show an error based on a specific condition.
# 
# ### Real-World Example
# 
# If a person tries to withdraw more money than their account balance, the system can raise an error message.
# 
# ### Implementation
# 
# The following program raises an error when the age is less than 18.
# 
# ### Explanation
# 
# The raise statement manually creates a ValueError when the given age is below 18.

# In[8]:


age = 16

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")


# ### Program Explanation
# 
# The program checks whether the age is below 18.
# 
# If the condition is true, raise creates a ValueError with a custom message.
# 
# The program stops at the raise statement because the condition is not satisfied.

# # assert
# 
# ### Definition
# 
# assert is used to check whether a condition is true.
# 
# If the condition is false, Python raises an AssertionError.
# 
# ### Real-World Example
# 
# Before allowing a student to attend an exam, we can check whether the student has completed the required registration.
# 
# ### Implementation
# 
# The following program checks whether the student has completed registration.
# 
# ### Explanation
# 
# The assert statement checks the condition. If registration is False, an AssertionError occurs.

# In[9]:


registered = False

assert registered, "Student is not registered"

print("Student can attend the exam")


# ### Program Explanation
# 
# The registered value is False.
# 
# The assert statement checks this condition.
# 
# Since the condition is False, Python raises an AssertionError with the given message.

# # Custom Exceptions
# 
# ### Definition
# 
# A custom exception is an exception created by the programmer for a specific situation.
# 
# It is created by defining a new class that inherits from Exception.
# 
# ### Real-World Example
# 
# A bank can create a specific error called InsufficientBalanceError when a customer tries to withdraw more money than available.
# 
# ### Implementation
# 
# The following program creates and uses a custom exception.
# 
# ### Explanation
# 
# InsufficientBalanceError is a custom exception created for a specific banking situation.

# In[11]:


class InsufficientBalanceError(Exception):
    pass


balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")

    print("Withdrawal successful")

except InsufficientBalanceError as error:
    print(error)


# ### Program Explanation
# 
# InsufficientBalanceError is a custom exception created by the programmer.
# 
# When the withdrawal amount is greater than the balance, the custom exception is raised.
# 
# The except block handles the custom exception and displays the error message.

# # ValueError
# 
# ### Definition
# 
# ValueError occurs when a function receives a value of the correct type but an invalid value.
# 
# ### When It Occurs
# 
# It commonly occurs when we try to convert an invalid value into another data type.
# 
# ### Implementation
# 
# The following program tries to convert text into an integer.
# 
# ### Explanation
# 
# "hello" is a string, but it cannot be converted into an integer, so Python raises a ValueError.

# # IndexError
# 
# ### Definition
# 
# IndexError occurs when we try to access an index that does not exist in a list or sequence.
# 
# ### When It Occurs
# 
# It commonly occurs when the given index is outside the available range.
# 
# ### Implementation
# 
# The following program tries to access an unavailable list index.
# 
# ### Explanation
# 
# The list has only 3 items, but index 5 does not exist, so Python raises an IndexError.

# In[12]:


try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index does not exist in the list")


# ### Program Explanation
# 
# In this program, the list contains only 3 items.
# 
# The program tries to access index 5, which is not available.
# 
# So, Python raises an IndexError.
# 
# The except block handles the error and displays a proper message.

# # KeyError
# 
# ### Definition
# 
# KeyError occurs when we try to access a dictionary key that does not exist.
# 
# ### When It Occurs
# 
# It commonly occurs when the given key is not available in the dictionary.
# 
# ### Implementation
# 
# The following program tries to access a key that is not present in the dictionary.
# 
# ### Explanation
# 
# The dictionary does not contain the key "city", so Python raises a KeyError.

# In[13]:


try:
    student = {
        "name": "Rahul",
        "age": 22
    }

    print(student["city"])

except KeyError:
    print("Key does not exist in the dictionary")


# ### Program Explanation
# 
# In this program, the dictionary contains the keys "name" and "age".
# 
# The program tries to access the "city" key, which is not available.
# 
# So, Python raises a KeyError.
# 
# The except block handles the error and displays a proper message.

# # AttributeError
# 
# ### Definition
# 
# AttributeError occurs when we try to access an attribute or method that does not exist for an object.
# 
# ### When It Occurs
# 
# It commonly occurs when we use an incorrect attribute or method name.
# 
# ### Implementation
# 
# The following program tries to access an attribute that does not exist.
# 
# ### Explanation
# 
# The Student object does not have a `city` attribute, so Python raises an AttributeError.

# In[15]:


class Student:
    def __init__(self, name):
        self.name = name

try:
    student = Student("Rahul")
    print(student.city)

except AttributeError:
    print("Attribute does not exist")


# ### Program Explanation
# 
# In this program, the Student object has only the `name` attribute.
# 
# The program tries to access the `city` attribute, which does not exist.
# 
# So, Python raises an AttributeError.
# 
# The except block handles the error and displays a proper message.

# # NameError
# 
# ### Definition
# 
# NameError occurs when we try to use a variable or name that has not been defined.
# 
# ### When It Occurs
# 
# It commonly occurs when we use a variable before creating it or use an incorrect variable name.
# 
# ### Implementation
# 
# The following program tries to print a variable that is not defined.
# 
# ### Explanation
# 
# The variable `name` is not created before it is used, so Python raises a NameError.

# In[16]:


try:
    print(name)

except NameError:
    print("Variable is not defined")


# ### Program Explanation
# 
# In this program, the variable `name` is not defined.
# 
# The program tries to use the variable before creating it.
# 
# So, Python raises a NameError.
# 
# The except block handles the error and displays a proper message.

# # FileNotFoundError
# 
# ### Definition
# 
# FileNotFoundError occurs when Python tries to open a file that does not exist.
# 
# ### When It Occurs
# 
# It commonly occurs when the file name or file path is incorrect.
# 
# ### Implementation
# 
# The following program tries to open a file that does not exist.
# 
# ### Explanation
# 
# The file is not available in the given path, so Python raises a FileNotFoundError.

# In[17]:


try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")


# ### Program Explanation
# 
# In this program, Python tries to open the `student.txt` file.
# 
# If the file does not exist, Python raises a FileNotFoundError.
# 
# The except block handles the error and displays a proper message.

# # ZeroDivisionError
# 
# ### Definition
# 
# ZeroDivisionError occurs when we try to divide a number by zero.
# 
# ### When It Occurs
# 
# It commonly occurs when the denominator in a division operation is zero.
# 
# ### Implementation
# 
# The following program tries to divide a number by zero.
# 
# ### Explanation
# 
# A number cannot be divided by zero, so Python raises a ZeroDivisionError.

# In[19]:


try:
    number = 10
    result = number / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# ### Program Explanation
# 
# In this program, 10 is divided by 0.
# 
# Division by zero is not allowed in Python.
# 
# So, Python raises a ZeroDivisionError.
# 
# The except block handles the error and displays a proper message.

# # ImportError
# 
# ### Definition
# 
# ImportError occurs when Python cannot import a required name or item from a module.
# 
# ### When It Occurs
# 
# It commonly occurs when the required function or class is not available in the module.
# 
# ### Implementation
# 
# The following program tries to import a function that does not exist in the `math` module.
# 
# ### Explanation
# 
# The `math` module does not contain `hello_function`, so Python raises an ImportError.

# In[21]:


try:
    from math import hello_function
    print(hello_function())

except ImportError:
    print("The required item cannot be imported")


# ### Program Explanation
# 
# In this program, the program tries to import `hello_function` from the `math` module.
# 
# The function does not exist in that module.
# 
# So, Python raises an ImportError.
# 
# The except block handles the error and displays a proper message.

# # ModuleNotFoundError
# 
# ### Definition
# 
# ModuleNotFoundError occurs when Python cannot find the module that we try to import.
# 
# ### When It Occurs
# 
# It commonly occurs when the module is not installed or the module name is incorrect.
# 
# ### Implementation
# 
# The following program tries to import a module that does not exist.
# 
# ### Explanation
# 
# The module `student_module` is not available, so Python raises a ModuleNotFoundError.

# In[22]:


try:
    import student_module
    print("Module imported successfully")

except ModuleNotFoundError:
    print("Module not found")


# ### Program Explanation
# 
# In this program, Python tries to import the `student_module`.
# 
# The module is not available in the Python environment.
# 
# So, Python raises a ModuleNotFoundError.
# 
# The except block handles the error and displays a proper message.

# In[ ]:




