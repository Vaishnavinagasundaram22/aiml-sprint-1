#!/usr/bin/env python
# coding: utf-8

# # What is Statistics?
# 
# ### Definition
# 
# Statistics is the process of collecting, organizing, analyzing, and interpreting data.
# 
# ### Why It Is Used
# 
# Statistics helps us understand data, find patterns, compare values, and make better decisions based on data.
# 
# ### Real-World Example
# 
# A college can collect students' marks and calculate the average mark to understand the overall performance.
# 
# ### AI/ML Example
# 
# In AI/ML, statistics helps us understand a dataset before building a machine learning model.
# 
# For example, we can calculate the average age of customers and identify unusual values in the dataset.
# 
# ### Numerical Example
# 
# Suppose the marks of 5 students are:
# 
# 60, 70, 80, 90, 100
# 
# Average:
# 
# (60 + 70 + 80 + 90 + 100) / 5 = 80
# 
# So, the average mark is 80.

# In[1]:


# Student marks
marks = [60, 70, 80, 90, 100]

# Calculate total
total = sum(marks)

# Calculate number of students
count = len(marks)

# Calculate average
average = total / count

print("Total Marks:", total)
print("Number of Students:", count)
print("Average Marks:", average)


# # Importance of Statistics in AI/ML
# 
# ### Definition
# 
# Statistics is important in AI/ML because it helps us understand data, find patterns, handle uncertainty, and make better predictions.
# 
# ### Why It Is Important
# 
# Statistics is used in AI/ML for:
# 
# - Understanding the dataset
# - Finding the average and spread of data
# - Detecting unusual values
# - Handling missing data
# - Finding relationships between features
# - Evaluating machine learning models
# - Making predictions based on data
# 
# ### Real-World Example
# 
# Suppose a company has customer data containing age, salary, and purchase amount.
# 
# Using statistics, we can find the average salary, understand customer spending, and identify unusual values.
# 
# ### AI/ML Example
# 
# Before training a machine learning model, we need to understand the dataset.
# 
# For example, statistics can help us find the average age of customers and check how the ages are distributed.
# 
# Statistics helps us understand the data before giving it to the ML model.

# In[2]:


# Customer ages
ages = [20, 25, 30, 35, 40]

# Calculate average age
average_age = sum(ages) / len(ages)

print("Customer Ages:", ages)
print("Average Age:", average_age)


# ### Program Explanation
# 
# `ages` contains the customer age data.
# 
# `sum()` calculates the total of all ages.
# 
# `len()` finds the number of customers.
# 
# We divide the total by the number of customers to find the average age.
# 
# This shows how statistics can help us understand data before using it in AI/ML.

# # Statistics vs Machine Learning
# 
# ### Definition of Statistics
# 
# Statistics is mainly used to collect, organize, analyze, and interpret data.
# 
# ### Definition of Machine Learning
# 
# Machine Learning is a method where computers learn patterns from data and use those patterns to make predictions or decisions.
# 
# ### Difference
# 
# Statistics mainly focuses on understanding and analyzing data.
# 
# Machine Learning mainly focuses on learning patterns from data and making predictions.
# 
# ### Simple Example
# 
# Suppose we have student marks:
# 
# 60, 70, 80, 90, 100
# 
# Using Statistics:
# 
# We can calculate the average mark.
# 
# Using Machine Learning:
# 
# We can use previous student data to predict the marks of a new student.
# 
# ### AI/ML Example
# 
# A company has customer data.
# 
# Statistics can help us understand the customer's age, salary, and spending habits.
# 
# Machine Learning can use this data to predict whether a customer will buy a product or not.

# In[3]:


# Student marks
marks = [60, 70, 80, 90, 100]

# Statistics: calculate average
average = sum(marks) / len(marks)

print("Average Marks:", average)

# Simple prediction example
new_student_mark = 85

if new_student_mark >= average:
    print("Prediction: Student may perform above average")
else:
    print("Prediction: Student may perform below average")


# ### Program Explanation
# 
# First, we calculate the average of the existing student marks.
# 
# Then, we compare a new student's mark with the average.
# 
# If the new mark is greater than or equal to the average, the program predicts that the student may perform above average.
# 
# This is only a simple example to understand the difference between statistical analysis and prediction.

# # Population and Sample
# 
# ### Definition
# 
# Population is the complete group of people, objects, or data that we want to study.
# 
# Sample is a smaller group selected from the population for the study.
# 
# ### Explanation
# 
# For example, a college has 1,000 students.
# 
# - 1,000 students → Population
# - 100 selected students → Sample
# 
# A sample is used when collecting data from the entire population is difficult or time-consuming.

# In[4]:


population = 1000
sample = 100

print("Total Population:", population)
print("Sample:", sample)


# # Parameter and Statistic
# 
# ### Definition
# 
# A parameter is a numerical value that describes the entire population.
# 
# A statistic is a numerical value that describes a sample taken from the population.
# 
# ### Explanation
# 
# For example, a college has 1,000 students.
# 
# If we calculate the average age of all 1,000 students, it is called a parameter because it represents the entire population.
# 
# If we select 100 students and calculate their average age, it is called a statistic because it represents only the sample.
# 
# ### Example
# 
# - Average age of all 1,000 students → Parameter
# - Average age of 100 selected students → Statistic
# 
# ### Why It Is Used
# 
# Parameter and statistic help us understand the difference between the whole population and a sample.
# 
# In statistics, we often use a sample statistic to understand or estimate information about the population.

# In[5]:


population_ages = [20, 21, 22, 20, 23, 21, 22, 24, 20, 21]
sample_ages = [20, 21, 22, 20, 23]

population_mean = sum(population_ages) / len(population_ages)
sample_mean = sum(sample_ages) / len(sample_ages)

print("Population Mean:", population_mean)
print("Sample Mean:", sample_mean)


# # Measures of Central Tendency
# 
# ### Definition
# 
# Measures of Central Tendency are statistical methods used to find the central or typical value in a dataset.
# 
# The three main measures of central tendency are:
# 
# - Mean
# - Median
# - Mode
# 
# ### Explanation
# 
# Suppose we have the following marks:
# 
# 10, 20, 30, 40, 50
# 
# We can use Mean, Median, or Mode to understand the central value of the data.
# 
# Mean finds the average value.
# 
# Median finds the middle value after arranging the data.
# 
# Mode finds the value that appears most often.
# 
# ### Why It Is Used
# 
# Measures of Central Tendency help us understand a large amount of data using a single representative value.

# In[6]:


marks = [10, 20, 30, 40, 50]

mean = sum(marks) / len(marks)

print("Mean:", mean)


# # Mean
# 
# ### Definition
# 
# Mean is the average value of a set of numbers.
# 
# ### Explanation
# 
# To find the mean, we add all the values and divide the total by the number of values.
# 
# For example, if the marks are:
# 
# 10, 20, 30, 40, 50
# 
# First, add all the marks:
# 
# 10 + 20 + 30 + 40 + 50 = 150
# 
# There are 5 values.
# 
# Mean = 150 / 5 = 30
# 
# So, the mean is 30.
# 
# ### Why It Is Used
# 
# Mean is used to find the average value of a dataset. It helps us understand the overall or typical value of the data.

# # Median
# 
# ### Definition
# 
# Median is the middle value of a dataset when the values are arranged in ascending or descending order.
# 
# ### Explanation
# 
# First, arrange the values in order.
# 
# For example:
# 
# 10, 20, 30, 40, 50
# 
# Here, 30 is the middle value.
# 
# So, the median is 30.
# 
# If the dataset has an even number of values, we take the two middle values and calculate their average.
# 
# For example:
# 
# 10, 20, 30, 40
# 
# The two middle values are 20 and 30.
# 
# Median = (20 + 30) / 2 = 25
# 
# ### Why It Is Used
# 
# Median is used to find the middle value of a dataset. It is especially useful when the data contains very high or very low values.

# In[8]:


marks = [10, 20, 30, 40, 50]

marks.sort()

n = len(marks)

if n % 2 == 1:
    median = marks[n // 2]
else:
    median = (marks[n // 2 - 1] + marks[n // 2]) / 2

print("Median:", median)


# # Mode
# 
# ### Definition
# 
# Mode is the value that appears most frequently in a dataset.
# 
# ### Explanation
# 
# For example, consider the following marks:
# 
# 10, 20, 20, 30, 40
# 
# Here, 20 appears two times, while the other values appear only once.
# 
# So, the mode is 20.
# 
# Mode can be used with numbers as well as categorical data such as colors, names, or departments.
# 
# ### Why It Is Used
# 
# Mode is used to find the most frequently occurring value in a dataset.
# 
# It helps us identify the most common value or category.

# In[9]:


marks = [10, 20, 20, 30, 40]

mode = max(set(marks), key=marks.count)

print("Mode:", mode)


# # Range
# 
# ### Definition
# 
# Range is the difference between the highest value and the lowest value in a dataset.
# 
# ### Explanation
# 
# To find the range, we first identify the highest and lowest values.
# 
# For example, consider the following marks:
# 
# 10, 20, 30, 40, 50
# 
# Highest value = 50
# 
# Lowest value = 10
# 
# Range = Highest value - Lowest value
# 
# Range = 50 - 10
# 
# Range = 40
# 
# So, the range is 40.
# 
# ### Why It Is Used
# 
# Range is used to understand how spread out the data is.
# 
# A larger range means the values are more spread out, while a smaller range means the values are closer together.

# In[10]:


marks = [10, 20, 30, 40, 50]

highest = max(marks)
lowest = min(marks)

range_value = highest - lowest

print("Highest Value:", highest)
print("Lowest Value:", lowest)
print("Range:", range_value)


# # Variance
# 
# ### Definition
# 
# Variance is a statistical measure that shows how much the values in a dataset differ from the mean.
# 
# ### Explanation
# 
# Variance tells us how spread out the data values are from the average value.
# 
# For example, consider the values:
# 
# 10, 20, 30
# 
# First, we find the mean:
# 
# Mean = (10 + 20 + 30) / 3
# 
# Mean = 20
# 
# Now, we find how much each value differs from the mean:
# 
# - 10 is 10 away from the mean
# - 20 is 0 away from the mean
# - 30 is 10 away from the mean
# 
# We square these differences and find their average.
# 
# Variance = 100 + 0 + 100 / 3
# 
# Variance = 66.67
# 
# ### Why It Is Used
# 
# Variance is used to understand how much the data values are spread out from the mean.
# 
# A small variance means the values are closer to the mean.
# 
# A large variance means the values are more spread out.

# In[11]:


data = [10, 20, 30]

mean = sum(data) / len(data)

squared_differences = [(x - mean) ** 2 for x in data]

variance = sum(squared_differences) / len(data)

print("Mean:", mean)
print("Variance:", variance)


# # Standard Deviation
# 
# ### Definition
# 
# Standard deviation is a statistical measure that shows how much the values in a dataset are spread out from the mean.
# 
# ### Explanation
# 
# Standard deviation is calculated by taking the square root of the variance.
# 
# For example, consider the values:
# 
# 10, 20, 30
# 
# The mean is 20.
# 
# The variance is 66.67.
# 
# Standard Deviation = √66.67
# 
# Standard Deviation ≈ 8.16
# 
# A small standard deviation means the values are closer to the mean.
# 
# A large standard deviation means the values are more spread out from the mean.
# 
# ### Why It Is Used
# 
# Standard deviation is used to understand the amount of variation or spread in a dataset.
# 
# It is commonly used in statistics and data analysis.

# In[12]:


import math

data = [10, 20, 30]

mean = sum(data) / len(data)

squared_differences = [(x - mean) ** 2 for x in data]

variance = sum(squared_differences) / len(data)

standard_deviation = math.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)


# # Probability
# 
# ### Definition
# 
# Probability is the measure of how likely an event is to happen.
# 
# The value of probability is always between 0 and 1.
# 
# - 0 → The event is impossible.
# - 1 → The event is certain.
# - Between 0 and 1 → The event has a chance of happening.
# 
# ### Explanation
# 
# For example, when we toss a coin, there are two possible outcomes:
# 
# - Head
# - Tail
# 
# There is one favorable outcome for getting a Head and two total possible outcomes.
# 
# Probability of getting Head:
# 
# Probability = Favorable Outcomes / Total Outcomes
# 
# Probability = 1 / 2
# 
# Probability = 0.5
# 
# So, the probability of getting a Head is 0.5 or 50%.
# 
# ### Why It Is Used
# 
# Probability is used to measure the chance of an event happening.
# 
# It is commonly used in data analysis, statistics, machine learning, and decision-making.

# In[14]:


favorable_outcomes = 1
total_outcomes = 2

probability = favorable_outcomes / total_outcomes

print("Probability of getting Head:", probability)


# # Types of Probability
# 
# ### Definition
# 
# There are different ways to calculate probability depending on the situation.
# 
# The main types of probability are:
# 
# - Classical Probability
# - Experimental Probability
# - Subjective Probability
# 
# ### Explanation
# 
# #### 1. Classical Probability
# 
# Classical probability is calculated when all possible outcomes are known and equally likely.
# 
# Example:
# 
# When we toss a fair coin, there are two possible outcomes: Head and Tail.
# 
# Probability of getting Head = 1 / 2 = 0.5
# 
# #### 2. Experimental Probability
# 
# Experimental probability is calculated using the results obtained from an actual experiment.
# 
# Example:
# 
# If a coin is tossed 10 times and Head appears 6 times:
# 
# Experimental Probability = 6 / 10 = 0.6
# 
# #### 3. Subjective Probability
# 
# Subjective probability is based on personal judgment, experience, or belief.
# 
# Example:
# 
# A person may believe that there is a high chance of rain based on the weather conditions.
# 
# ### Why It Is Used
# 
# Different types of probability help us calculate or estimate the chance of an event based on known outcomes, actual results, or personal judgment.

# In[15]:


# Classical Probability

favorable_outcomes = 1
total_outcomes = 2

classical_probability = favorable_outcomes / total_outcomes

# Experimental Probability

heads = 6
total_tosses = 10

experimental_probability = heads / total_tosses

print("Classical Probability:", classical_probability)
print("Experimental Probability:", experimental_probability)


# # Random Variable
# 
# ### Definition
# 
# A random variable is a variable that represents the possible numerical outcomes of a random experiment.
# 
# ### Explanation
# 
# A random experiment is an experiment where the result is not known in advance.
# 
# For example, when we toss a coin, the possible outcomes are:
# 
# - Head
# - Tail
# 
# We can assign numerical values to these outcomes.
# 
# For example:
# 
# - Head = 1
# - Tail = 0
# 
# Here, the random variable represents the outcome of the coin toss.
# 
# Another example is rolling a dice.
# 
# The possible values of the random variable are:
# 
# 1, 2, 3, 4, 5, 6
# 
# We do not know which number will appear before rolling the dice, so it is a random variable.
# 
# ### Why It Is Used
# 
# Random variables are used to represent uncertain outcomes using numbers.
# 
# They are commonly used in probability, statistics, and machine learning.

# In[16]:


import random

coin = random.choice(["Head", "Tail"])

if coin == "Head":
    random_variable = 1
else:
    random_variable = 0

print("Coin Result:", coin)
print("Random Variable:", random_variable)


# # Discrete and Continuous Random Variables
# 
# ### Definition
# 
# Random variables are mainly divided into two types:
# 
# 1. Discrete Random Variable
# 2. Continuous Random Variable
# 
# ### Explanation
# 
# ### 1. Discrete Random Variable
# 
# A discrete random variable can take specific and countable values.
# 
# For example, when rolling a dice, the possible values are:
# 
# 1, 2, 3, 4, 5, 6
# 
# We can count these values, so the dice result is a discrete random variable.
# 
# Other examples:
# 
# - Number of students in a class
# - Number of cars in a parking area
# - Number of goals in a match
# 
# ### 2. Continuous Random Variable
# 
# A continuous random variable can take any value within a range.
# 
# For example, a person's height can be:
# 
# 160.5 cm, 160.55 cm, 160.555 cm, etc.
# 
# Height can have many possible decimal values, so it is a continuous random variable.
# 
# Other examples:
# 
# - Weight
# - Temperature
# - Time
# - Distance
# 
# ### Why It Is Used
# 
# The difference between discrete and continuous random variables helps us understand whether data can be counted as separate values or measured over a range.

# In[17]:


# Discrete Random Variable

number_of_students = 30

# Continuous Random Variable

height = 165.5

print("Number of Students:", number_of_students)
print("Height:", height)


# # Probability Distribution
# 
# ### Definition
# 
# Probability Distribution shows all the possible values of a random variable and the probability of each value.
# 
# ### Explanation
# 
# For example, when we roll a fair dice, the possible outcomes are:
# 
# 1, 2, 3, 4, 5, 6
# 
# Each number has the same probability.
# 
# Probability = 1 / 6 = 0.1667
# 
# The total probability of all possible outcomes is always 1.
# 
# ### Why It Is Used
# 
# Probability Distribution is used to understand how likely each possible outcome is.
# 
# It is useful in statistics, data analysis, and machine learning.

# In[18]:


outcomes = [1, 2, 3, 4, 5, 6]

probability = 1 / 6

for outcome in outcomes:
    print("Outcome:", outcome, "Probability:", probability)


# # Normal Distribution
# 
# ### Definition
# 
# Normal Distribution is a type of probability distribution where most of the data values are close to the average value.
# 
# It is also called a bell-shaped distribution because its graph looks like a bell.
# 
# ### Explanation
# 
# In a normal distribution, most values are found near the mean.
# 
# The values become less common as we move away from the mean.
# 
# For example, the heights of students in a class may follow a normal distribution, where most students have heights close to the average height.
# 
# ### Why It Is Used
# 
# Normal Distribution is used to understand how data is spread around the mean.
# 
# It is commonly used in statistics, data analysis, and machine learning.

# In[20]:


get_ipython().system('pip install numpy matplotlib')


# In[21]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Normal Distribution")
plt.show()


# In[ ]:




