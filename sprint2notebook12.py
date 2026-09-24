#!/usr/bin/env python
# coding: utf-8

# # Correlation Matrix
# 
# ### Definition
# 
# A Correlation Matrix is a table that shows the relationship between multiple numerical variables.
# 
# It helps us understand how strongly two variables are related and in which direction they move.
# 
# ### Types of Correlation
# 
# - Positive Correlation: Both variables increase or decrease together.
# - Negative Correlation: When one variable increases, the other tends to decrease.
# - No Correlation: There is no clear linear relationship between the variables.
# 
# ### When to Use
# 
# Correlation Matrix is used to:
# 
# - Understand relationships between features.
# - Find strongly related variables.
# - Identify features that may contain similar information.
# - Understand the dataset before building a machine learning model.
# 
# ### Business Example
# 
# A company can check the relationship between advertising spending, website visits, and sales.
# 
# For example, if advertising spending and sales have a high positive correlation, higher advertising spending is associated with higher sales.
# 
# ### AI/ML Example
# 
# In machine learning, a correlation matrix helps us understand relationships between features and identify features that may be highly related to each other.
# 
# ### Numerical Example
# 
# Consider the following data:
# 
# Study Hours: 2, 4, 6, 8, 10
# 
# Marks: 50, 60, 70, 80, 90
# 
# As study hours increase, marks also increase.
# 
# Therefore, these two variables have a strong positive correlation.
# 
# ### Python Implementation
# 
# Pandas provides the `corr()` function to calculate the correlation matrix.
# 
# ### Interpretation
# 
# Correlation values range from -1 to +1.
# 
# - +1 → Perfect positive correlation
# - 0 → No linear correlation
# - -1 → Perfect negative correlation
# 
# A value closer to +1 indicates a strong positive relationship.
# 
# A value closer to -1 indicates a strong negative relationship.

# In[1]:


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


# # Multicollinearity
# 
# ### Definition
# 
# Multicollinearity occurs when two or more independent variables in a dataset are highly related to each other.
# 
# This means that the features contain similar information.
# 
# ### When to Use
# 
# We check for multicollinearity when:
# 
# - Building machine learning models.
# - Working with multiple input features.
# - Using models such as Linear Regression.
# - We want to identify highly related features.
# 
# ### When Not to Use
# 
# Multicollinearity is mainly a concern when the relationship between input features affects the model.
# 
# It is not directly used for categorical features without appropriate encoding.
# 
# ### Business Example
# 
# A company may have these features:
# 
# - House Size in square feet
# - Number of Rooms
# - Number of Bedrooms
# 
# House size and number of rooms may be highly related.
# 
# This can create multicollinearity because these features provide similar information.
# 
# ### AI/ML Example
# 
# In a machine learning model that predicts house prices, highly correlated input features can make it difficult to understand the individual effect of each feature.
# 
# ### Numerical Example
# 
# Suppose:
# 
# House Size = [1000, 1500, 2000, 2500]
# 
# Number of Rooms = [2, 3, 4, 5]
# 
# Both variables increase together.
# 
# Therefore, they may have a high correlation and could have multicollinearity.
# 
# ### Python Implementation
# 
# We can use the correlation matrix to identify highly correlated features.
# 
# A correlation value close to +1 or -1 indicates a strong relationship between two variables.
# 
# ### Interpretation
# 
# If two or more independent variables have a very high correlation, there may be multicollinearity.
# 
# Multicollinearity can make it difficult to understand the individual contribution of each feature in some models.

# In[2]:


import pandas as pd

data = {
    "House_Size": [1000, 1500, 2000, 2500, 3000],
    "Number_of_Rooms": [2, 3, 4, 5, 6],
    "Price": [20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)


# # Variance Inflation Factor (VIF)
# 
# ### Definition
# 
# Variance Inflation Factor (VIF) is a statistical measure used to detect multicollinearity between independent variables.
# 
# It tells us how much the variance of a feature's coefficient is increased because of its relationship with other features.
# 
# ### When to Use
# 
# VIF is used when:
# 
# - We have multiple independent variables.
# - We want to detect multicollinearity.
# - We are building models such as Linear Regression.
# - We want to identify features that may provide similar information.
# 
# ### When Not to Use
# 
# VIF is mainly used for numerical independent variables.
# 
# It is not normally used directly on categorical variables unless they have been appropriately encoded.
# 
# ### Business Example
# 
# A company predicts house prices using:
# 
# - House Size
# - Number of Rooms
# - Number of Bedrooms
# 
# If these features are highly related, VIF can help identify multicollinearity.
# 
# ### AI/ML Example
# 
# In a machine learning dataset, VIF can help identify highly related input features before training a regression model.
# 
# ### Numerical Example
# 
# Suppose a dataset contains:
# 
# - Study Hours
# - Assignment Hours
# - Attendance
# 
# We can calculate the VIF for each feature.
# 
# A higher VIF indicates that a feature has a stronger relationship with the other independent variables.
# 
# ### Python Implementation
# 
# The `variance_inflation_factor()` function from `statsmodels` is used to calculate VIF.
# 
# ### Interpretation
# 
# A commonly used guideline is:
# 
# - VIF close to 1 → Low multicollinearity
# - VIF between 1 and 5 → Usually acceptable
# - VIF above 5 → Possible multicollinearity
# - VIF above 10 → Strong multicollinearity may be present
# 
# These are guidelines, not strict rules.
# 
# A high VIF means that the feature is strongly related to the other independent variables.

# In[ ]:


get_ipython().run_line_magic('pip', 'install statsmodels')


# In[ ]:


import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Assignment_Hours": [1, 2, 3, 4, 5],
    "Attendance": [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

vif_data = pd.DataFrame()

vif_data["Feature"] = df.columns

vif_data["VIF"] = [
    variance_inflation_factor(df.values, i)
    for i in range(df.shape[1])
]

print(vif_data)


# # Feature Importance
# 
# ### Definition
# 
# Feature Importance is a technique used to identify which features contribute more to the prediction of a machine learning model.
# 
# It helps us understand which input variables are more useful for making predictions.
# 
# ### When to Use
# 
# Feature Importance is used when:
# 
# - We want to understand which features are important.
# - We want to simplify a machine learning model.
# - We want to identify less useful features.
# - We want to understand how a model makes predictions.
# 
# ### When Not to Use
# 
# Feature importance should not be treated as a direct proof of cause and effect.
# 
# Different machine learning models may calculate feature importance differently.
# 
# ### Business Example
# 
# A company wants to predict whether a customer will purchase a product.
# 
# The features may include:
# 
# - Age
# - Income
# - Website Visits
# - Previous Purchases
# 
# Feature importance can show which features contribute more to the prediction.
# 
# ### AI/ML Example
# 
# In a machine learning model, feature importance can help identify the input variables that have the greatest influence on the model's predictions.
# 
# ### Numerical Example
# 
# Suppose a model gives the following feature importance values:
# 
# - Income → 0.50
# - Website Visits → 0.30
# - Age → 0.20
# 
# Income has the highest importance value among these features.
# 
# ### Python Implementation
# 
# A Decision Tree model provides a `feature_importances_` attribute that can be used to find the importance of each feature.
# 
# ### Interpretation
# 
# A higher feature importance value means the feature contributed more to the model's decisions.
# 
# Feature importance values are model-dependent, so they should be interpreted in the context of the chosen machine learning model.

# In[ ]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Age": [20, 25, 30, 35, 40, 45],
    "Income": [20, 30, 40, 50, 60, 70],
    "Website_Visits": [2, 3, 4, 6, 8, 10],
    "Purchased": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income", "Website_Visits"]]
y = df["Purchased"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

importance = model.feature_importances_

for feature, value in zip(X.columns, importance):
    print(feature, ":", value)


# # Feature Selection Basics
# 
# ### Definition
# 
# Feature Selection is the process of selecting the most useful features from a dataset for building a machine learning model.
# 
# It helps remove unnecessary or less useful features from the dataset.
# 
# ### When to Use
# 
# Feature selection is used when:
# 
# - The dataset has many features.
# - Some features are not useful for prediction.
# - Some features contain similar information.
# - We want to reduce the complexity of a model.
# - We want to improve model performance.
# 
# ### When Not to Use
# 
# Feature selection should not be done only based on feature names or assumptions.
# 
# The usefulness of a feature should be checked using the data and the chosen machine learning method.
# 
# ### Business Example
# 
# A company wants to predict customer purchases using:
# 
# - Age
# - Income
# - Website Visits
# - Customer ID
# - Purchase History
# 
# Customer ID may not provide useful information for predicting purchases.
# 
# Feature selection can help identify and remove such unnecessary features.
# 
# ### AI/ML Example
# 
# In machine learning, selecting useful features can reduce the number of inputs given to a model and can make the model simpler.
# 
# ### Numerical Example
# 
# Suppose a dataset has 5 features:
# 
# - Age
# - Income
# - Website Visits
# - Customer ID
# - Previous Purchases
# 
# After checking the features, we may select:
# 
# - Age
# - Income
# - Website Visits
# - Previous Purchases
# 
# Customer ID may be removed because it does not provide useful predictive information.
# 
# ### Python Implementation
# 
# One simple method is to use `SelectKBest` from Scikit-learn to select the best features based on a statistical score.
# 
# ### Interpretation
# 
# Feature selection keeps useful features and removes features that are less useful for the selected prediction task.
# 
# The selected features can then be used to train the machine learning model.

# In[14]:


import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

data = {
    "Age": [20, 25, 30, 35, 40, 45],
    "Income": [20, 30, 40, 50, 60, 70],
    "Website_Visits": [2, 3, 4, 6, 8, 10],
    "Customer_ID": [101, 102, 103, 104, 105, 106],
    "Purchased": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income", "Website_Visits", "Customer_ID"]]
y = df["Purchased"]

selector = SelectKBest(score_func=f_classif, k=2)

X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("Selected Features:")
print(selected_features.tolist())


# In[ ]:




