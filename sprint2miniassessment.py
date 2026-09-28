#!/usr/bin/env python
# coding: utf-8

# # Mini Assessment
# 
# ## Question 1
# 
# Calculate the Variance of:
# 
# 10, 20, 30, 40, 50

# In[3]:


import numpy as np

data = [10, 20, 30, 40, 50]

variance = np.var(data)

print("Variance:", variance)


# ## Question 2
# 
# Calculate the IQR of:
# 
# 10, 12, 15, 18, 20, 22, 25, 30, 35

# In[4]:


import numpy as np

data = [10, 12, 15, 18, 20, 22, 25, 30, 35]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# ## Question 3
# 
# Using the IQR method, identify the outliers from:
# 
# 10, 12, 15, 18, 20, 22, 25, 30, 100

# In[5]:


import numpy as np

data = [10, 12, 15, 18, 20, 22, 25, 30, 100]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = [
    value for value in data
    if value < lower_limit or value > upper_limit
]

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Outliers:", outliers)


# ## Question 4
# 
# Calculate the Correlation between:
# 
# Study Hours = [2, 4, 6, 8, 10]
# 
# Marks = [50, 60, 70, 80, 90]

# In[6]:


import pandas as pd

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

correlation = df["Study_Hours"].corr(df["Marks"])

print("Correlation:", correlation)


# ## Question 5
# 
# Calculate the Mean, Median, Variance, and Standard Deviation of:
# 
# 10, 20, 30, 40, 50

# In[7]:


import numpy as np

data = [10, 20, 30, 40, 50]

mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
standard_deviation = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)


# ## Question 6
# 
# Create a Correlation Matrix for:
# 
# Study_Hours = [2, 4, 6, 8, 10]
# 
# Marks = [50, 60, 70, 80, 90]
# 
# Attendance = [60, 65, 70, 80, 85]

# In[8]:


import pandas as pd

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 80, 90],
    "Attendance": [60, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)


# ## Question 7
# 
# Identify the outliers using the IQR method:
# 
# 5, 6, 7, 8, 9, 10, 11, 50

# In[9]:


import numpy as np

data = [5, 6, 7, 8, 9, 10, 11, 50]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = [
    value for value in data
    if value < lower_limit or value > upper_limit
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Outliers:", outliers)


# ## Question 8
# 
# Calculate the Variance of:
# 
# 5, 10, 15, 20, 25

# In[10]:


import numpy as np

data = [5, 10, 15, 20, 25]

variance = np.var(data)

print("Variance:", variance)


# ## Question 9
# 
# Calculate the Correlation between:
# 
# Advertising = [10, 20, 30, 40, 50]
# 
# Sales = [15, 25, 35, 45, 55]

# In[11]:


import pandas as pd

data = {
    "Advertising": [10, 20, 30, 40, 50],
    "Sales": [15, 25, 35, 45, 55]
}

df = pd.DataFrame(data)

correlation = df["Advertising"].corr(df["Sales"])

print("Correlation:", correlation)


# ## Question 10
# 
# Calculate the Mean, Median, IQR, and Standard Deviation of:
# 
# 10, 15, 20, 25, 30, 35, 40

# In[12]:


import numpy as np

data = [10, 15, 20, 25, 30, 35, 40]

mean = np.mean(data)
median = np.median(data)

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

standard_deviation = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("IQR:", IQR)
print("Standard Deviation:", standard_deviation)


# In[ ]:




