#!/usr/bin/env python
# coding: utf-8

# # Normal Distribution
# 
# ### Definition
# 
# Normal Distribution is a probability distribution where most of the values are concentrated around the mean.
# 
# The values become less frequent as we move away from the mean.
# 
# It is also called a bell-shaped distribution because its graph looks like a bell.
# 
# ### Formula
# 
# The probability density function of Normal Distribution is:
# 
# f(x) = (1 / (σ√(2π))) × e^(-(x - μ)² / (2σ²))
# 
# Where:
# 
# x = data value
# 
# μ = mean
# 
# σ = standard deviation
# 
# ### Numerical Example
# 
# Suppose the average exam mark is 50 and the standard deviation is 10.
# 
# Most students' marks may be around 50.
# 
# Some students may score around 40 or 60.
# 
# Very few students may score extremely low or extremely high.
# 
# ### Business Example
# 
# A company can use Normal Distribution to study employee performance scores when most employees have scores around the average.
# 
# ### AI/ML Example
# 
# Normal Distribution is commonly used in statistics and machine learning.
# 
# It can help us understand numerical features, data distributions and model assumptions.
# 
# ### Python Implementation
# 
# The following program generates normally distributed data and displays it using a histogram.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Normal Distribution")
plt.show()


# ### Interpretation
# 
# The histogram shows a bell-shaped distribution.
# 
# Most values are concentrated around the mean, which is 50.
# 
# As we move away from the mean, the number of values decreases.
# 
# This is the typical shape of a Normal Distribution.

# # Uniform Distribution
# 
# ### Definition
# 
# Uniform Distribution is a distribution where all values have an equal or almost equal chance of occurring.
# 
# In a continuous uniform distribution, values within a particular range have the same probability density.
# 
# ### Formula
# 
# For a continuous Uniform Distribution:
# 
# f(x) = 1 / (b - a)
# 
# Where:
# 
# a = minimum value
# 
# b = maximum value
# 
# ### Numerical Example
# 
# Suppose a random number is selected between 1 and 10.
# 
# Every value in this range has an equal chance of being selected.
# 
# For example:
# 
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 
# The probability is spread evenly across the range.
# 
# ### Business Example
# 
# A company may use a random process to select customers from a fixed range of customer IDs.
# 
# If every ID has an equal chance of being selected, it represents a simple uniform selection.
# 
# ### AI/ML Example
# 
# Uniform Distribution can be used for generating random values during simulations and for initializing some machine learning parameters.
# 
# ### Python Implementation
# 
# The following program generates random values between 0 and 1 and displays their distribution.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(0, 1, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Uniform Distribution")
plt.show()


# ### Interpretation
# 
# The histogram shows that the values are spread relatively evenly across the range from 0 to 1.
# 
# Unlike Normal Distribution, the values are not concentrated around a single middle point.
# 
# Uniform Distribution gives equal probability across the specified range.

# # Gaussian Distribution
# 
# ### Definition
# 
# Gaussian Distribution is a continuous probability distribution that has a bell-shaped curve.
# 
# It is commonly used to represent data where most values are around the mean and fewer values occur as we move away from the mean.
# 
# Gaussian Distribution is another name commonly used for Normal Distribution.
# 
# ### Formula
# 
# f(x) = (1 / (σ√(2π))) × e^(-(x - μ)² / (2σ²))
# 
# Where:
# 
# x = data value
# 
# μ = mean
# 
# σ = standard deviation
# 
# ### Numerical Example
# 
# Suppose the average height of a group is 165 cm and the standard deviation is 5 cm.
# 
# Most people may have heights close to 165 cm.
# 
# Fewer people may have heights much lower or much higher than 165 cm.
# 
# This creates a bell-shaped distribution.
# 
# ### Business Example
# 
# A company can use Gaussian Distribution to analyse measurements such as product dimensions when most products are close to the target measurement.
# 
# ### AI/ML Example
# 
# Gaussian Distribution is important in machine learning and statistics.
# 
# It is used in techniques such as Gaussian Naive Bayes and is also used to model numerical data.
# 
# ### Python Implementation
# 
# The following program generates data using a Gaussian distribution and displays it as a histogram.

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(165, 5, 1000)

plt.hist(data, bins=20)
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.title("Gaussian Distribution")
plt.show()


# ### Interpretation
# 
# The histogram shows a bell-shaped curve.
# 
# Most values are close to the mean of 165.
# 
# As the values move farther from the mean, their frequency decreases.
# 
# Gaussian Distribution and Normal Distribution describe the same commonly used bell-shaped distribution.

# # Left Skew
# 
# ### Definition
# 
# Left Skew is a distribution where the tail of the data extends more towards the left side.
# 
# It is also called Negative Skewness.
# 
# In a left-skewed distribution, most of the values are concentrated on the right side, while a few smaller values create a long tail towards the left.
# 
# ### Relationship
# 
# For a left-skewed distribution:
# 
# Mean < Median < Mode
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 2, 8, 9, 10, 10, 11, 12
# 
# Most values are concentrated around the higher values.
# 
# The smaller value 2 creates a tail towards the left.
# 
# This represents left skew.
# 
# ### Business Example
# 
# A company may analyse customer spending where most customers spend higher amounts, but a small number of customers spend very little.
# 
# This can create a left-skewed distribution.
# 
# ### AI/ML Example
# 
# In machine learning, identifying skewness helps us understand the distribution of numerical features.
# 
# Highly skewed features may sometimes need transformation before being used in a model.
# 
# ### Python Implementation
# 
# The following program creates a left-skewed dataset and displays it using a histogram.

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

data = np.concatenate([
    np.random.normal(70, 8, 900),
    np.random.normal(25, 5, 100)
])

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Left Skewed Distribution")
plt.show()


# ### Interpretation
# 
# The histogram shows that most values are concentrated on the right side.
# 
# A smaller number of values extend towards the left and create a longer left tail.
# 
# Therefore, the distribution is left-skewed or negatively skewed.

# # Right Skew
# 
# ### Definition
# 
# Right Skew is a distribution where the tail of the data extends more towards the right side.
# 
# It is also called Positive Skewness.
# 
# In a right-skewed distribution, most of the values are concentrated on the left side, while a few larger values create a long tail towards the right.
# 
# ### Relationship
# 
# For a right-skewed distribution:
# 
# Mean > Median > Mode
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 2, 3, 4, 5, 5, 6, 20
# 
# Most values are concentrated around the smaller values.
# 
# The large value 20 creates a tail towards the right.
# 
# This represents right skew.
# 
# ### Business Example
# 
# Income data is often used as an example of a right-skewed distribution.
# 
# Most people may have moderate incomes, while a small number of people have very high incomes.
# 
# These high values create a long tail towards the right.
# 
# ### AI/ML Example
# 
# In machine learning, identifying right-skewed features helps us understand the distribution of data.
# 
# A highly skewed feature may sometimes be transformed before training a machine learning model.
# 
# ### Python Implementation
# 
# The following program creates a right-skewed dataset and displays it using a histogram.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=2, size=1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Right Skewed Distribution")
plt.show()


# ### Interpretation
# 
# The histogram shows that most values are concentrated on the left side.
# 
# A smaller number of larger values extend towards the right and create a longer right tail.
# 
# Therefore, the distribution is right-skewed or positively skewed.

# # Symmetric Distribution
# 
# ### Definition
# 
# A symmetric distribution is a distribution where the data is distributed in a similar way on both sides of the center.
# 
# The left side and right side have approximately the same shape.
# 
# ### Relationship
# 
# In a perfectly symmetric distribution:
# 
# Mean = Median = Mode
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 1, 2, 3, 4, 5, 6, 7
# 
# The center value is 4.
# 
# The values on both sides are balanced:
# 
# Left side: 1, 2, 3
# 
# Right side: 5, 6, 7
# 
# This represents a symmetric distribution.
# 
# ### Business Example
# 
# A company can analyse production measurements where most products are distributed evenly around the target value.
# 
# For example, if the target weight is 500 grams, measurements may be distributed similarly above and below 500 grams.
# 
# ### AI/ML Example
# 
# Symmetry is useful when analysing the distribution of numerical features.
# 
# Normal Distribution is a common example of a symmetric distribution.
# 
# ### Python Implementation
# 
# The following program generates data from a normal distribution and displays it using a histogram.

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Symmetric Distribution")
plt.show()


# ### Interpretation
# 
# The histogram is approximately symmetric around the mean.
# 
# The values are distributed on both sides of the center in a similar pattern.
# 
# A normal distribution is an example of a symmetric distribution.

# # Kurtosis
# 
# ### Definition
# 
# Kurtosis is a statistical measure that describes the shape of the distribution, especially the tail behaviour of the data.
# 
# It helps us understand whether a distribution has relatively light or heavy tails compared with a normal distribution.
# 
# ### Types of Kurtosis
# 
# There are three common types:
# 
# 1. Mesokurtic
#    - Similar tail behaviour to a normal distribution.
# 
# 2. Leptokurtic
#    - Heavier tails.
#    - More extreme values may occur.
# 
# 3. Platykurtic
#    - Lighter tails.
#    - Fewer extreme values may occur.
# 
# ### Formula
# 
# A common population definition of kurtosis is:
# 
# Kurtosis = E[(X - μ)⁴] / σ⁴
# 
# Where:
# 
# X = data value
# 
# μ = mean
# 
# σ = standard deviation
# 
# ### Numerical Example
# 
# Suppose two datasets have similar means and standard deviations.
# 
# If one dataset contains more extreme values than the other, its tails can be heavier.
# 
# Kurtosis helps us identify this difference in tail behaviour.
# 
# ### Business Example
# 
# A company can use kurtosis to analyse financial returns.
# 
# A dataset with heavy tails may indicate that extreme changes occur more often than expected under a normal distribution.
# 
# ### AI/ML Example
# 
# Kurtosis can help during exploratory data analysis to understand the shape and extreme-value behaviour of numerical features.
# 
# ### Python Implementation
# 
# The following program calculates kurtosis using Pandas.

# In[7]:


import pandas as pd

values = [10, 12, 13, 14, 15, 16, 18, 20, 50]

data = pd.Series(values)

kurtosis = data.kurt()

print("Values:", values)
print("Kurtosis:", kurtosis)


# ### Interpretation
# 
# The dataset has a positive excess kurtosis.
# 
# This indicates heavier tails and a greater presence of extreme values compared with a normal distribution.
# 
# Kurtosis is mainly useful for understanding the tail behaviour of a distribution.

# # Empirical Rule (68–95–99.7)
# 
# ### Definition
# 
# The Empirical Rule describes how data is distributed in a normal distribution.
# 
# It tells us approximately how much data falls within 1, 2 and 3 standard deviations from the mean.
# 
# ### Rule
# 
# For a normal distribution:
# 
# 68% of the data falls within ±1 standard deviation from the mean.
# 
# 95% of the data falls within ±2 standard deviations from the mean.
# 
# 99.7% of the data falls within ±3 standard deviations from the mean.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Mean = 50
# 
# Standard Deviation = 10
# 
# Within 1 standard deviation:
# 
# 50 - 10 = 40
# 
# 50 + 10 = 60
# 
# Approximately 68% of the data falls between 40 and 60.
# 
# Within 2 standard deviations:
# 
# 50 - 20 = 30
# 
# 50 + 20 = 70
# 
# Approximately 95% of the data falls between 30 and 70.
# 
# Within 3 standard deviations:
# 
# 50 - 30 = 20
# 
# 50 + 30 = 80
# 
# Approximately 99.7% of the data falls between 20 and 80.
# 
# ### Business Example
# 
# A company can use the Empirical Rule to understand employee performance scores when the scores approximately follow a normal distribution.
# 
# For example, it can estimate how many employees fall within 1, 2 or 3 standard deviations from the average performance score.
# 
# ### AI/ML Example
# 
# The Empirical Rule helps in understanding normally distributed features and identifying unusually extreme values.
# 
# It can also provide a simple way to understand how data is spread around the mean.
# 
# ### Python Implementation
# 
# The following program calculates the ranges covered by 1, 2 and 3 standard deviations.

# In[8]:


mean = 50
standard_deviation = 10

one_std = (mean - standard_deviation, mean + standard_deviation)
two_std = (mean - 2 * standard_deviation, mean + 2 * standard_deviation)
three_std = (mean - 3 * standard_deviation, mean + 3 * standard_deviation)

print("Mean:", mean)
print("1 Standard Deviation:", one_std, "→ Approximately 68%")
print("2 Standard Deviations:", two_std, "→ Approximately 95%")
print("3 Standard Deviations:", three_std, "→ Approximately 99.7%")


# ### Interpretation
# 
# For a normal distribution:
# 
# Approximately 68% of the data lies between 40 and 60.
# 
# Approximately 95% of the data lies between 30 and 70.
# 
# Approximately 99.7% of the data lies between 20 and 80.
# 
# The Empirical Rule helps us quickly understand how data is distributed around the mean.
