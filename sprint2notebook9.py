#!/usr/bin/env python
# coding: utf-8

# # What are Outliers?
# 
# ### Definition
# 
# An outlier is a data value that is very different from the other values in a dataset.
# 
# It is a value that lies far away from the general pattern of the data.
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# 10, 12, 11, 13, 12, 14, 50
# 
# Most values are between 10 and 14.
# 
# The value 50 is very different from the other values.
# 
# Therefore, 50 can be considered an outlier.
# 
# ### Business Example
# 
# A company records the delivery time of its orders:
# 
# 25, 28, 30, 27, 29, 120 minutes
# 
# Most deliveries take around 25–30 minutes, but one delivery took 120 minutes.
# 
# The value 120 may be an outlier.
# 
# ### AI/ML Example
# 
# In a machine learning dataset, an outlier could represent:
# 
# - An unusual transaction
# - An abnormal sensor reading
# - An unusually high house price
# - A suspicious financial transaction
# 
# Detecting outliers is important because extreme values can affect statistical calculations and machine learning models.
# 
# ### Python Implementation
# 
# We can identify a possible outlier by comparing the values in a dataset.

# In[1]:


values = [10, 12, 11, 13, 12, 14, 50]

print("Values:", values)

for value in values:
    if value > 30:
        print("Possible Outlier:", value)


# # Types of Outliers
# 
# ### Definition
# 
# Outliers can be classified based on how they occur and where they appear in a dataset.
# 
# The main types of outliers are:
# 
# 1. Global Outlier
# 2. Contextual Outlier
# 3. Collective Outlier
# 
# ### Global Outlier
# 
# A Global Outlier is a value that is very different from the rest of the dataset.
# 
# Example:
# 
# 10, 12, 11, 13, 50
# 
# Here, 50 is a global outlier because it is far away from the other values.
# 
# ### Contextual Outlier
# 
# A Contextual Outlier is a value that is unusual in a particular situation or context.
# 
# Example:
# 
# A temperature of 40°C may be normal in summer but unusual during winter.
# 
# ### Collective Outlier
# 
# A Collective Outlier occurs when a group of data values together forms an unusual pattern.
# 
# Example:
# 
# In network traffic data, a sudden continuous series of unusual requests may represent an abnormal pattern.
# 
# ### Business Example
# 
# A bank normally sees transactions between ₹500 and ₹10,000.
# 
# A single transaction of ₹5,00,000 may be a global outlier.
# 
# A transaction made at an unusual time or location may be a contextual outlier.
# 
# A large group of unusual transactions occurring together may be a collective outlier.
# 
# ### AI/ML Example
# 
# Outlier types can be useful in:
# 
# - Fraud detection
# - Network intrusion detection
# - Sensor monitoring
# - Anomaly detection
# 
# Machine learning systems can use these patterns to identify unusual data.
# 
# ### Python Implementation
# 
# The following program demonstrates a simple global outlier.

# In[2]:


values = [10, 12, 11, 13, 50]

mean = sum(values) / len(values)

print("Values:", values)
print("Mean:", mean)

for value in values:
    if abs(value - mean) > 20:
        print("Possible Global Outlier:", value)


# # Detecting Outliers
# 
# ### Definition
# 
# Detecting Outliers means identifying data values that are significantly different from the other values in a dataset.
# 
# Common methods used to detect outliers are:
# 
# - IQR Method
# - Z-Score Method
# - Box Plot
# - Scatter Plot
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 12, 11, 13, 50
# 
# The value 50 is much higher than the other values, so it may be an outlier.
# 
# ### Business Example
# 
# A company can detect unusually high transaction amounts to identify possible abnormal transactions.
# 
# ### AI/ML Example
# 
# Outlier detection can be used to identify unusual records before training a machine learning model.
# 
# ### Python Implementation
# 
# The IQR method can be used to detect outliers by calculating the lower and upper limits.

# In[3]:


import numpy as np

values = [10, 12, 11, 13, 50]

q1 = np.percentile(values, 25)
q3 = np.percentile(values, 75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = [
    value for value in values
    if value < lower_limit or value > upper_limit
]

print("Outliers:", outliers)


# # IQR (Interquartile Range)
# 
# ### Definition
# 
# IQR stands for Interquartile Range. It measures the spread of the middle 50% of the data.
# 
# It is calculated using the first quartile (Q1) and third quartile (Q3).
# 
# ### Formula
# 
# IQR = Q3 - Q1
# 
# Q1 = 25th percentile
# 
# Q3 = 75th percentile
# 
# For detecting outliers:
# 
# Lower Limit = Q1 - 1.5 × IQR
# 
# Upper Limit = Q3 + 1.5 × IQR
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 11, 12, 13, 14, 50
# 
# Q1 = 11.25
# 
# Q3 = 13.75
# 
# IQR = 13.75 - 11.25 = 2.5
# 
# Upper Limit = 13.75 + (1.5 × 2.5) = 17.5
# 
# Since 50 is greater than 17.5, 50 is an outlier.
# 
# ### Business Example
# 
# A company can use IQR to identify unusually high or low transaction amounts.
# 
# ### AI/ML Example
# 
# In AI/ML, IQR can be used to detect extreme values in a dataset before training a machine learning model.
# 
# ### Python Implementation
# 
# The following program calculates Q1, Q3, IQR, and identifies outliers.

# In[4]:


import numpy as np

values = [10, 11, 12, 13, 14, 50]

q1 = np.percentile(values, 25)
q3 = np.percentile(values, 75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = [
    value for value in values
    if value < lower_limit or value > upper_limit
]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Outliers:", outliers)


# # Z-Score
# 
# ### Definition
# 
# Z-Score tells us how far a data value is from the mean in terms of standard deviation.
# 
# A high positive or negative Z-Score can indicate that a value is unusual compared to the other values.
# 
# ### Formula
# 
# Z-Score = (X - Mean) / Standard Deviation
# 
# Where:
# 
# X = Data value
# 
# Mean = Average of the data
# 
# Standard Deviation = Measure of how spread out the data is
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 20, 30, 40, 50
# 
# Mean = 30
# 
# For the value 50:
# 
# Z-Score = (50 - 30) / Standard Deviation
# 
# The Z-Score shows how far 50 is from the mean.
# 
# A commonly used rule is that values with a Z-Score greater than +3 or less than -3 may be considered outliers.
# 
# ### Business Example
# 
# A company can use Z-Score to identify unusually high sales transactions compared with normal transactions.
# 
# ### AI/ML Example
# 
# In AI/ML, Z-Score can be used to detect unusual values in numerical features before training a machine learning model.
# 
# ### Python Implementation
# 
# The following program calculates the Z-Score for each value and identifies possible outliers.

# In[5]:


import numpy as np

values = np.array([10, 20, 30, 40, 100])

mean = np.mean(values)
std = np.std(values)

z_scores = (values - mean) / std

print("Mean:", mean)
print("Standard Deviation:", std)
print("Z-Scores:", z_scores)

outliers = values[np.abs(z_scores) > 2]

print("Possible Outliers:", outliers)


# # Box Plot
# 
# ### Definition
# 
# A Box Plot is a graph used to understand the distribution of data and identify outliers.
# 
# It shows the minimum value, Q1, median, Q3, and maximum value.
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 12, 14, 15, 16, 18, 50
# 
# The Box Plot can show that 50 is far away from the other values and may be an outlier.
# 
# ### Business Example
# 
# A company can use a Box Plot to visualize employee salaries and identify unusually high or low salaries.
# 
# ### AI/ML Example
# 
# In AI/ML, Box Plots can be used to visualize numerical features and identify possible outliers before model training.
# 
# ### Python Implementation
# 
# The following program creates a Box Plot using Matplotlib.

# In[6]:


import matplotlib.pyplot as plt

values = [10, 12, 14, 15, 16, 18, 50]

plt.boxplot(values)

plt.title("Box Plot")
plt.ylabel("Values")

plt.show()


# # Scatter Plot
# 
# ### Definition
# 
# A Scatter Plot is a graph that uses points to show the relationship between two numerical variables.
# 
# It can also help identify unusual data points that are far away from the other points.
# 
# ### Numerical Example
# 
# Consider the following values:
# 
# Hours Studied: 1, 2, 3, 4, 5
# 
# Marks: 40, 45, 50, 55, 95
# 
# The point (5, 95) is far from the general pattern and may be an unusual value.
# 
# ### Business Example
# 
# A company can use a Scatter Plot to compare advertising expenses and sales.
# 
# ### AI/ML Example
# 
# In AI/ML, Scatter Plots can be used to visualize relationships between features and identify possible outliers before model training.
# 
# ### Python Implementation
# 
# The following program creates a Scatter Plot using Matplotlib.

# In[7]:


import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5]
marks = [40, 45, 50, 55, 95]

plt.scatter(hours_studied, marks)

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()


# In[ ]:




