#!/usr/bin/env python
# coding: utf-8

# # What is NumPy?
# 
# ### Definition
# 
# NumPy stands for Numerical Python. It is a Python library used for numerical calculations and working with arrays.
# 
# NumPy helps us store and process large amounts of numerical data easily and efficiently.
# 
# ### Example
# 
# For example, a teacher has student marks:
# 
# 60, 75, 80, 90, 85
# 
# We can store these values in a NumPy array and easily calculate the total and average.
# 
# ### AI/ML Example
# 
# In AI/ML, we work with numerical data such as age, salary, marks, and product prices. NumPy arrays help us store and perform calculations on this data.
# 
# ### Code Explanation
# 
# `import numpy as np` imports the NumPy library.
# 
# `np.array()` creates a NumPy array.
# 
# `np.sum()` calculates the total of the values.
# 
# `np.mean()` calculates the average of the values.
# 
# ### Output Explanation
# 
# The output displays the student marks, their total, and their average.

# In[1]:


import numpy as np

marks = np.array([60, 75, 80, 90, 85])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))


# # Why NumPy?
# 
# NumPy is used because it can handle numerical data faster and more efficiently than normal Python lists.
# 
# It provides arrays that allow us to perform calculations on many values at the same time.
# 
# For example, if we have marks of many students, NumPy can calculate the total, average, minimum, and maximum values easily.
# 
# ### Real-World Example
# 
# A company may have sales data for thousands of products. Instead of calculating each value one by one, NumPy can perform calculations on the complete dataset efficiently.
# 
# ### AI/ML Example
# 
# In Machine Learning, large datasets contain many numerical values. NumPy helps in numerical calculations and data processing before building ML models.
# 
# ### Code Explanation
# 
# `np.array()` creates a NumPy array.
# 
# `marks + 5` adds 5 to every value in the array at the same time. This is one reason NumPy is useful.
# 
# ### Output Explanation
# 
# The original marks are displayed first. Then 5 is added to every student's mark using a single operation.

# In[2]:


import numpy as np

marks = np.array([60, 70, 80, 90, 85])

updated_marks = marks + 5

print("Original Marks:", marks)
print("Updated Marks:", updated_marks)


# # NumPy Array (ndarray)
# 
# ### Definition
# 
# A NumPy array is called an `ndarray`, which means N-dimensional array.
# 
# It is a collection of values stored together in a structured format. NumPy arrays can store numerical data and can have one or more dimensions.
# 
# ### Example
# 
# A list of student marks can be converted into a NumPy array:
# 
# [60, 70, 80, 90, 85]
# 
# This is a one-dimensional NumPy array.
# 
# ### Real-World Example
# 
# A school can store the marks of students in a NumPy array and perform calculations such as total and average.
# 
# ### AI/ML Example
# 
# In AI/ML, numerical data such as age, salary, height, and experience can be stored in NumPy arrays and processed efficiently.
# 
# ### Code Explanation
# 
# `np.array()` converts the given values into a NumPy array.
# 
# `type()` is used to check the data type of the object.
# 
# The output shows that the object created is a NumPy `ndarray`.

# In[3]:


import numpy as np

marks = np.array([60, 70, 80, 90, 85])

print("Marks:", marks)
print("Type:", type(marks))


# # Creating NumPy Arrays
# 
# ### Definition
# 
# Creating a NumPy array means converting values or Python collections such as lists into a NumPy `ndarray`.
# 
# NumPy provides different methods to create arrays depending on the requirement.
# 
# ### Example
# 
# We can create a NumPy array from a Python list using `np.array()`.
# 
# We can also create arrays filled with zeros or ones using `np.zeros()` and `np.ones()`.
# 
# ### Real-World Example
# 
# If we need to store the marks of students, we can create an array using their marks.
# 
# If we need an array to represent empty values initially, we can create an array filled with zeros.
# 
# ### AI/ML Example
# 
# In AI/ML, arrays can be created to store numerical features such as age, salary, experience, or model input values.
# 
# ### Code Explanation
# 
# `np.array()` creates an array from a list.
# 
# `np.zeros()` creates an array containing only zeros.
# 
# `np.ones()` creates an array containing only ones.
# 
# ### Output Explanation
# 
# The output shows three different NumPy arrays created using different methods.

# In[4]:


import numpy as np

marks = np.array([60, 70, 80, 90, 85])
zeros = np.zeros(5)
ones = np.ones(5)

print("Marks Array:", marks)
print("Zeros Array:", zeros)
print("Ones Array:", ones)


# # Dimensions of NumPy Array
# 
# ### Definition
# 
# The dimension of a NumPy array tells us how many levels of data the array contains.
# 
# A one-dimensional array contains a single row of values.
# 
# A two-dimensional array contains rows and columns.
# 
# A three-dimensional array contains multiple two-dimensional arrays.
# 
# ### Example
# 
# 1D:
# [10, 20, 30]
# 
# 2D:
# [[10, 20],
#  [30, 40]]
# 
# ### Real-World Example
# 
# Student marks for one class can be represented using a 1D array.
# 
# Marks of multiple students for multiple subjects can be represented using a 2D array.
# 
# ### AI/ML Example
# 
# In AI/ML, a dataset is commonly represented as a 2D array where rows represent records and columns represent features.
# 
# ### Code Explanation
# 
# `ndim` returns the number of dimensions of a NumPy array.
# 
# The first array has 1 dimension and the second array has 2 dimensions.
# 
# ### Output Explanation
# 
# The output shows the number of dimensions for each array.

# In[5]:


import numpy as np

one_d = np.array([10, 20, 30])

two_d = np.array([
    [10, 20],
    [30, 40]
])

print("1D Array:", one_d)
print("1D Dimensions:", one_d.ndim)

print("2D Array:")
print(two_d)
print("2D Dimensions:", two_d.ndim)


# # Shape of NumPy Array
# 
# ### Definition
# 
# The shape of a NumPy array tells us the number of elements present along each dimension.
# 
# For a 1D array, the shape shows the number of elements.
# 
# For a 2D array, the shape shows the number of rows and columns.
# 
# ### Example
# 
# If an array has 3 rows and 2 columns, its shape will be `(3, 2)`.
# 
# ### Real-World Example
# 
# A company has sales data for 4 products and 2 months. We can store this data in a 2D array with 4 rows and 2 columns.
# 
# ### AI/ML Example
# 
# In AI/ML, the shape of a dataset helps us understand how many records and features are present.
# 
# ### Code Explanation
# 
# The `shape` attribute returns the shape of the NumPy array.
# 
# In the example, the array contains 3 rows and 2 columns, so the shape is `(3, 2)`.
# 
# ### Output Explanation
# 
# The output `(3, 2)` means there are 3 rows and 2 columns.

# In[6]:


import numpy as np

sales = np.array([
    [100, 200],
    [150, 250],
    [180, 300]
])

print("Sales Data:")
print(sales)
print("Shape:", sales.shape)


# # Size of NumPy Array
# 
# ### Definition
# 
# The `size` of a NumPy array tells us the total number of elements present in the array.
# 
# It counts all the elements, including elements in all rows and columns.
# 
# ### Example
# 
# If an array has 3 rows and 2 columns, it contains:
# 
# 3 × 2 = 6 elements
# 
# So, its size is 6.
# 
# ### Real-World Example
# 
# If a company has sales data for 3 products across 2 months, the array contains 6 sales values.
# 
# ### AI/ML Example
# 
# In AI/ML, `size` can be used to understand how many total values are present in an array or dataset.
# 
# ### Code Explanation
# 
# The `size` attribute returns the total number of elements in the NumPy array.
# 
# ### Output Explanation
# 
# The array has 3 rows and 2 columns, so the total number of elements is 6.

# In[7]:


import numpy as np

sales = np.array([
    [100, 200],
    [150, 250],
    [180, 300]
])

print("Sales Data:")
print(sales)
print("Size:", sales.size)


# # Data Types in NumPy
# 
# ### Definition
# 
# The data type tells us what type of values are stored inside a NumPy array.
# 
# NumPy supports different data types such as integers, floating-point numbers, and strings.
# 
# The `dtype` attribute is used to check the data type of an array.
# 
# ### Example
# 
# An array containing whole numbers can have an integer data type.
# 
# An array containing decimal values can have a floating-point data type.
# 
# ### Real-World Example
# 
# A company may store customer ages as integers and customer salaries as floating-point numbers.
# 
# ### AI/ML Example
# 
# In AI/ML, choosing a suitable data type can help in storing and processing numerical data efficiently.
# 
# ### Code Explanation
# 
# `dtype` shows the data type of the values stored in the NumPy array.
# 
# In the example, the first array contains integers and the second array contains decimal values.
# 
# ### Output Explanation
# 
# The output shows the data type of each NumPy array.

# In[8]:


import numpy as np

ages = np.array([20, 25, 30, 35])
salary = np.array([25000.5, 30000.75, 45000.25])

print("Ages:", ages)
print("Age Data Type:", ages.dtype)

print("Salary:", salary)
print("Salary Data Type:", salary.dtype)


# # Indexing in NumPy
# 
# ### Definition
# 
# Indexing means accessing a specific element from a NumPy array using its position.
# 
# NumPy uses zero-based indexing, which means the first element is at index `0`, the second element is at index `1`, and so on.
# 
# ### Example
# 
# For the array:
# 
# [10, 20, 30, 40, 50]
# 
# The indexes are:
# 
# 10 → 0  
# 20 → 1  
# 30 → 2  
# 40 → 3  
# 50 → 4
# 
# ### Real-World Example
# 
# If we store the marks of students in an array, we can use indexing to access the mark of a particular student.
# 
# ### AI/ML Example
# 
# In AI/ML, indexing is used to access specific values from datasets or arrays during data processing.
# 
# ### Code Explanation
# 
# `marks[0]` accesses the first element.
# 
# `marks[2]` accesses the third element.
# 
# ### Output Explanation
# 
# The output displays the first and third values from the NumPy array.

# In[9]:


import numpy as np

marks = np.array([60, 70, 80, 90, 85])

print("Marks:", marks)
print("First Mark:", marks[0])
print("Third Mark:", marks[2])


# # Slicing in NumPy
# 
# ### Definition
# 
# Slicing means selecting a specific range of elements from a NumPy array.
# 
# The basic syntax is:
# 
# array[start:stop]
# 
# The `start` index is included, but the `stop` index is not included.
# 
# ### Example
# 
# For the array:
# 
# [10, 20, 30, 40, 50]
# 
# `array[1:4]` gives:
# 
# [20, 30, 40]
# 
# Because index 1 is included and index 4 is excluded.
# 
# ### Real-World Example
# 
# If a company stores monthly sales from January to December, slicing can be used to select sales for only a few months.
# 
# ### AI/ML Example
# 
# In AI/ML, slicing can be used to select specific rows, columns, or parts of an array for data processing.
# 
# ### Code Explanation
# 
# `marks[1:4]` selects elements from index 1 up to, but not including, index 4.
# 
# ### Output Explanation
# 
# The output contains the second, third, and fourth values of the array.

# In[10]:


import numpy as np

marks = np.array([60, 70, 80, 90, 85])

selected_marks = marks[1:4]

print("Marks:", marks)
print("Selected Marks:", selected_marks)


# # Reshaping NumPy Arrays
# 
# ### Definition
# 
# Reshaping means changing the structure or shape of a NumPy array without changing its data.
# 
# The `reshape()` function is used to change the number of rows and columns.
# 
# ### Example
# 
# An array with 6 elements can be reshaped from 1 row with 6 elements into 2 rows and 3 columns.
# 
# The total number of elements must remain the same.
# 
# ### Real-World Example
# 
# Suppose we have sales data for 6 products. We can reshape the data into 2 rows and 3 columns to organize it in a table-like format.
# 
# ### AI/ML Example
# 
# In AI/ML, reshaping is commonly used to convert data into the required format before giving it to a Machine Learning model.
# 
# ### Code Explanation
# 
# `reshape(2, 3)` changes the array into 2 rows and 3 columns.
# 
# The original array has 6 elements, and the reshaped array also has 6 elements.
# 
# ### Output Explanation
# 
# The output shows the original one-dimensional array and the same data arranged into 2 rows and 3 columns.

# In[11]:


import numpy as np

sales = np.array([100, 200, 300, 400, 500, 600])

reshaped_sales = sales.reshape(2, 3)

print("Original Array:", sales)
print("Reshaped Array:")
print(reshaped_sales)


# # Flatten in NumPy
# 
# ### Definition
# 
# `flatten()` is used to convert a NumPy array with multiple dimensions into a one-dimensional array.
# 
# It returns all the elements as a single row.
# 
# ### Example
# 
# A 2D array:
# 
# [[10, 20],
#  [30, 40]]
# 
# After using `flatten()`:
# 
# [10, 20, 30, 40]
# 
# ### Real-World Example
# 
# If sales data is stored in rows and columns, we can flatten it into a single list of values when we need to process all values together.
# 
# ### AI/ML Example
# 
# In AI/ML, flattening can be used to convert multidimensional data into a one-dimensional form before passing it to certain Machine Learning algorithms.
# 
# ### Code Explanation
# 
# `flatten()` converts the 2D array into a 1D array.
# 
# The original data is not changed.
# 
# ### Output Explanation
# 
# The original array has 2 rows and 3 columns. After flattening, all 6 values are placed into one dimension.

# In[12]:


import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

flattened_data = data.flatten()

print("Original Array:")
print(data)

print("Flattened Array:")
print(flattened_data)


# # Copy vs View in NumPy
# 
# ### Definition
# 
# In NumPy, `copy()` creates a completely separate array, while a view creates another way to access the same original data.
# 
# If we change a copied array, the original array is not affected.
# 
# If we change a view, the original array can also be affected because both refer to the same underlying data.
# 
# ### Real-World Example
# 
# Imagine you have an original document.
# 
# A copy is like making a separate photocopy. Changes made to the photocopy do not affect the original.
# 
# A view is like looking at the same original document from another window. Changes to the data can affect the original.
# 
# ### AI/ML Example
# 
# In AI/ML data processing, `copy()` is useful when we want to modify data safely without changing the original dataset.
# 
# A view can be useful when we want to work with the same data without creating another copy in memory.
# 
# ### Code Explanation
# 
# `original.copy()` creates an independent copy.
# 
# `original[:]` creates a view of the original array.
# 
# When we change the copied array, the original remains unchanged.
# 
# When we change the view, the original array is also changed.
# 
# ### Output Explanation
# 
# The copied array changes from 10 to 100, but the original array remains unchanged.
# 
# The view changes from 20 to 200, so the original array also changes to 200.

# In[13]:


import numpy as np

original = np.array([10, 20, 30, 40])

copied = original.copy()
viewed = original[:]

copied[0] = 100
viewed[1] = 200

print("Original Array:", original)
print("Copied Array:", copied)
print("Viewed Array:", viewed)


# # Broadcasting in NumPy
# 
# ### Definition
# 
# Broadcasting is a NumPy feature that allows arrays with different shapes to perform operations together.
# 
# NumPy automatically adjusts the smaller array or value to match the larger array when possible.
# 
# ### Example
# 
# If we have:
# 
# [10, 20, 30]
# 
# and add `5`:
# 
# [10, 20, 30] + 5
# 
# NumPy adds 5 to every element:
# 
# [15, 25, 35]
# 
# ### Real-World Example
# 
# If a company wants to increase the price of every product by ₹5, we can add 5 to the entire NumPy array at once.
# 
# ### AI/ML Example
# 
# Broadcasting is commonly used in AI/ML for mathematical operations on arrays, such as adding values, scaling features, and normalizing data.
# 
# ### Code Explanation
# 
# `prices + 5` adds 5 to every element in the array using broadcasting.
# 
# We do not need to write a loop to add 5 to each value.
# 
# ### Output Explanation
# 
# The original prices are displayed first. The updated prices contain ₹5 added to every product price.

# In[14]:


import numpy as np

prices = np.array([100, 200, 300, 400])

updated_prices = prices + 5

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)


# # Array Operations in NumPy
# 
# ### Definition
# 
# Array operations are mathematical operations performed directly on NumPy arrays.
# 
# We can perform operations such as addition, subtraction, multiplication, and division on arrays.
# 
# NumPy performs these operations element by element.
# 
# ### Example
# 
# If we have two arrays:
# 
# [10, 20, 30]  
# [1, 2, 3]
# 
# Addition gives:
# 
# [11, 22, 33]
# 
# ### Real-World Example
# 
# A shop has the prices of three products and wants to calculate the price after adding a fixed amount. NumPy can perform the calculation on all prices at the same time.
# 
# ### AI/ML Example
# 
# Array operations are commonly used in AI/ML for calculations involving features, predictions, and numerical datasets.
# 
# ### Code Explanation
# 
# `array1 + array2` performs addition element by element.
# 
# `array1 - array2` performs subtraction.
# 
# `array1 * array2` performs multiplication.
# 
# `array1 / array2` performs division.
# 
# ### Output Explanation
# 
# Each operation is performed between the corresponding elements of the two arrays.

# In[15]:


import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([2, 4, 5])

print("Addition:", array1 + array2)
print("Subtraction:", array1 - array2)
print("Multiplication:", array1 * array2)
print("Division:", array1 / array2)


# # Universal Functions (ufuncs) in NumPy
# 
# ### Definition
# 
# Universal functions, also called `ufuncs`, are NumPy functions that perform operations on each element of an array.
# 
# They are designed to work efficiently with NumPy arrays without using explicit loops.
# 
# ### Examples
# 
# Some common NumPy universal functions are:
# 
# - `np.sqrt()` – calculates square root
# - `np.exp()` – calculates exponential value
# - `np.abs()` – returns absolute value
# - `np.round()` – rounds decimal values
# 
# ### Real-World Example
# 
# If a company has several numerical values and wants to calculate the square root of all values, NumPy can perform the calculation on the complete array at once.
# 
# ### AI/ML Example
# 
# ufuncs are used in AI/ML for mathematical calculations during data preprocessing, feature transformation, and numerical computation.
# 
# ### Code Explanation
# 
# `np.sqrt()` calculates the square root of every element in the array.
# 
# ### Output Explanation
# 
# The output shows the square root calculated for each value in the NumPy array.

# In[16]:


import numpy as np

numbers = np.array([4, 9, 16, 25])

square_roots = np.sqrt(numbers)

print("Numbers:", numbers)
print("Square Roots:", square_roots)


# In[ ]:




