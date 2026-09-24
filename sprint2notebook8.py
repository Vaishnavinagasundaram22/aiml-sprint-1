#!/usr/bin/env python
# coding: utf-8

# # Correlation
# 
# ### Definition
# 
# Correlation is a statistical measure that shows the relationship between two variables.
# 
# It tells us whether two variables move together and how strongly they are related.
# 
# The correlation value usually ranges from -1 to +1.
# 
# +1 → Perfect positive relationship
# 0 → No linear relationship
# -1 → Perfect negative relationship
# 
# ### Formula
# 
# Pearson Correlation:
# 
# r = Cov(X, Y) / (σX × σY)
# 
# Where:
# 
# r = Correlation coefficient
# Cov(X, Y) = Covariance between X and Y
# σX = Standard deviation of X
# σY = Standard deviation of Y
# 
# ### Numerical Example
# 
# Suppose we have:
# 
# Study Hours: 1, 2, 3, 4, 5
# Marks:       20, 30, 40, 50, 60
# 
# As study hours increase, marks also increase.
# 
# So, these two variables have a positive correlation.
# 
# ### Business Example
# 
# A company can study the relationship between:
# 
# Advertising Spending and Sales
# 
# If advertising spending increases and sales also increase, they may have a positive correlation.
# 
# ### AI/ML Example
# 
# In machine learning, correlation can be used to understand relationships between features.
# 
# For example:
# 
# House Size and House Price
# 
# If larger houses generally have higher prices, these two variables may have a positive correlation.
# 
# Correlation can also help identify features that may be useful for a machine learning model.
# 
# ### Python Implementation
# 
# We can use Pandas to calculate the correlation between two variables.

# In[1]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

correlation = df["Study_Hours"].corr(df["Marks"])

print(df)
print("Correlation:", correlation)


# ### Interpretation
# 
# The correlation value is 1.0.
# 
# This means Study Hours and Marks have a perfect positive linear relationship in this example.
# 
# As study hours increase, marks also increase in a consistent pattern.
# 
# In AI/ML, correlation can help us understand relationships between variables and identify potentially related features.

# # Covariance
# 
# ### Definition
# 
# Covariance is a statistical measure that shows the direction of the relationship between two variables.
# 
# It tells us whether two variables tend to increase together or whether one increases while the other decreases.
# 
# ### Formula
# 
# Covariance:
# 
# Cov(X, Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / n
# 
# Where:
# 
# Xi = Individual value of X
# Yi = Individual value of Y
# X̄ = Mean of X
# Ȳ = Mean of Y
# n = Number of observations
# 
# ### Numerical Example
# 
# Suppose:
# 
# Study Hours = [1, 2, 3]
# Marks = [20, 30, 40]
# 
# When Study Hours increase, Marks also increase.
# 
# Therefore, the covariance will be positive.
# 
# If one variable increases while the other decreases, covariance will generally be negative.
# 
# ### Business Example
# 
# A company can study:
# 
# Advertising Spending
# Sales
# 
# If advertising spending increases and sales also increase, the covariance between them will be positive.
# 
# ### AI/ML Example
# 
# Covariance can be used to understand how features change together.
# 
# For example:
# 
# Temperature and Ice Cream Sales
# 
# If temperature increases and ice cream sales also increase, they can have positive covariance.
# 
# Covariance is also an important concept used in methods such as PCA.
# 
# ### Python Implementation
# 
# Pandas can be used to calculate covariance between two variables.

# In[2]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3],
    "Marks": [20, 30, 40]
}

df = pd.DataFrame(data)

covariance = df["Study_Hours"].cov(df["Marks"])

print(df)
print("Covariance:", covariance)


# ### Interpretation
# 
# The covariance is positive (10.0).
# 
# This means Study Hours and Marks tend to increase together.
# 
# A positive covariance indicates that the variables generally move in the same direction.
# 
# A negative covariance indicates that the variables generally move in opposite directions.
# 
# The size of covariance depends on the units of the variables, so covariance is mainly useful for understanding direction rather than directly comparing relationship strength.
# 
# Correlation is easier to interpret because its value is always between -1 and +1.

# # Positive Correlation
# 
# ### Definition
# 
# Positive Correlation occurs when two variables generally move in the same direction.
# 
# When one variable increases, the other variable also tends to increase.
# 
# Similarly, when one variable decreases, the other variable also tends to decrease.
# 
# ### Formula
# 
# The correlation coefficient is represented by:
# 
# r
# 
# For positive correlation:
# 
# 0 < r ≤ 1
# 
# r = +1 means a perfect positive correlation.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Study Hours = [1, 2, 3, 4, 5]
# Marks = [20, 30, 40, 50, 60]
# 
# As Study Hours increase, Marks also increase.
# 
# Therefore, the variables have a positive correlation.
# 
# ### Business Example
# 
# A company can compare:
# 
# Advertising Spending and Sales
# 
# If advertising spending increases and sales also tend to increase, these variables have a positive correlation.
# 
# ### AI/ML Example
# 
# In a house-price dataset:
# 
# House Size and House Price
# 
# Generally, when house size increases, house price may also increase.
# 
# Therefore, these two features can show positive correlation.
# 
# Correlation can help us understand relationships between features before building a machine learning model.
# 
# ### Python Implementation
# 
# We can use Pandas to calculate the correlation coefficient between two variables.

# In[3]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

correlation = df["Study_Hours"].corr(df["Marks"])

print("Correlation:", correlation)


# ### Interpretation
# 
# The correlation value is 1.0.
# 
# This indicates a perfect positive linear relationship in this example.
# 
# As Study Hours increase, Marks also increase consistently.
# 
# Therefore, Study Hours and Marks have a positive correlation.

# # Negative Correlation
# 
# ### Definition
# 
# Negative Correlation occurs when two variables generally move in opposite directions.
# 
# When one variable increases, the other variable tends to decrease.
# 
# Similarly, when one variable decreases, the other tends to increase.
# 
# ### Formula
# 
# The correlation coefficient is represented by:
# 
# r
# 
# For negative correlation:
# 
# -1 ≤ r < 0
# 
# r = -1 means a perfect negative correlation.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Exercise Hours = [1, 2, 3, 4, 5]
# Weight = [80, 75, 70, 65, 60]
# 
# As Exercise Hours increase, Weight decreases.
# 
# Therefore, these variables have a negative correlation.
# 
# ### Business Example
# 
# A company can study:
# 
# Product Price and Number of Customers
# 
# If the price of a product increases and the number of customers tends to decrease, these variables may have a negative correlation.
# 
# ### AI/ML Example
# 
# In a machine learning dataset, suppose:
# 
# Distance to a Store and Number of Visits
# 
# If customers living farther away tend to visit the store less frequently, these variables may have a negative correlation.
# 
# Correlation can help us understand relationships between features before building a machine learning model.
# 
# ### Python Implementation
# 
# We can use Pandas to calculate the correlation coefficient.

# In[4]:


import pandas as pd

data = {
    "Exercise_Hours": [1, 2, 3, 4, 5],
    "Weight": [80, 75, 70, 65, 60]
}

df = pd.DataFrame(data)

correlation = df["Exercise_Hours"].corr(df["Weight"])

print(df)
print("Correlation:", correlation)


# # No Correlation
# 
# ### Definition
# 
# No Correlation means there is no clear linear relationship between two variables.
# 
# A change in one variable does not show a consistent linear change in the other variable.
# 
# ### Formula
# 
# The correlation coefficient is represented by:
# 
# r
# 
# For no linear correlation:
# 
# r ≈ 0
# 
# A value close to 0 means there is little or no linear relationship between the variables.
# 
# ### Numerical Example
# 
# Suppose:
# 
# Study Hours = [1, 2, 3, 4, 5]
# Shoe Size = [7, 9, 6, 10, 8]
# 
# There is no clear pattern between Study Hours and Shoe Size.
# 
# Therefore, these variables may have little or no linear correlation.
# 
# ### Business Example
# 
# A company may compare:
# 
# Employee ID and Monthly Sales
# 
# Employee ID is just an identification number. It does not normally have a meaningful linear relationship with sales.
# 
# ### AI/ML Example
# 
# In a machine learning dataset, some features may have little or no linear relationship with each other.
# 
# Checking correlation can help us understand which numerical features are related and which are not.
# 
# ### Python Implementation
# 
# We can use Pandas to calculate the correlation coefficient.

# In[5]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Shoe_Size": [7, 9, 6, 10, 8]
}

df = pd.DataFrame(data)

correlation = df["Study_Hours"].corr(df["Shoe_Size"])

print(df)
print("Correlation:", correlation)


# # Pearson Correlation
# 
# ### Definition
# 
# Pearson Correlation is a statistical method used to measure the strength and direction of the linear relationship between two numerical variables.
# 
# The correlation value ranges from -1 to +1.
# 
# +1 → Perfect positive correlation
# 0 → No linear correlation
# -1 → Perfect negative correlation
# 
# ### Formula
# 
# r = Cov(X, Y) / (σX × σY)
# 
# Where:
# 
# r = Pearson correlation coefficient
# Cov(X, Y) = Covariance between X and Y
# σX = Standard deviation of X
# σY = Standard deviation of Y
# 
# ### Numerical Example
# 
# Suppose:
# 
# Study Hours = [1, 2, 3, 4, 5]
# Marks = [20, 30, 40, 50, 60]
# 
# As Study Hours increase, Marks also increase.
# 
# Therefore, the Pearson correlation is +1, which shows a perfect positive linear relationship.
# 
# ### Business Example
# 
# A company can use Pearson Correlation to study the relationship between advertising spending and sales.
# 
# If advertising spending increases and sales also increase, they may have a positive correlation.
# 
# ### AI/ML Example
# 
# Pearson Correlation can be used to understand the relationship between numerical features.
# 
# For example:
# 
# House Size and House Price
# 
# If larger houses generally have higher prices, these variables may have a positive Pearson correlation.
# 
# ### Python Implementation
# 
# Pandas provides the corr() function to calculate the Pearson correlation between numerical variables.

# In[6]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

pearson_correlation = df["Study_Hours"].corr(df["Marks"])

print("Pearson Correlation:", pearson_correlation)


# # Spearman Correlation
# 
# ### Definition
# 
# Spearman Correlation is a statistical method used to measure the strength and direction of a relationship between two variables based on their ranks.
# 
# It is useful when the relationship is not necessarily linear but the variables generally move in the same or opposite order.
# 
# ### Formula
# 
# Spearman's Rank Correlation:
# 
# ρ = 1 - (6Σd² / n(n² - 1))
# 
# Where:
# 
# ρ = Spearman correlation coefficient
# d = Difference between the ranks
# n = Number of observations
# 
# The value ranges from -1 to +1.
# 
# +1 → Perfect positive relationship
# 0 → No monotonic relationship
# -1 → Perfect negative relationship
# 
# ### Numerical Example
# 
# Suppose:
# 
# Study Hours = [1, 2, 3, 4, 5]
# Marks = [20, 30, 40, 50, 60]
# 
# Both variables have the same ranking.
# 
# Therefore, the Spearman correlation is +1.
# 
# ### Business Example
# 
# A company can compare:
# 
# Customer Satisfaction Rank and Purchase Frequency Rank.
# 
# Spearman Correlation can be used to check whether customers with higher satisfaction rankings also tend to have higher purchase-frequency rankings.
# 
# ### AI/ML Example
# 
# Spearman Correlation can be useful when numerical data is based on rankings or when the relationship is monotonic but not necessarily linear.
# 
# For example, it can be used to study the relationship between feature rankings and model-related measurements.
# 
# ### Python Implementation
# 
# Pandas can calculate Spearman Correlation using the method="spearman" parameter.

# In[7]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

spearman_correlation = df["Study_Hours"].corr(
    df["Marks"],
    method="spearman"
)

print("Spearman Correlation:", spearman_correlation)


# # Correlation Matrix
# 
# ### Definition
# 
# A Correlation Matrix is a table that shows the correlation values between multiple numerical variables.
# 
# Each value shows the strength and direction of the relationship between two variables.
# 
# The values range from -1 to +1.
# 
# +1 → Perfect positive correlation
# 0 → No linear correlation
# -1 → Perfect negative correlation
# 
# ### Numerical Example
# 
# Suppose we have three variables:
# 
# Study Hours
# Marks
# Attendance
# 
# A correlation matrix can show the relationship between every pair of these variables.
# 
# ### Business Example
# 
# A company can use a correlation matrix to study relationships between:
# 
# Advertising
# Sales
# Profit
# 
# This helps understand how these numerical variables are related.
# 
# ### AI/ML Example
# 
# In machine learning, a correlation matrix can be used to understand relationships between features.
# 
# It can help identify highly correlated features before building a model.
# 
# ### Python Implementation
# 
# Pandas can create a correlation matrix using the corr() function.

# In[8]:


import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60],
    "Attendance": [60, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)


# # Heatmap
# 
# ### Definition
# 
# A Heatmap is a visual representation of data using different shades or colors.
# 
# In correlation analysis, a heatmap is used to display a correlation matrix visually.
# 
# It makes it easier to identify strong positive and negative relationships between variables.
# 
# ### Numerical Example
# 
# Suppose the correlation between two variables is:
# 
# Study Hours and Marks = +0.95
# 
# This indicates a strong positive correlation.
# 
# A heatmap represents this correlation using a color scale, making the relationship easy to identify.
# 
# ### Business Example
# 
# A company can use a heatmap to visualize the relationships between:
# 
# Advertising
# Sales
# Profit
# Customer Spending
# 
# This helps the company quickly identify relationships between variables.
# 
# ### AI/ML Example
# 
# In machine learning, a correlation heatmap can be used during Exploratory Data Analysis (EDA).
# 
# It can help identify highly correlated features and understand relationships between numerical features.
# 
# ### Python Implementation
# 
# Seaborn can be used to create a heatmap from a correlation matrix.

# In[4]:


get_ipython().system('pip install seaborn')


# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 30, 40, 50, 60],
    "Attendance": [60, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True)

plt.title("Correlation Heatmap")
plt.show()


# In[ ]:




