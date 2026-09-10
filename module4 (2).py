#!/usr/bin/env python
# coding: utf-8

# <h2>What is Exception Handling?</h2>
# 
# <p><strong>Exception handling</strong> is a mechanism used to handle errors that occur during the execution of a Python program without stopping the entire program.</p>
# 
# 
# <h3>Why is Exception Handling Used?</h3>
# 
# <p><strong>Exception handling</strong>  is used to prevent unexpected program termination and handle errors in a controlled way.</p>
# 
# <h3>Keywords Used in Exception Handling</h3>
# 
# <p><strong>try</strong> - Contains the code that may cause an error.</p>
# 
# <p><strong>except</strong> - Handles the error when an exception occurs.</p>
# 
# <p><strong>else</strong> - Runs when no exception occurs.</p>
# 
# <p><strong>finally</strong> - Runs whether an exception occurs or not.</p>
# 
# <p><strong>raise</strong> - Used to manually generate an exception.</p>

# In[3]:


class InvalidFileException(Exception):
    pass


# <h3>Code Explanation</h3>
# 
# 
# 
# <p><strong>def</strong> is used to create a function. <strong>validate_file</strong> is the function name, and <strong>file_name</strong> is the input parameter.</p>
# 
# 
# <p>The <strong>try</strong> block contains the code that may cause an exception.</p>
# 
# <p>This checks whether the file name does not end with <strong>.csv</strong>. If the file is not a CSV file, the condition becomes true.</p>
# 
# 
# <p><strong>raise</strong> is used to manually generate an exception. Here, the custom exception <strong>InvalidFileException</strong> is raised when the file format is invalid.</p>
# 
# 
# <p>This message is displayed when the file has a valid <strong>.csv</strong> format.</p>

# In[8]:


def validate_file(file_name):
    try:
        if not file_name.endswith(".csv"):
            raise InvalidFileException("Invalid file format")

        print("File format is valid")

    except InvalidFileException as error:
        print("Error:", error)

    finally:
        print("File validation completed")


validate_file("data.csv")
validate_file("data.exe")


# <p><strong>except InvalidFileException as error:</strong> Handles the custom exception and stores the error message in the variable <strong>error</strong>.</p>
# 
# <p><strong>print("Error:", error):</strong> Prints the error message when an invalid file format is found.</p>
# 
# <p><strong>finally:</strong> Executes the code inside it whether an exception occurs or not.</p>
# 
# <p><strong>print("File validation completed"):</strong> Displays a message after the file validation process is completed.</p>
# 
# <p><strong>validate_file("data.csv"):</strong> Calls the function with a valid CSV file.</p>
# 
# <p><strong>validate_file("data.exe"):</strong> Calls the function with an invalid file format and triggers the custom exception.</p>
