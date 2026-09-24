#!/usr/bin/env python
# coding: utf-8

# # Null Hypothesis
# 
# ### Definition
# 
# The Null Hypothesis is a statement that says there is no significant difference or relationship between the variables being studied.
# 
# It is usually represented by H₀.
# 
# ### Simple Example
# 
# Suppose a company introduces a new training program.
# 
# Null Hypothesis:
# 
# "The new training program does not improve employee performance."
# 
# ### Business Example
# 
# A company may use a Null Hypothesis to check whether a new marketing strategy has actually increased sales.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, hypothesis testing can be used to check whether an observed difference in data is statistically significant.
# 
# ### Python Implementation
# 
# The following example demonstrates a simple hypothesis testing concept using a sample of values.

# In[1]:


import numpy as np
from scipy import stats

sample = [52, 51, 49, 50, 53, 48, 51, 52, 50, 49]

hypothesized_mean = 50

t_statistic, p_value = stats.ttest_1samp(sample, hypothesized_mean)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# # Alternative Hypothesis
# 
# ### Definition
# 
# The Alternative Hypothesis is a statement that says there is a significant difference or relationship between the variables being studied.
# 
# It is usually represented by H₁ or Hₐ.
# 
# ### Simple Example
# 
# Suppose a company introduces a new training program.
# 
# Alternative Hypothesis:
# 
# "The new training program improves employee performance."
# 
# ### Business Example
# 
# A company can use the Alternative Hypothesis to test whether a new marketing strategy increases sales.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, the Alternative Hypothesis can be used to check whether a change observed in the data is statistically significant.
# 
# ### Python Implementation
# 
# The following program uses a one-sample t-test to test whether the sample mean is different from 50.

# In[2]:


import numpy as np
from scipy import stats

sample = [52, 51, 49, 50, 53, 48, 51, 52, 50, 49]

hypothesized_mean = 50

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# # p-value
# 
# ### Definition
# 
# The p-value is a value used in hypothesis testing to determine how strong the evidence is against the Null Hypothesis.
# 
# A smaller p-value indicates stronger evidence against the Null Hypothesis.
# 
# ### Simple Example
# 
# If the p-value is 0.03, it means the result is statistically significant at a 5% significance level because 0.03 is less than 0.05.
# 
# ### Business Example
# 
# A company can use a p-value to check whether a new marketing strategy has produced a statistically significant change in sales.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, p-values can be used to determine whether an observed relationship or difference in data is statistically significant.
# 
# ### Python Implementation
# 
# The following program performs a one-sample t-test and displays the p-value.

# In[3]:


from scipy import stats

sample = [52, 51, 49, 50, 53, 48, 51, 52, 50, 49]

t_statistic, p_value = stats.ttest_1samp(sample, 50)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# # Significance Level
# 
# ### Definition
# 
# Significance Level is the limit used to decide whether a result is statistically significant in hypothesis testing.
# 
# It is usually represented by α (alpha).
# 
# A commonly used significance level is 0.05 or 5%.
# 
# ### Simple Example
# 
# If:
# 
# p-value < 0.05
# 
# the result is considered statistically significant.
# 
# If:
# 
# p-value >= 0.05
# 
# the result is not considered statistically significant.
# 
# ### Business Example
# 
# A company can use a 5% significance level to test whether a new advertisement has produced a significant change in sales.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, the significance level helps decide whether an observed difference or relationship is statistically significant.
# 
# ### Python Implementation
# 
# The following program compares the p-value with a significance level of 0.05.

# In[4]:


from scipy import stats

sample = [52, 51, 49, 50, 53, 48, 51, 52, 50, 49]

t_statistic, p_value = stats.ttest_1samp(sample, 50)

significance_level = 0.05

print("P-Value:", p_value)

if p_value < significance_level:
    print("Result is statistically significant")
else:
    print("Result is not statistically significant")


# # Type I Error
# 
# ### Definition
# 
# Type I Error occurs when we reject the Null Hypothesis even though the Null Hypothesis is actually true.
# 
# It is also called a false positive.
# 
# ### Simple Example
# 
# Suppose a company tests whether a new training program improves employee performance.
# 
# Null Hypothesis:
# 
# "The training program does not improve performance."
# 
# If the test says that the training program improves performance when it actually does not, this is a Type I Error.
# 
# ### Business Example
# 
# A company may conclude that a new advertisement increases sales when there is actually no real improvement.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, Type I Error can happen when we identify a relationship or difference as significant when it is actually not significant.
# 
# ### Python Implementation
# 
# The following example demonstrates the idea of a Type I Error using a hypothesis test.

# In[5]:


from scipy import stats

sample = [50, 51, 49, 50, 52, 48, 51, 50, 49, 51]

t_statistic, p_value = stats.ttest_1samp(sample, 50)

significance_level = 0.05

print("P-Value:", p_value)

if p_value < significance_level:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Type II Error
# 
# ### Definition
# 
# Type II Error occurs when we do not reject the Null Hypothesis even though the Null Hypothesis is actually false.
# 
# It is also called a false negative.
# 
# ### Simple Example
# 
# Suppose a company tests whether a new training program improves employee performance.
# 
# Null Hypothesis:
# 
# "The training program does not improve performance."
# 
# If the training program actually improves performance, but the test fails to identify the improvement, this is a Type II Error.
# 
# ### Business Example
# 
# A company may conclude that a new marketing strategy does not increase sales when it actually does.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, Type II Error can happen when a real relationship or difference exists but the statistical test fails to detect it.
# 
# ### Python Implementation
# 
# The following example demonstrates the decision made using a hypothesis test.

# In[6]:


from scipy import stats

sample = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

t_statistic, p_value = stats.ttest_1samp(sample, 50)

significance_level = 0.05

print("P-Value:", p_value)

if p_value < significance_level:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # One-Tailed Test
# 
# ### Definition
# 
# A One-Tailed Test is a hypothesis test used when we want to check whether a value is significantly greater than or significantly less than a specific value.
# 
# It tests the result in only one direction.
# 
# ### Types
# 
# 1. Right-Tailed Test – checks whether the value is greater than a specific value.
# 2. Left-Tailed Test – checks whether the value is less than a specific value.
# 
# ### Numerical Example
# 
# Suppose the average delivery time is expected to be 30 minutes.
# 
# We want to check whether the new system reduces the delivery time.
# 
# Null Hypothesis (H₀):
# 
# The average delivery time is 30 minutes or more.
# 
# Alternative Hypothesis (H₁):
# 
# The average delivery time is less than 30 minutes.
# 
# This is a Left-Tailed Test.
# 
# ### Business Example
# 
# A company can use a One-Tailed Test to check whether a new process reduces production time.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, a One-Tailed Test can be used when the expected change has a specific direction, such as checking whether a new method increases model performance.
# 
# ### Python Implementation
# 
# The following program performs a left-tailed one-sample t-test.

# In[7]:


from scipy import stats

sample = [27, 28, 29, 26, 28, 27, 29, 28, 26, 27]

hypothesized_mean = 30

t_statistic, p_value_two_tailed = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

p_value_one_tailed = p_value_two_tailed / 2

print("T-Statistic:", t_statistic)
print("One-Tailed P-Value:", p_value_one_tailed)

if t_statistic < 0 and p_value_one_tailed < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Two-Tailed Test
# 
# ### Definition
# 
# A Two-Tailed Test is a hypothesis test used when we want to check whether a value is significantly different from a specific value.
# 
# It checks both directions: greater than and less than.
# 
# ### Numerical Example
# 
# Suppose the average delivery time is expected to be 30 minutes.
# 
# Null Hypothesis (H₀):
# 
# The average delivery time is 30 minutes.
# 
# Alternative Hypothesis (H₁):
# 
# The average delivery time is not 30 minutes.
# 
# This is a Two-Tailed Test because we are checking for a difference in either direction.
# 
# ### Business Example
# 
# A company can use a Two-Tailed Test to check whether a new process changes the average production time.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, a Two-Tailed Test can be used to check whether a feature or measurement is significantly different from an expected value.
# 
# ### Python Implementation
# 
# The following program performs a two-tailed one-sample t-test.

# In[8]:


from scipy import stats

sample = [32, 31, 29, 30, 33, 28, 31, 32, 30, 29]

hypothesized_mean = 30

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("T-Statistic:", t_statistic)
print("Two-Tailed P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # T-Test
# 
# ### Definition
# 
# A T-Test is a statistical test used to compare the means of data and determine whether there is a significant difference between them.
# 
# It is commonly used when the sample size is small or the population standard deviation is unknown.
# 
# ### Types of T-Test
# 
# 1. One-Sample T-Test
# 2. Independent Two-Sample T-Test
# 3. Paired T-Test
# 
# ### Numerical Example
# 
# Suppose we want to check whether the average marks of students are significantly different from 50.
# 
# Sample marks:
# 
# 52, 51, 49, 50, 53, 48
# 
# We can use a One-Sample T-Test for this comparison.
# 
# ### Business Example
# 
# A company can use a T-Test to compare the average sales before and after a new marketing strategy.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, a T-Test can be used to compare groups and check whether the difference between their means is statistically significant.
# 
# ### Python Implementation
# 
# The following program performs a One-Sample T-Test.

# In[9]:


from scipy import stats

sample = [52, 51, 49, 50, 53, 48]

hypothesized_mean = 50

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# # Chi-Square Test
# 
# ### Definition
# 
# The Chi-Square Test is a statistical test used to find whether there is a significant relationship between categorical variables.
# 
# It compares the observed values with the expected values.
# 
# ### Types
# 
# 1. Chi-Square Test of Independence
# 2. Chi-Square Goodness of Fit Test
# 
# ### Numerical Example
# 
# Suppose we want to check whether gender and product preference are related.
# 
# | Gender | Product A | Product B |
# |--------|-----------|-----------|
# | Male   | 30        | 20        |
# | Female | 20        | 30        |
# 
# A Chi-Square Test can be used to check whether gender and product preference are related.
# 
# ### Business Example
# 
# A company can use a Chi-Square Test to check whether customer age group is related to product preference.
# 
# ### AI/ML Example
# 
# In AI/ML, the Chi-Square Test can be used for feature selection when working with categorical features.
# 
# ### Python Implementation
# 
# The following program performs a Chi-Square Test of Independence.

# In[10]:


from scipy.stats import chi2_contingency

data = [
    [30, 20],
    [20, 30]
]

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(data)

print("Chi-Square Value:", chi2)
print("P-Value:", p_value)
print("Degrees of Freedom:", degrees_of_freedom)
print("Expected Values:")
print(expected)


# # ANOVA
# 
# ### Definition
# 
# ANOVA stands for Analysis of Variance.
# 
# It is a statistical test used to compare the means of three or more groups and determine whether there is a significant difference between them.
# 
# ### Numerical Example
# 
# Suppose we have the marks of students from three different classes:
# 
# Class A: 70, 72, 68, 71
# 
# Class B: 80, 82, 79, 81
# 
# Class C: 75, 77, 74, 76
# 
# ANOVA can be used to check whether the average marks of these three classes are significantly different.
# 
# ### Business Example
# 
# A company can use ANOVA to compare the average sales generated by three different marketing strategies.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, ANOVA can be used to determine whether different groups have significantly different mean values.
# 
# ### Python Implementation
# 
# The following program performs a one-way ANOVA test for three groups.

# In[11]:


from scipy.stats import f_oneway

group_a = [70, 72, 68, 71]
group_b = [80, 82, 79, 81]
group_c = [75, 77, 74, 76]

f_statistic, p_value = f_oneway(
    group_a,
    group_b,
    group_c
)

print("F-Statistic:", f_statistic)
print("P-Value:", p_value)

