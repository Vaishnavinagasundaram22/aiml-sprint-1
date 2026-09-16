#!/usr/bin/env python
# coding: utf-8

# # File Handling
# 
# ### Definition
# 
# File handling is used to create, read, write, and manage files using Python.
# 
# ### Why It Is Used
# 
# It helps us store and retrieve data permanently from files.
# 
# ### Real-World Example
# 
# A student management system can store student details in a file and read them whenever needed.
# 
# ### Implementation
# 
# The following program creates a file and writes student information into it.
# 
# ### Explanation
# 
# The `open()` function is used to open a file, and the `write()` method is used to add data.

# In[1]:


file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Age: 22")

file.close()

print("Data written successfully")


# ### Program Explanation
# 
# The file is opened using `open()` in write mode.
# 
# The `write()` method stores student information in the file.
# 
# The `close()` method closes the file after writing.
# 
# This demonstrates how Python can store data in a file.

# # Text File
# 
# ### Definition
# 
# A text file is a file used to store data as plain text.
# 
# ### Why It Is Used
# 
# It is useful for storing simple information such as names, notes, and messages.
# 
# ### Real-World Example
# 
# A student application can store student details in a text file.
# 
# ### Implementation
# 
# The following program reads data from a text file.
# 
# ### Explanation
# 
# The `open()` function opens the file in read mode, and `read()` gets the stored text.

# In[2]:


file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# ### Program Explanation
# 
# The file is opened using `open()` in read mode.
# 
# The `read()` method reads the data from the file.
# 
# The `close()` method closes the file after reading.
# 
# This demonstrates how Python reads data from a text file.

# # CSV File
# 
# ### Definition
# 
# A CSV file stores data in rows and columns, with values separated by commas.
# 
# ### Why It Is Used
# 
# It is commonly used to store and exchange tabular data.
# 
# ### Real-World Example
# 
# A college can store student details such as name, age, and course in a CSV file.
# 
# ### Implementation
# 
# The following program creates a CSV file and writes student details into it.
# 
# ### Explanation
# 
# The `csv` module is used to write structured data into a CSV file.

# In[3]:


import csv

data = [
    ["Name", "Age", "Course"],
    ["Rahul", 22, "Python"],
    ["Priya", 21, "SQL"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully")


# ### Program Explanation
# 
# The `csv` module is imported to work with CSV files.
# 
# The data is stored in rows and columns.
# 
# `csv.writer()` writes the data into the CSV file.
# 
# `writerows()` writes all the rows into the file.

# # JSON File
# 
# ### Definition
# 
# A JSON file is used to store data in a structured format using key-value pairs.
# 
# ### Why It Is Used
# 
# JSON is commonly used to store and exchange data between applications.
# 
# ### Real-World Example
# 
# A student application can store student details such as name, age, and course in JSON format.
# 
# ### Implementation
# 
# The following program creates a JSON file and stores student details in it.
# 
# ### Explanation
# 
# The `json` module is used to convert Python data into JSON format and store it in a file.

# In[4]:


import json

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully")


# ### Program Explanation
# 
# The `json` module is imported to work with JSON files.
# 
# The student details are stored using key-value pairs.
# 
# `json.dump()` writes the Python data into the JSON file.
# 
# The `with` statement automatically closes the file.

# # Pickle
# 
# ### Definition
# 
# Pickle is a Python module used to store Python objects in a file.
# 
# ### Why It Is Used
# 
# It helps us save Python objects and use them again later.
# 
# ### Real-World Example
# 
# A Python application can save student details and load them later without creating the data again.
# 
# ### Implementation
# 
# The following program stores a Python dictionary in a pickle file.
# 
# ### Explanation
# 
# `pickle.dump()` stores the Python object in the file.

# In[5]:


import pickle

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print("Object saved successfully")


# ### Program Explanation
# 
# The `pickle` module is imported to work with Python objects.
# 
# The dictionary contains student details.
# 
# `pickle.dump()` saves the dictionary into the pickle file.
# 
# `wb` means the file is opened in binary write mode.

# # with Statement
# 
# ### Definition
# 
# The `with` statement is used to work with files safely.
# 
# ### Why It Is Used
# 
# It automatically closes the file after the required operation is completed.
# 
# ### Real-World Example
# 
# When we open a file to read student details, the `with` statement makes sure the file is properly closed after reading.
# 
# ### Implementation
# 
# The following program reads data from a text file using the `with` statement.
# 
# ### Explanation
# 
# The file is automatically closed when the `with` block finishes.

# In[6]:


with open("student.txt", "r") as file:
    data = file.read()
    print(data)

print("File closed automatically")


# ### Program Explanation
# 
# The `with` statement opens the file safely.
# 
# The `read()` method reads the file data.
# 
# After the `with` block finishes, Python automatically closes the file.
# 
# This avoids the need to call `file.close()` separately.

# # pathlib
# 
# ### Definition
# 
# `pathlib` is a Python module used to work with file and folder paths.
# 
# ### Why It Is Used
# 
# It makes it easier to create, find, check, and manage file paths.
# 
# ### Real-World Example
# 
# In a student application, `pathlib` can be used to check whether a student data file exists.
# 
# ### Implementation
# 
# The following program checks whether a file exists.
# 
# ### Explanation
# 
# `Path()` creates a path object, and `exists()` checks whether the file is available.

# In[7]:


from pathlib import Path

file_path = Path("student.txt")

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")


# ### Program Explanation
# 
# `Path()` creates a path for the file.
# 
# `exists()` checks whether the file is available.
# 
# If the file exists, the program displays `File exists`.
# 
# Otherwise, it displays `File does not exist`.

# # os Module
# 
# ### Definition
# 
# The `os` module is used to interact with the operating system.
# 
# ### Why It Is Used
# 
# It helps us work with files, folders, directories, and paths.
# 
# ### Real-World Example
# 
# A Python application can use the `os` module to check whether a folder exists.
# 
# ### Implementation
# 
# The following program checks whether a folder exists.
# 
# ### Explanation
# 
# `os.path.exists()` checks whether the given folder or path is available.

# In[8]:


import os

folder = "student_data"

if os.path.exists(folder):
    print("Folder exists")
else:
    print("Folder does not exist")


# ### Program Explanation
# 
# The `os` module is imported to work with the operating system.
# 
# `os.path.exists()` checks whether the given folder exists.
# 
# The program displays the result based on the folder availability.

# # shutil Module
# 
# ### Definition
# 
# The `shutil` module is used to perform file and folder operations.
# 
# ### Why It Is Used
# 
# It helps us copy, move, and delete files and folders.
# 
# ### Real-World Example
# 
# A company can use `shutil` to copy important files into a backup folder.
# 
# ### Implementation
# 
# The following program copies a file from one location to another.
# 
# ### Explanation
# 
# `shutil.copy()` creates a copy of the file in the destination location.

# In[9]:


import shutil

shutil.copy("student.txt", "student_backup.txt")

print("File copied successfully")


# ### Program Explanation
# 
# The `shutil` module is imported to work with files and folders.
# 
# `shutil.copy()` copies `student.txt` into `student_backup.txt`.
# 
# This demonstrates how Python can create a backup copy of a file.

# # File Validation
# 
# ### Definition
# 
# File validation means checking whether a file is valid and available before using it.
# 
# ### Why It Is Used
# 
# It helps prevent errors caused by missing files or incorrect file types.
# 
# ### Real-World Example
# 
# Before reading a student data file, an application can check whether the file exists and has the correct extension.
# 
# ### Implementation
# 
# The following program checks whether a file exists before reading it.
# 
# ### Explanation
# 
# The program validates the file using `Path.exists()` before opening it.

# In[10]:


from pathlib import Path

file_path = Path("student.txt")

if file_path.exists():
    print("File is valid and available")
else:
    print("File does not exist")


# ### Program Explanation
# 
# `Path()` creates the file path.
# 
# `exists()` checks whether the file is available.
# 
# If the file exists, the program considers it available for further processing.
# 
# This helps avoid file-related errors.

# # Directories
# 
# ### Definition
# 
# A directory is a folder used to organize files and other folders.
# 
# ### Why It Is Used
# 
# Directories help us store and manage related files in an organized way.
# 
# ### Real-World Example
# 
# A student application can have a `student_data` folder containing student files.
# 
# ### Implementation
# 
# The following program creates a directory if it does not already exist.
# 
# ### Explanation
# 
# `mkdir()` is used to create a new directory.

# In[11]:


from pathlib import Path

folder = Path("student_data")

if not folder.exists():
    folder.mkdir()
    print("Directory created")
else:
    print("Directory already exists")


# ### Program Explanation
# 
# `Path()` creates the path for the directory.
# 
# `exists()` checks whether the directory is already available.
# 
# `mkdir()` creates the directory if it does not exist.
# 
# This helps organize files into separate folders.

# In[ ]:




