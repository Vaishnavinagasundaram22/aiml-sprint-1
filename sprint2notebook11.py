#!/usr/bin/env python
# coding: utf-8

# # T-Test
# 
# ### Definition
# 
# A T-Test is a statistical test used to compare the mean of one or more groups and determine whether there is a significant difference.
# 
# It is commonly used when the sample size is small and the population standard deviation is unknown.
# 
# ### Assumptions
# 
# - The data should be numerical.
# - The observations should be independent.
# - The data should be approximately normally distributed.
# - For an independent T-Test, the groups should be independent.
# 
# ### When to Use
# 
# A T-Test is used when we want to compare means and find out whether the difference is statistically significant.
# 
# ### When Not to Use
# 
# A T-Test should not be used when the data does not meet its assumptions or when the data is strongly non-normal.
# 
# ### Types of T-Test
# 
# 1. One-Sample T-Test
# 2. Independent T-Test
# 3. Paired T-Test
# 
# ### Business Example
# 
# A company can use a T-Test to check whether the average sales before and after a new marketing strategy are significantly different.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, a T-Test can be used to compare the means of two groups and check whether their difference is statistically significant.
# 
# ### Numerical Example
# 
# Suppose the expected average mark is 50.
# 
# Sample marks:
# 
# 52, 51, 49, 50, 53, 48
# 
# We can use a One-Sample T-Test to check whether the sample mean is significantly different from 50.
# 
# ### Python Implementation
# 
# The following program performs a One-Sample T-Test.
# 
# ### Interpretation
# 
# The p-value is compared with the significance level, usually 0.05.
# 
# If p-value < 0.05, we reject the Null Hypothesis.
# 
# If p-value >= 0.05, we do not reject the Null Hypothesis.

# In[1]:


from scipy import stats

sample = [52, 51, 49, 50, 53, 48]

hypothesized_mean = 50

t_statistic, p_value = stats.ttest_1samp(
    sample,
    hypothesized_mean
)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Z-Test
# 
# ### Definition
# 
# A Z-Test is a statistical test used to determine whether there is a significant difference between a sample mean and a population mean, or between two sample means.
# 
# It is generally used when the population standard deviation is known or when the sample size is large.
# 
# ### Assumptions
# 
# - The data should be numerical.
# - Observations should be independent.
# - The data should be approximately normally distributed.
# - Population standard deviation should be known for a standard one-sample Z-Test.
# - The sample size is generally large.
# 
# ### When to Use
# 
# A Z-Test is used when we want to compare means and the population standard deviation is known or the sample size is sufficiently large.
# 
# ### When Not to Use
# 
# A Z-Test should not be used when the population standard deviation is unknown and the sample size is small. In such cases, a T-Test is generally more appropriate.
# 
# ### Business Example
# 
# A company can use a Z-Test to check whether the average delivery time is significantly different from the expected delivery time when the population standard deviation is known.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, a Z-Test can be used to compare sample statistics with a known population value.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Sample Mean = 52
# 
# Population Mean = 50
# 
# Population Standard Deviation = 10
# 
# Sample Size = 100
# 
# The Z-Test can be used to determine whether the sample mean is significantly different from the population mean.
# 
# ### Python Implementation
# 
# The following program calculates the Z-Statistic and p-value.
# 
# ### Interpretation
# 
# If p-value < 0.05, we reject the Null Hypothesis.
# 
# If p-value >= 0.05, we do not reject the Null Hypothesis.

# In[2]:


import numpy as np
from scipy import stats

sample = [52, 51, 49, 50, 53, 48, 51, 52, 50, 49]

population_mean = 50
population_std = 10

sample_mean = np.mean(sample)
sample_size = len(sample)

z_statistic = (sample_mean - population_mean) / (
    population_std / np.sqrt(sample_size)
)

p_value = 2 * (1 - stats.norm.cdf(abs(z_statistic)))

print("Z-Statistic:", z_statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Chi-Square Test
# 
# ### Definition
# 
# The Chi-Square Test is a statistical test used to determine whether there is a significant relationship between categorical variables.
# 
# It compares the observed values with the expected values.
# 
# ### Assumptions
# 
# - The data should be categorical.
# - Observations should be independent.
# - The categories should be mutually exclusive.
# - Expected frequency in each cell should generally be sufficiently large.
# 
# ### When to Use
# 
# The Chi-Square Test is used when we want to check whether two categorical variables are related.
# 
# It can also be used to compare observed frequencies with expected frequencies.
# 
# ### When Not to Use
# 
# The Chi-Square Test should not be used when the observations are not independent or when the expected frequencies are too small.
# 
# ### Types
# 
# 1. Chi-Square Test of Independence
# 2. Chi-Square Goodness of Fit Test
# 
# ### Business Example
# 
# A company can use a Chi-Square Test to check whether customer age group is related to product preference.
# 
# ### AI/ML Example
# 
# In AI/ML, the Chi-Square Test can be used for feature selection when working with categorical features.
# 
# ### Numerical Example
# 
# Suppose a company wants to check whether gender and product preference are related.
# 
# | Gender | Product A | Product B |
# |--------|-----------|-----------|
# | Male   | 30        | 20        |
# | Female | 20        | 30        |
# 
# A Chi-Square Test can be used to test whether gender and product preference are independent.
# 
# ### Python Implementation
# 
# The following program performs a Chi-Square Test of Independence.
# 
# ### Interpretation
# 
# If p-value < 0.05, we reject the Null Hypothesis and conclude that there is a statistically significant association between the variables.
# 
# If p-value >= 0.05, we do not reject the Null Hypothesis.

# In[3]:


from scipy.stats import chi2_contingency

data = [
    [30, 20],
    [20, 30]
]

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(data)

print("Chi-Square Value:", chi2)
print("P-Value:", p_value)
print("Degrees of Freedom:", degrees_of_freedom)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # ANOVA
# 
# ### Definition
# 
# ANOVA stands for Analysis of Variance.
# 
# ANOVA is a statistical test used to compare the means of three or more groups and determine whether there is a statistically significant difference between them.
# 
# ### Assumptions
# 
# - The dependent variable should be numerical.
# - The observations should be independent.
# - The data in each group should be approximately normally distributed.
# - The groups should have similar variances.
# 
# ### When to Use
# 
# ANOVA is used when we want to compare the means of three or more independent groups.
# 
# ### When Not to Use
# 
# ANOVA should not be used when the observations are not independent or when the data strongly violates the assumptions.
# 
# ### Business Example
# 
# A company can use ANOVA to compare the average sales generated by three different marketing strategies.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, ANOVA can be used to determine whether different groups have significantly different mean values.
# 
# ### Numerical Example
# 
# Suppose the marks of students from three classes are:
# 
# Class A: 70, 72, 68, 71
# 
# Class B: 80, 82, 79, 81
# 
# Class C: 75, 77, 74, 76
# 
# ANOVA can be used to check whether the average marks of these three classes are significantly different.
# 
# ### Python Implementation
# 
# The following program performs a one-way ANOVA test.
# 
# ### Interpretation
# 
# If p-value < 0.05, we reject the Null Hypothesis and conclude that at least one group mean is significantly different.
# 
# If p-value >= 0.05, we do not reject the Null Hypothesis.

# In[4]:


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

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Mann-Whitney U Test
# 
# ### Definition
# 
# The Mann-Whitney U Test is a non-parametric statistical test used to compare two independent groups.
# 
# It is an alternative to the Independent T-Test when the data does not meet the assumptions required for a T-Test.
# 
# ### Assumptions
# 
# - The two groups should be independent.
# - The data should be at least ordinal.
# - The observations should be independent within and between groups.
# - The two groups should have a similar distribution if the test is being used to compare their locations.
# 
# ### When to Use
# 
# The Mann-Whitney U Test is used when comparing two independent groups, especially when the data is not normally distributed or contains ordinal values.
# 
# ### When Not to Use
# 
# It should not be used for paired or repeated measurements. For paired data, a Wilcoxon signed-rank test is more appropriate.
# 
# ### Business Example
# 
# A company can use the Mann-Whitney U Test to compare customer satisfaction scores between two independent groups.
# 
# ### AI/ML Example
# 
# In AI/ML and data analysis, it can be used to compare numerical or ordinal measurements between two independent groups when normality assumptions are not suitable.
# 
# ### Numerical Example
# 
# Suppose customer satisfaction scores are collected from two independent groups:
# 
# Group A: 7, 8, 6, 7, 9
# 
# Group B: 5, 6, 4, 6, 5
# 
# The Mann-Whitney U Test can be used to check whether the two groups differ significantly.
# 
# ### Python Implementation
# 
# The following program performs a Mann-Whitney U Test.
# 
# ### Interpretation
# 
# If p-value < 0.05, we reject the Null Hypothesis.
# 
# If p-value >= 0.05, we do not reject the Null Hypothesis.

# In[5]:


from scipy.stats import mannwhitneyu

group_a = [7, 8, 6, 7, 9]
group_b = [5, 6, 4, 6, 5]

u_statistic, p_value = mannwhitneyu(
    group_a,
    group_b,
    alternative="two-sided"
)

print("U-Statistic:", u_statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Do not reject the Null Hypothesis")


# # Shapiro-Wilk Test
# 
# ### Definition
# 
# The Shapiro-Wilk Test is a statistical test used to check whether a dataset is approximately normally distributed.
# 
# ### Assumptions
# 
# - The data should be numerical.
# - The observations should be independent.
# - The test is mainly useful for checking the normality of numerical data.
# 
# ### When to Use
# 
# The Shapiro-Wilk Test is used when we want to check whether data follows a normal distribution before applying statistical methods that assume normality.
# 
# ### When Not to Use
# 
# - It is not used for categorical data.
# - For very large datasets, the test may detect very small differences from normality, so visual checks can also be useful.
# 
# ### Business Example
# 
# A company wants to check whether customer response times are normally distributed before applying a statistical method that requires normally distributed data.
# 
# ### AI/ML Example
# 
# In AI/ML, the Shapiro-Wilk Test can be used to check whether a numerical feature or model residuals are approximately normally distributed when normality is relevant to the chosen method.
# 
# ### Numerical Example
# 
# Consider the following data:
# 
# 10, 12, 11, 13, 12, 14, 11, 13
# 
# We can use the Shapiro-Wilk Test to check whether these values are approximately normally distributed.
# 
# ### Python Implementation
# 
# The `shapiro()` function from SciPy is used to perform the Shapiro-Wilk Test.
# 
# ### Interpretation
# 
# - If p-value > 0.05, we do not reject the Null Hypothesis. The data does not show significant evidence against normality.
# - If p-value <= 0.05, we reject the Null Hypothesis. The data shows evidence that it is not normally distributed.

# In[6]:


from scipy.stats import shapiro

data = [10, 12, 11, 13, 12, 14, 11, 13]

statistic, p_value = shapiro(data)

print("Shapiro-Wilk Statistic:", statistic)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Data is not normally distributed")
else:
    print("Do not reject the Null Hypothesis")
    print("Data is approximately normally distributed")


# In[ ]:




