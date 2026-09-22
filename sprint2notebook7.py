#!/usr/bin/env python
# coding: utf-8

# # Sampling
# 
# ### Definition
# 
# Sampling is the process of selecting a smaller group of people or data from a larger population for analysis.
# 
# In simple words, instead of studying the entire population, we select a smaller group called a sample.
# 
# ### Formula
# 
# There is no single formula for Sampling.
# 
# The basic idea is:
# 
# Population → Large group
# 
# Sample → Smaller group selected from the population
# 
# ### Numerical Example
# 
# Suppose a college has 1,000 students.
# 
# Instead of asking all 1,000 students about their satisfaction, we select 100 students and collect their responses.
# 
# Here:
# 
# Population = 1,000 students
# 
# Sample = 100 students
# 
# ### Business Example
# 
# A company has 10,000 customers.
# 
# The company wants to know whether customers are satisfied with a new product.
# 
# Instead of contacting all 10,000 customers, the company can select a smaller sample and collect their feedback.
# 
# ### AI/ML Example
# 
# In machine learning, datasets can be very large.
# 
# Sampling can be used to select a smaller portion of data for analysis, testing, or experimentation.
# 
# A properly selected sample can help us understand the characteristics of the larger population.
# 
# ### Python Implementation
# 
# The following program creates a population of 20 students and selects 5 students as a sample.

# In[1]:


import random

population = list(range(1, 21))

sample = random.sample(population, 5)

print("Population:", population)
print("Sample:", sample)
print("Population Size:", len(population))
print("Sample Size:", len(sample))


# # Random Sampling
# 
# ### Definition
# 
# Random Sampling is a sampling method where every member of the population has an equal chance of being selected.
# 
# In simple words, we select members randomly without intentionally choosing specific people.
# 
# ### Formula
# 
# There is no specific formula for Random Sampling.
# 
# The main idea is:
# 
# Every member of the population → Equal chance of selection
# 
# ### Numerical Example
# 
# Suppose a class has 20 students.
# 
# We want to select 5 students for a survey.
# 
# Using Random Sampling, 5 students are selected randomly from the 20 students.
# 
# Therefore:
# 
# Population = 20 students
# 
# Sample = 5 students
# 
# ### Business Example
# 
# A company has 10,000 customers and wants to collect feedback from 100 customers.
# 
# The company can randomly select 100 customers so that each customer has an equal chance of being selected.
# 
# ### AI/ML Example
# 
# Random Sampling can be used to select a subset of data from a large dataset.
# 
# For example, we may randomly select 1,000 records from a dataset containing 100,000 records for initial analysis.
# 
# ### Python Implementation
# 
# The following program randomly selects 5 students from a population of 20 students.

# # Stratified Sampling
# 
# ### Definition
# 
# Stratified Sampling is a sampling method where the population is divided into different groups called strata, and samples are selected from each group.
# 
# In simple words, first we divide the population into groups based on a common characteristic, then we select members from every group.
# 
# ### Formula
# 
# There is no single formula for Stratified Sampling.
# 
# A common approach is proportional sampling:
# 
# Sample from each group = (Group Size / Population Size) × Total Sample Size
# 
# ### Numerical Example
# 
# Suppose a college has:
# 
# - 60 Engineering students
# - 40 Arts students
# 
# Total students = 100
# 
# We want to select 20 students.
# 
# Using proportional sampling:
# 
# Engineering sample = (60 / 100) × 20 = 12
# 
# Arts sample = (40 / 100) × 20 = 8
# 
# So the final sample contains:
# 
# 12 Engineering students
# 
# 8 Arts students
# 
# ### Business Example
# 
# A company has customers from different age groups:
# 
# - Young customers
# - Middle-aged customers
# - Senior customers
# 
# The company can select customers from each age group to make sure every group is represented in the sample.
# 
# ### AI/ML Example
# 
# Suppose an ML dataset contains different classes of customers.
# 
# Stratified Sampling can be used to select samples from each class while maintaining the proportion of the original dataset.
# 
# This is especially useful when some groups are smaller than others.
# 
# ### Python Implementation
# 
# The following program divides students into two groups and selects samples from both groups.

# In[2]:


import random

engineering_students = [
    "E1", "E2", "E3", "E4", "E5",
    "E6", "E7", "E8", "E9", "E10"
]

arts_students = [
    "A1", "A2", "A3", "A4", "A5",
    "A6", "A7", "A8", "A9", "A10"
]

engineering_sample = random.sample(engineering_students, 5)
arts_sample = random.sample(arts_students, 5)

sample = engineering_sample + arts_sample

print("Engineering Sample:", engineering_sample)
print("Arts Sample:", arts_sample)
print("Total Sample:", sample)
print("Sample Size:", len(sample))


# # Cluster Sampling
# 
# ### Definition
# 
# Cluster Sampling is a sampling method where the population is divided into natural groups called clusters.
# 
# Instead of selecting individual people from the entire population, we randomly select some clusters and collect data from the selected clusters.
# 
# ### Formula
# 
# There is no single fixed formula for Cluster Sampling.
# 
# The main idea is:
# 
# Population → Divide into Clusters → Randomly Select Clusters → Collect Data
# 
# ### Numerical Example
# 
# A city has 5 schools:
# 
# School A → 100 students
# School B → 100 students
# School C → 100 students
# School D → 100 students
# School E → 100 students
# 
# Instead of selecting students from every school, we randomly select 2 schools.
# 
# Selected clusters:
# 
# School B
# School D
# 
# We can collect data from the students in these selected schools.
# 
# ### Business Example
# 
# A company has 10 branches in different cities.
# 
# Instead of collecting customer feedback from every branch, the company randomly selects 3 branches and collects feedback from those branches.
# 
# Here, each branch is a cluster.
# 
# ### AI/ML Example
# 
# Suppose we want to build a customer prediction model using data from many stores.
# 
# Instead of collecting data from every store, we can select some stores as clusters and use their customer data for analysis or model development.
# 
# ### Python Implementation
# 
# Python can be used to randomly select clusters from a population of clusters.

# In[3]:


import random

clusters = {
    "School A": ["Student 1", "Student 2", "Student 3"],
    "School B": ["Student 4", "Student 5", "Student 6"],
    "School C": ["Student 7", "Student 8", "Student 9"],
    "School D": ["Student 10", "Student 11", "Student 12"]
}

selected_clusters = random.sample(list(clusters.keys()), 2)

print("Selected Clusters:", selected_clusters)

selected_students = []

for cluster in selected_clusters:
    selected_students.extend(clusters[cluster])

print("Students from Selected Clusters:", selected_students)


# # Systematic Sampling
# 
# ### Definition
# 
# Systematic Sampling is a sampling method where we select every k-th member from a population after choosing a starting point.
# 
# It is useful when the population is arranged in an ordered list.
# 
# ### Formula
# 
# k = N / n
# 
# Where:
# 
# N = Total population size
# n = Required sample size
# k = Sampling interval
# 
# ### Numerical Example
# 
# Suppose a company has 20 employees and we want to select 5 employees.
# 
# N = 20
# n = 5
# 
# k = 20 / 5
# k = 4
# 
# If the starting point is 2, we select every 4th employee:
# 
# 2, 6, 10, 14, 18
# 
# So the selected sample is:
# 
# 2, 6, 10, 14, 18
# 
# ### Business Example
# 
# A supermarket has 1,000 customers in a customer list.
# 
# The company wants to survey 100 customers.
# 
# Sampling interval:
# 
# k = 1000 / 100
# k = 10
# 
# The company can select every 10th customer after choosing a starting point.
# 
# ### AI/ML Example
# 
# Suppose a company has a large dataset containing customer records.
# 
# Instead of processing every record manually, we can select records at a fixed interval to create a sample for initial data analysis.
# 
# ### Python Implementation
# 
# Python can be used to select every k-th item from a list.

# In[4]:


customers = list(range(1, 21))

sample_size = 5
sampling_interval = len(customers) // sample_size

start = 2

sample = customers[start - 1::sampling_interval]

print("Customers:", customers)
print("Sampling Interval:", sampling_interval)
print("Selected Sample:", sample)


# # Sampling Error
# 
# ### Definition
# 
# Sampling Error is the difference between the result obtained from a sample and the actual value of the entire population.
# 
# It happens because we study only a sample instead of the complete population.
# 
# ### Formula
# 
# Sampling Error = Sample Statistic - Population Parameter
# 
# For the absolute difference:
# 
# Sampling Error = |Sample Value - Population Value|
# 
# ### Numerical Example
# 
# Suppose the average salary of all employees in a company is:
# 
# Population Mean = ₹50,000
# 
# We select a sample of employees and calculate:
# 
# Sample Mean = ₹47,000
# 
# Sampling Error:
# 
# = |47,000 - 50,000|
# = ₹3,000
# 
# So, the sampling error is ₹3,000.
# 
# ### Business Example
# 
# A company has 10,000 customers.
# 
# The actual average customer spending is ₹2,000.
# 
# The company surveys only some customers and gets an average spending of ₹1,850.
# 
# The difference between these two values is sampling error.
# 
# ### AI/ML Example
# 
# Suppose a company has a large customer dataset.
# 
# Instead of using the complete population, a sample is selected to analyze customer behavior.
# 
# The statistics calculated from the sample may differ from the statistics of the complete dataset.
# 
# This difference is called sampling error.
# 
# ### Python Implementation
# 
# Python can be used to calculate the difference between the population value and sample value.

# In[5]:


population_mean = 50000
sample_mean = 47000

sampling_error = abs(sample_mean - population_mean)

print("Population Mean:", population_mean)
print("Sample Mean:", sample_mean)
print("Sampling Error:", sampling_error)


# # Sample Size
# 
# ### Definition
# 
# Sample Size means the total number of observations or members selected from a population for a study.
# 
# For example, if a company has 10,000 customers and selects 500 customers for a survey, then the sample size is 500.
# 
# ### Formula
# 
# One simple formula used to estimate sample size is:
# 
# n = N / (1 + N × e²)
# 
# Where:
# 
# N = Population size
# n = Sample size
# e = Acceptable margin of error
# 
# This is one simple sample-size formula. The appropriate formula can change depending on the study and requirements.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Population size (N) = 1000
# Margin of error (e) = 0.05
# 
# n = 1000 / (1 + 1000 × 0.05²)
# 
# n = 1000 / (1 + 1000 × 0.0025)
# 
# n = 1000 / 3.5
# 
# n ≈ 285.71
# 
# So, the required sample size is approximately 286.
# 
# ### Business Example
# 
# A company has 10,000 customers and wants to understand customer satisfaction.
# 
# Instead of asking all 10,000 customers, the company can select an appropriate sample size and collect feedback from those customers.
# 
# ### AI/ML Example
# 
# In machine learning, a dataset may contain millions of records.
# 
# A sample can be selected for exploratory data analysis, testing data-processing methods, or initial experiments.
# 
# Choosing an appropriate sample size helps balance the amount of data with the time and resources required for analysis.
# 
# ### Python Implementation
# 
# Python can be used to calculate the sample size using the formula above.

# In[6]:


population_size = 1000
margin_of_error = 0.05

sample_size = population_size / (
    1 + population_size * margin_of_error ** 2
)

print("Population Size:", population_size)
print("Margin of Error:", margin_of_error)
print("Calculated Sample Size:", sample_size)
print("Required Sample Size:", round(sample_size))


# In[ ]:




