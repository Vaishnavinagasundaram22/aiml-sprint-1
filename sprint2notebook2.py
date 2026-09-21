#!/usr/bin/env python
# coding: utf-8

# # Mean
# 
# ### Definition
# 
# Mean is the average value of a set of numbers.
# 
# ### Formula
# 
# Mean = Sum of all values / Number of values
# 
# ### Numerical Example
# 
# Consider the following marks:
# 
# 10, 20, 30, 40, 50
# 
# First, add all the values:
# 
# 10 + 20 + 30 + 40 + 50 = 150
# 
# Number of values = 5
# 
# Mean = 150 / 5
# 
# Mean = 30
# 
# So, the mean is 30.
# 
# ### Business Example
# 
# A company can calculate the mean monthly sales to understand its average sales.
# 
# For example, if the monthly sales are:
# 
# 1000, 1200, 1500, 1300, 2000
# 
# The mean gives the average monthly sales.
# 
# ### AI/ML Example
# 
# In Machine Learning, mean can be used to understand the average value of a feature.
# 
# For example, the mean age of customers can help us understand the general age of the customers in a dataset.
# 
# ### Python Implementation
# 
# The following program calculates the mean of a set of values.

# In[1]:


marks = [10, 20, 30, 40, 50]

mean = sum(marks) / len(marks)

print("Marks:", marks)
print("Mean:", mean)


# # Median
# 
# ### Definition
# 
# Median is the middle value of a dataset when the values are arranged in ascending or descending order.
# 
# ### Formula
# 
# If the number of values is odd:
# 
# Median = Middle value
# 
# If the number of values is even:
# 
# Median = Average of the two middle values
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# 10, 20, 30, 40, 50
# 
# The values are already arranged in ascending order.
# 
# The middle value is 30.
# 
# Therefore:
# 
# Median = 30
# 
# For an even number of values:
# 
# 10, 20, 30, 40
# 
# The two middle values are 20 and 30.
# 
# Median = (20 + 30) / 2
# 
# Median = 25
# 
# ### Business Example
# 
# A company can use the median salary to understand the typical salary of its employees.
# 
# Median is useful when some salaries are extremely high or low.
# 
# ### AI/ML Example
# 
# In Machine Learning, median can be used to understand the center of a dataset.
# 
# It can also be useful when dealing with data that contains extreme values.
# 
# ### Python Implementation
# 
# The following program calculates the median of a dataset.

# In[2]:


import numpy as np

marks = [10, 20, 30, 40, 50]

median = np.median(marks)

print("Marks:", marks)
print("Median:", median)


# ### Interpretation
# 
# The program calculates the middle value of the dataset.
# 
# The median is 30.
# 
# This means that 30 is the middle value when the data is arranged in order.
# 
# Median is especially useful when the dataset contains extreme values.

# # Mode
# 
# ### Definition
# 
# Mode is the value that occurs most frequently in a dataset.
# 
# ### Formula
# 
# There is no specific mathematical formula for Mode.
# 
# Mode = Most frequently occurring value
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# 10, 20, 20, 30, 40
# 
# Here, 20 occurs two times.
# 
# The other values occur only once.
# 
# Therefore:
# 
# Mode = 20
# 
# ### Business Example
# 
# A shop can use Mode to find the most commonly purchased product size.
# 
# For example, if the most frequently purchased shoe size is 8, then the mode is 8.
# 
# ### AI/ML Example
# 
# In Machine Learning, Mode can be used to find the most common category in categorical data.
# 
# For example, if a dataset contains customer preferred payment methods, Mode can show the most commonly used payment method.
# 
# ### Python Implementation
# 
# The following program finds the mode of a dataset.

# In[4]:


from statistics import mode

values = [10, 20, 20, 30, 40]

result = mode(values)

print("Values:", values)
print("Mode:", result)


# # Weighted Mean
# 
# ### Definition
# 
# Weighted Mean is an average where different values are given different levels of importance or weight.
# 
# ### Formula
# 
# Weighted Mean = Σ(value × weight) / Σ(weight)
# 
# ### Numerical Example
# 
# Consider a student's marks:
# 
# Assignment = 80, Weight = 20%
# 
# Exam = 90, Weight = 80%
# 
# Weighted Mean = (80 × 0.20) + (90 × 0.80)
# 
# Weighted Mean = 16 + 72
# 
# Weighted Mean = 88
# 
# Therefore, the weighted mean is 88.
# 
# ### Business Example
# 
# A company can calculate an employee's overall performance using different weights for different factors.
# 
# For example, sales performance may have a higher weight than attendance.
# 
# ### AI/ML Example
# 
# Weighted Mean can be used when some observations or features are more important than others.
# 
# For example, in a weighted dataset, more important observations can have higher weights.
# 
# ### Python Implementation
# 
# The following program calculates the weighted mean of two values.

# In[5]:


values = [80, 90]
weights = [0.20, 0.80]

weighted_mean = sum(value * weight for value, weight in zip(values, weights))

print("Weighted Mean:", weighted_mean)


# # Geometric Mean
# 
# ### Definition
# 
# Geometric Mean is an average that is calculated by multiplying all the values and taking the nth root, where n is the number of values.
# 
# ### Formula
# 
# Geometric Mean = (x₁ × x₂ × x₃ × ... × xₙ)^(1/n)
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# 2, 8
# 
# First, multiply the values:
# 
# 2 × 8 = 16
# 
# There are 2 values.
# 
# Geometric Mean = √16
# 
# Geometric Mean = 4
# 
# Therefore, the geometric mean is 4.
# 
# ### Business Example
# 
# Geometric Mean can be used to calculate the average growth rate of a business over multiple years.
# 
# For example, it can be used to analyze investment growth or sales growth.
# 
# ### AI/ML Example
# 
# Geometric Mean can be used when working with values that change by ratios or percentages.
# 
# It is useful for analyzing growth rates and multiplicative changes in data.
# 
# ### Python Implementation
# 
# The following program calculates the geometric mean of a dataset.

# In[8]:


get_ipython().system('pip install scipy')


# In[ ]:


from scipy.stats import gmean

values = [2, 8]

geometric_mean = gmean(values)

print("Values:", values)
print("Geometric Mean:", geometric_mean)


# # Harmonic Mean
# 
# ### Definition
# 
# Harmonic Mean is an average that is calculated by dividing the number of values by the sum of their reciprocals.
# 
# ### Formula
# 
# Harmonic Mean = n / (1/x₁ + 1/x₂ + ... + 1/xₙ)
# 
# Here, n represents the number of values.
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# 2, 4
# 
# Number of values = 2
# 
# Harmonic Mean = 2 / (1/2 + 1/4)
# 
# Harmonic Mean = 2 / 0.75
# 
# Harmonic Mean = 2.67
# 
# Therefore, the harmonic mean is approximately 2.67.
# 
# ### Business Example
# 
# Harmonic Mean can be used to calculate an average rate, such as average speed or average price-to-performance ratios.
# 
# For example, it can be useful when comparing rates across different situations.
# 
# ### AI/ML Example
# 
# Harmonic Mean is used when we want to combine rates or performance measures.
# 
# For example, the F1-score in Machine Learning uses the harmonic mean of Precision and Recall.
# 
# ### Python Implementation
# 
# The following program calculates the harmonic mean without using any external library.

# In[ ]:


values = [2, 4]

n = len(values)

harmonic_mean = n / sum(1 / value for value in values)

print("Values:", values)
print("Harmonic Mean:", harmonic_mean)


# In[ ]:




