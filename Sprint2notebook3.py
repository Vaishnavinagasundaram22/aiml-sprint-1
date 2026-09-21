#!/usr/bin/env python
# coding: utf-8

# # Range
# 
# ### Definition
# 
# Range tells us how much the values are spread from the smallest value to the largest value.
# 
# ### Formula
# 
# Range = Maximum Value - Minimum Value
# 
# ### Numerical Example
# 
# Suppose the marks are:
# 
# 10, 20, 30, 40, 50
# 
# Maximum value = 50
# 
# Minimum value = 10
# 
# Range = 50 - 10 = 40
# 
# So, the Range is 40.
# 
# ### Business Example
# 
# A company checks the delivery times of orders:
# 
# 20, 25, 30, 35, 40 minutes
# 
# Range = 40 - 20 = 20 minutes
# 
# This shows the difference between the fastest and slowest delivery time.
# 
# ### AI/ML Example
# 
# In a machine learning dataset, range can be used to understand how widely a numerical feature is distributed.
# 
# For example, if the age values are from 20 to 60:
# 
# Range = 60 - 20 = 40
# 
# ### Python Implementation
# 
# The following program finds the minimum value, maximum value and range of a dataset.

# In[1]:


values = [10, 20, 30, 40, 50]

minimum = min(values)
maximum = max(values)

range_value = maximum - minimum

print("Values:", values)
print("Minimum Value:", minimum)
print("Maximum Value:", maximum)
print("Range:", range_value)


# # Variance
# 
# ### Definition
# 
# Variance tells us how much the values in a dataset are spread out from the mean.
# 
# If the values are close to the mean, the variance will be small.
# 
# If the values are far from the mean, the variance will be large.
# 
# ### Formula
# 
# Population Variance:
# 
# Variance = Σ(x - μ)² / N
# 
# Where:
# 
# x = each value
# μ = mean
# N = total number of values
# 
# ### Numerical Example
# 
# Suppose the values are:
# 
# 2, 4, 6
# 
# First, find the mean:
# 
# Mean = (2 + 4 + 6) / 3
# Mean = 4
# 
# Now find the difference from the mean:
# 
# 2 - 4 = -2
# 4 - 4 = 0
# 6 - 4 = 2
# 
# Square the differences:
# 
# (-2)² = 4
# 0² = 0
# 2² = 4
# 
# Variance:
# 
# Variance = (4 + 0 + 4) / 3
# Variance = 8 / 3
# Variance = 2.67
# 
# ### Business Example
# 
# A company can use variance to understand how much employee sales values differ from the average sales.
# 
# Low variance means the sales values are closer to the average.
# 
# High variance means the sales values are more spread out.
# 
# ### AI/ML Example
# 
# Variance is useful in understanding how much a numerical feature varies in a dataset.
# 
# It is also important in feature analysis and machine learning techniques such as PCA.
# 
# ### Python Implementation
# 
# The following program calculates the population variance manually.

# In[2]:


values = [2, 4, 6]

mean = sum(values) / len(values)

squared_differences = [(value - mean) ** 2 for value in values]

variance = sum(squared_differences) / len(values)

print("Values:", values)
print("Mean:", mean)
print("Variance:", variance)


# # Standard Deviation
# 
# ### Definition
# 
# Standard Deviation tells us how much the values in a dataset are spread out from the mean.
# 
# It is the square root of variance.
# 
# ### Formula
# 
# Standard Deviation = √Variance
# 
# For population data:
# 
# σ = √(Σ(x - μ)² / N)
# 
# Where:
# 
# x = each value
# μ = mean
# N = total number of values
# 
# ### Numerical Example
# 
# Suppose the values are:
# 
# 2, 4, 6
# 
# Mean = 4
# 
# We already calculated the variance:
# 
# Variance = 2.67
# 
# So:
# 
# Standard Deviation = √2.67
# 
# Standard Deviation ≈ 1.63
# 
# ### Business Example
# 
# A company can use standard deviation to understand how much employee sales differ from the average sales.
# 
# If the standard deviation is small, the sales values are close to the average.
# 
# If the standard deviation is large, the sales values are more spread out.
# 
# ### AI/ML Example
# 
# Standard deviation is commonly used in machine learning to understand feature variation.
# 
# It is also useful in feature scaling, especially in standardization.
# 
# ### Python Implementation
# 
# The following program calculates the standard deviation from the variance.

# In[3]:


values = [2, 4, 6]

mean = sum(values) / len(values)

squared_differences = [(value - mean) ** 2 for value in values]

variance = sum(squared_differences) / len(values)

standard_deviation = variance ** 0.5

print("Values:", values)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)


# # Quartiles
# 
# ### Definition
# 
# Quartiles divide an ordered dataset into four equal parts.
# 
# The three main quartiles are:
# 
# Q1 → First Quartile → 25% of the data is below this value
# 
# Q2 → Second Quartile → 50% of the data is below this value
# 
# Q3 → Third Quartile → 75% of the data is below this value
# 
# Q2 is also called the Median.
# 
# ### Formula
# 
# Q1 = 25th Percentile
# 
# Q2 = 50th Percentile
# 
# Q3 = 75th Percentile
# 
# ### Numerical Example
# 
# Suppose the values are:
# 
# 10, 20, 30, 40, 50, 60, 70
# 
# The middle value is 40, so:
# 
# Q2 = 40
# 
# The lower part is:
# 
# 10, 20, 30
# 
# Q1 = 20
# 
# The upper part is:
# 
# 50, 60, 70
# 
# Q3 = 60
# 
# Therefore:
# 
# Q1 = 20
# Q2 = 40
# Q3 = 60
# 
# ### Business Example
# 
# A company can use quartiles to understand employee salaries.
# 
# Q1 shows the salary level below which approximately 25% of the employees fall.
# 
# Q2 represents the median salary.
# 
# Q3 shows the salary level below which approximately 75% of the employees fall.
# 
# ### AI/ML Example
# 
# Quartiles are useful in machine learning for understanding the distribution of numerical features.
# 
# They are also used in detecting outliers using the IQR method.
# 
# ### Python Implementation
# 
# The following program calculates Q1, Q2 and Q3 using NumPy.

# In[4]:


import numpy as np

values = [10, 20, 30, 40, 50, 60, 70]

q1 = np.percentile(values, 25)
q2 = np.percentile(values, 50)
q3 = np.percentile(values, 75)

print("Values:", values)
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)


# # Percentiles
# 
# ### Definition
# 
# Percentile tells us the position of a value compared with the other values in a dataset.
# 
# It tells us the percentage of values that are below a particular value.
# 
# For example, if a student's score is at the 80th percentile, it means the score is higher than approximately 80% of the scores in the dataset.
# 
# ### Formula
# 
# Percentile Position = (P / 100) × (N + 1)
# 
# Where:
# 
# P = percentile value
# 
# N = number of values
# 
# Note: In Python, percentile calculation may use interpolation depending on the method used.
# 
# ### Numerical Example
# 
# Suppose the marks are:
# 
# 10, 20, 30, 40, 50
# 
# The 50th percentile represents the middle of the dataset.
# 
# The 50th percentile is:
# 
# 30
# 
# So, 30 is the value at the 50th percentile.
# 
# ### Business Example
# 
# A company can use percentiles to analyse employee salaries.
# 
# For example, the 90th percentile salary tells us the salary level below which approximately 90% of the employees fall.
# 
# ### AI/ML Example
# 
# Percentiles can be used to understand the distribution of features in a dataset.
# 
# They are also useful for identifying extreme values and detecting outliers.
# 
# ### Python Implementation
# 
# The following program calculates different percentiles using NumPy.

# In[5]:


import numpy as np

values = [10, 20, 30, 40, 50]

p25 = np.percentile(values, 25)
p50 = np.percentile(values, 50)
p75 = np.percentile(values, 75)

print("Values:", values)
print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)


# ### Interpretation
# 
# The 25th percentile is 20.
# 
# The 50th percentile is 30.
# 
# The 75th percentile is 40.
# 
# This means approximately:
# 
# 25% of the values are below 20.
# 
# 50% of the values are below 30.
# 
# 75% of the values are below 40.
# 
# Percentiles help us understand the position of values within a dataset.

# # Interquartile Range (IQR)
# 
# ### Definition
# 
# IQR stands for Interquartile Range.
# 
# It measures the spread of the middle 50% of the data.
# 
# IQR is calculated using the first quartile (Q1) and third quartile (Q3).
# 
# ### Formula
# 
# IQR = Q3 - Q1
# 
# Where:
# 
# Q1 = First Quartile
# 
# Q3 = Third Quartile
# 
# ### Numerical Example
# 
# Suppose:
# 
# Q1 = 20
# 
# Q3 = 60
# 
# Then:
# 
# IQR = Q3 - Q1
# 
# IQR = 60 - 20
# 
# IQR = 40
# 
# So, the IQR is 40.
# 
# ### Business Example
# 
# A company can use IQR to understand the spread of the middle 50% of employee salaries.
# 
# It can also help identify unusually high or low salary values.
# 
# ### AI/ML Example
# 
# IQR is commonly used for detecting outliers in machine learning datasets.
# 
# A common method is:
# 
# Lower Bound = Q1 - 1.5 × IQR
# 
# Upper Bound = Q3 + 1.5 × IQR
# 
# Values outside these boundaries can be considered potential outliers.
# 
# ### Python Implementation
# 
# The following program calculates Q1, Q3 and IQR.

# In[6]:


import numpy as np

values = [10, 20, 30, 40, 50, 60, 70]

q1 = np.percentile(values, 25)
q3 = np.percentile(values, 75)

iqr = q3 - q1

print("Values:", values)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)


# # Coefficient of Variation
# 
# ### Definition
# 
# Coefficient of Variation (CV) is a measure of relative variation in a dataset.
# 
# It compares the standard deviation with the mean.
# 
# CV is usually expressed as a percentage.
# 
# ### Formula
# 
# CV = (Standard Deviation / Mean) × 100
# 
# ### Numerical Example
# 
# Suppose:
# 
# Mean = 50
# 
# Standard Deviation = 5
# 
# Then:
# 
# CV = (5 / 50) × 100
# 
# CV = 10%
# 
# So, the Coefficient of Variation is 10%.
# 
# ### Business Example
# 
# A company wants to compare the variation in sales between two different products.
# 
# Even if the products have different average sales, CV can help compare their relative variation.
# 
# ### AI/ML Example
# 
# In machine learning, CV can help understand how much variation a feature has relative to its mean.
# 
# It can also be useful when comparing datasets or features that have different scales.
# 
# ### Python Implementation
# 
# The following program calculates the Coefficient of Variation.

# In[7]:


values = [45, 50, 55]

mean = sum(values) / len(values)

squared_differences = [(value - mean) ** 2 for value in values]

variance = sum(squared_differences) / len(values)

standard_deviation = variance ** 0.5

cv = (standard_deviation / mean) * 100

print("Values:", values)
print("Mean:", mean)
print("Standard Deviation:", standard_deviation)
print("Coefficient of Variation:", cv, "%")


# In[ ]:




