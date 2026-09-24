#!/usr/bin/env python
# coding: utf-8

# # Statistics in Data Cleaning
# 
# ### Definition
# 
# Data Cleaning is the process of finding and correcting or removing incorrect, incomplete, duplicate, or inconsistent data.
# 
# Statistics helps us understand the data and identify unusual or incorrect values before using it for machine learning.
# 
# ### Why Statistics is Used
# 
# Statistical measures such as:
# 
# - Mean
# - Median
# - Standard Deviation
# - Minimum and Maximum
# - Quartiles
# 
# can help us understand the data and identify possible problems.
# 
# ### Business Example
# 
# A company has customer age data:
# 
# 20, 25, 30, 35, 200
# 
# The value 200 may be an incorrect age.
# 
# Statistical analysis can help identify this unusual value.
# 
# ### AI/ML Example
# 
# Before training a machine learning model, statistical analysis can be used to understand numerical features and identify unusual values that may affect the model.
# 
# ### Numerical Example
# 
# Consider the following ages:
# 
# 20, 22, 25, 28, 30, 150
# 
# The value 150 is much higher than the other values.
# 
# This value should be investigated during data cleaning.
# 
# ### Python Implementation
# 
# We can use Pandas functions such as `describe()` to get statistical information about numerical columns.
# 
# ### Interpretation
# 
# Statistical summaries help us understand the data and identify values that may require further checking or cleaning.

# In[1]:


import pandas as pd

data = {
    "Age": [20, 22, 25, 28, 30, 150],
    "Salary": [20000, 25000, 30000, 35000, 40000, 45000]
}

df = pd.DataFrame(data)

print("Statistical Summary:")
print(df.describe())


# # Outlier Detection
# 
# ### Definition
# 
# Outlier Detection is the process of identifying values that are very different from the other values in a dataset.
# 
# An outlier may be caused by an error, unusual situation, or genuine extreme value.
# 
# ### Why Statistics is Used
# 
# Statistics helps identify outliers using methods such as:
# 
# - Mean and Standard Deviation
# - IQR (Interquartile Range)
# - Z-Score
# 
# ### Business Example
# 
# A company has employee salary data:
# 
# 20000, 22000, 25000, 28000, 30000, 200000
# 
# The value 200000 is much higher than the other salaries and may be an outlier.
# 
# ### AI/ML Example
# 
# Outliers can affect machine learning models and may reduce model performance.
# 
# Statistical methods can help identify unusual values before training a model.
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 12, 15, 18, 20, 100
# 
# The value 100 is much higher than the other values.
# 
# Statistical analysis can be used to check whether 100 is an outlier.
# 
# ### Python Implementation
# 
# We can use the IQR method to identify outliers.
# 
# IQR = Q3 - Q1
# 
# A value below Q1 - 1.5 × IQR or above Q3 + 1.5 × IQR can be considered an outlier.
# 
# ### Interpretation
# 
# If a value is outside the calculated lower and upper limits, it can be identified as a possible outlier.

# In[2]:


import pandas as pd

data = {
    "Salary": [20000, 22000, 25000, 28000, 30000, 200000]
}

df = pd.DataFrame(data)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nOutliers:")
print(outliers)


# # Feature Engineering
# 
# ### Definition
# 
# Feature Engineering is the process of creating, transforming, or modifying features from existing data to make the data more useful for a machine learning model.
# 
# A feature is an input variable used by a machine learning model to make predictions.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand the data and decide how features should be transformed.
# 
# Measures such as mean, median, standard deviation, and distribution can help us choose suitable transformations.
# 
# ### Business Example
# 
# A company has customer information such as:
# 
# - Date of Birth
# - Monthly Income
# - Number of Purchases
# 
# Instead of directly using Date of Birth, we can create a new feature called Age.
# 
# ### AI/ML Example
# 
# In a house price prediction model, we may have:
# 
# - House Length
# - House Width
# 
# We can create a new feature:
# 
# House Area = Length × Width
# 
# The new feature may provide more useful information to the model.
# 
# ### Numerical Example
# 
# If:
# 
# House Length = 40
# 
# House Width = 30
# 
# Then:
# 
# House Area = 40 × 30 = 1200 square feet
# 
# ### Python Implementation
# 
# We can create a new feature from existing columns using Pandas.
# 
# ### Interpretation
# 
# Feature engineering creates useful information from existing data and can help machine learning models learn patterns more effectively.

# In[3]:


import pandas as pd

data = {
    "Length": [40, 50, 60],
    "Width": [30, 40, 50]
}

df = pd.DataFrame(data)

df["Area"] = df["Length"] * df["Width"]

print(df)


# # Feature Scaling
# 
# ### Definition
# 
# Feature Scaling is the process of bringing numerical features to a similar range of values.
# 
# It is useful when different features have very different scales.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand the range, mean, and standard deviation of features.
# 
# These values help us choose an appropriate scaling method.
# 
# ### Business Example
# 
# A customer dataset may contain:
# 
# - Age: 20 to 60
# - Salary: 20,000 to 100,000
# 
# Salary has much larger values than Age.
# 
# Feature scaling can bring these features to a similar scale.
# 
# ### AI/ML Example
# 
# Feature scaling is commonly useful for algorithms such as:
# 
# - K-Nearest Neighbors
# - K-Means Clustering
# - Support Vector Machines
# - Logistic Regression
# 
# ### Numerical Example
# 
# Suppose a feature contains:
# 
# 10, 20, 30, 40, 50
# 
# After scaling, the values can be converted into a smaller and comparable range.
# 
# ### Python Implementation
# 
# StandardScaler can be used to standardize numerical features.
# 
# It transforms the data based on the mean and standard deviation.
# 
# ### Interpretation
# 
# After scaling, the features have comparable scales, which can help certain machine learning algorithms work more effectively.

# In[4]:


import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("Original Data:")
print(df)

print("\nScaled Data:")
print(scaled_df)


# # Data Normalization
# 
# ### Definition
# 
# Data Normalization is the process of transforming numerical data into a common range, usually between 0 and 1.
# 
# It helps features with different value ranges become comparable.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand the minimum and maximum values of the data.
# 
# These values are used to transform the data into a common range.
# 
# ### Business Example
# 
# A company has customer data:
# 
# - Age: 20 to 60
# - Income: 20,000 to 100,000
# 
# The values are in different ranges.
# 
# Normalization can convert them into a common range.
# 
# ### AI/ML Example
# 
# Normalization can be useful for machine learning algorithms that are sensitive to the scale of input features, such as:
# 
# - K-Nearest Neighbors
# - K-Means Clustering
# - Neural Networks
# 
# ### Numerical Example
# 
# Consider the values:
# 
# 10, 20, 30, 40, 50
# 
# Using Min-Max Normalization:
# 
# Normalized Value = (Value - Minimum) / (Maximum - Minimum)
# 
# For the value 30:
# 
# (30 - 10) / (50 - 10) = 0.5
# 
# ### Python Implementation
# 
# MinMaxScaler from Scikit-learn can be used to normalize numerical data between 0 and 1.
# 
# ### Interpretation
# 
# After normalization, the numerical values are converted into a common range, making the features easier to compare.

# In[5]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

normalized_data = scaler.fit_transform(df)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=df.columns
)

print("Original Data:")
print(df)

print("\nNormalized Data:")
print(normalized_df)


# # Model Evaluation
# 
# ### Definition
# 
# Model Evaluation is the process of checking how well a machine learning model performs on data.
# 
# Statistics helps us measure the performance of a model using different evaluation metrics.
# 
# ### Why Statistics is Used
# 
# Statistics helps us compare the predicted values with the actual values and understand how accurate the model is.
# 
# Common evaluation metrics include:
# 
# - Accuracy
# - Precision
# - Recall
# - F1-Score
# - Mean Squared Error (MSE)
# - R² Score
# 
# ### Business Example
# 
# A company builds a model to predict whether a customer will purchase a product.
# 
# The model's predictions can be compared with the actual customer results to measure how well the model performs.
# 
# ### AI/ML Example
# 
# For a classification model, Accuracy can be used to measure how many predictions are correct.
# 
# ### Numerical Example
# 
# Suppose a model makes 10 predictions and 8 predictions are correct.
# 
# Accuracy = 8 / 10 = 0.8
# 
# Therefore, the accuracy is 80%.
# 
# ### Python Implementation
# 
# We can use Scikit-learn to calculate evaluation metrics such as accuracy.
# 
# ### Interpretation
# 
# Evaluation metrics help us understand whether a machine learning model is performing well and whether it needs improvement.

# In[6]:


from sklearn.metrics import accuracy_score

actual = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]

predicted = [1, 1, 0, 1, 1, 1, 0, 0, 1, 0]

accuracy = accuracy_score(actual, predicted)

print("Accuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# # Linear Regression
# 
# ### Definition
# 
# Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value based on one or more input features.
# 
# It tries to find a relationship between the input and output variables.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand the relationship between variables and measure how well the regression model fits the data.
# 
# ### Business Example
# 
# A company can use Linear Regression to predict house prices based on:
# 
# - House Size
# - Number of Rooms
# - Location
# 
# ### AI/ML Example
# 
# Linear Regression can be used to predict:
# 
# - House Price
# - Sales
# - Salary
# - Product Demand
# 
# ### Numerical Example
# 
# Suppose we have:
# 
# Study Hours: 2, 4, 6, 8
# 
# Marks: 50, 60, 70, 80
# 
# The model can learn the relationship between study hours and marks and predict marks for a new number of study hours.
# 
# ### Python Implementation
# 
# Scikit-learn provides `LinearRegression()` to create a linear regression model.
# 
# ### Interpretation
# 
# The model learns the relationship between the input feature and the target value and can use this relationship to make predictions.

# In[8]:


import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[["Study_Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

new_data = pd.DataFrame({"Study_Hours": [12]})

predicted_marks = model.predict(new_data)

print("Predicted Marks:", predicted_marks[0])


# # Logistic Regression
# 
# ### Definition
# 
# Logistic Regression is a supervised machine learning algorithm used for classification problems.
# 
# It is mainly used when the output has two possible categories, such as Yes/No or 0/1.
# 
# ### Why Statistics is Used
# 
# Statistics helps Logistic Regression calculate the probability of an outcome.
# 
# The probability is then used to classify the data into different categories.
# 
# ### Business Example
# 
# A bank can use Logistic Regression to predict whether a customer will:
# 
# - Get a loan: Yes
# - Get a loan: No
# 
# ### AI/ML Example
# 
# Logistic Regression can be used for:
# 
# - Spam or Not Spam
# - Customer Churn or Not Churn
# - Disease or No Disease
# - Purchase or No Purchase
# 
# ### Numerical Example
# 
# Suppose a model predicts:
# 
# Probability = 0.80
# 
# If the classification threshold is 0.5, the prediction is:
# 
# 0.80 > 0.5 → Class 1
# 
# ### Python Implementation
# 
# Scikit-learn provides `LogisticRegression()` to create a logistic regression model.
# 
# ### Interpretation
# 
# The model predicts the probability of an outcome and converts it into a class such as 0 or 1.

# In[9]:


import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Passed": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Study_Hours"]]
y = df["Passed"]

model = LogisticRegression()

model.fit(X, y)

new_data = pd.DataFrame({"Study_Hours": [5]})

prediction = model.predict(new_data)
probability = model.predict_proba(new_data)

print("Prediction:", prediction[0])
print("Probability:", probability[0])


# # Naive Bayes
# 
# ### Definition
# 
# Naive Bayes is a supervised machine learning algorithm mainly used for classification problems.
# 
# It is based on Bayes' Theorem and assumes that the features are independent of each other.
# 
# ### Why Statistics is Used
# 
# Naive Bayes uses probability to calculate the likelihood of different classes.
# 
# It uses the available data to determine which class is most likely for a new input.
# 
# ### Business Example
# 
# An email service can use Naive Bayes to classify emails as:
# 
# - Spam
# - Not Spam
# 
# ### AI/ML Example
# 
# Naive Bayes can be used for:
# 
# - Spam Detection
# - Text Classification
# - Sentiment Analysis
# - Document Classification
# 
# ### Numerical Example
# 
# Suppose an email contains words commonly found in spam emails.
# 
# Naive Bayes calculates the probability of the email being Spam and Not Spam.
# 
# If the Spam probability is higher, the email is classified as Spam.
# 
# ### Python Implementation
# 
# Scikit-learn provides `GaussianNB()` for implementing Naive Bayes classification.
# 
# ### Interpretation
# 
# The model uses probability to determine the most likely class for a given input.

# In[10]:


import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Attendance": [50, 55, 60, 70, 80, 90],
    "Passed": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Study_Hours", "Attendance"]]
y = df["Passed"]

model = GaussianNB()

model.fit(X, y)

new_data = pd.DataFrame({
    "Study_Hours": [5],
    "Attendance": [85]
})

prediction = model.predict(new_data)

print("Prediction:", prediction[0])


# # Clustering
# 
# ### Definition
# 
# Clustering is an unsupervised machine learning technique used to group similar data points together.
# 
# The groups created by clustering are called clusters.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand the distribution and similarity of data points.
# 
# It can help identify patterns and differences between groups.
# 
# ### Business Example
# 
# A company can group customers based on:
# 
# - Age
# - Income
# - Purchase Amount
# 
# Customers with similar characteristics can be placed in the same cluster.
# 
# ### AI/ML Example
# 
# Clustering can be used for:
# 
# - Customer Segmentation
# - Product Grouping
# - Image Segmentation
# - Anomaly Detection
# 
# ### Numerical Example
# 
# Suppose customers have the following data:
# 
# | Customer | Income | Spending |
# |----------|--------|----------|
# | A | 20 | 10 |
# | B | 22 | 12 |
# | C | 80 | 75 |
# | D | 85 | 78 |
# 
# Customers A and B are similar, while C and D are similar.
# 
# Therefore, they can be grouped into two clusters.
# 
# ### Python Implementation
# 
# K-Means is a commonly used clustering algorithm.
# 
# It groups data points into a specified number of clusters.
# 
# ### Interpretation
# 
# Clustering helps discover natural groups or patterns in data without using predefined output labels.

# In[11]:


import pandas as pd
from sklearn.cluster import KMeans

data = {
    "Income": [20, 22, 25, 80, 85, 90],
    "Spending": [10, 12, 15, 75, 80, 85]
}

df = pd.DataFrame(data)

model = KMeans(n_clusters=2, random_state=42, n_init=10)

df["Cluster"] = model.fit_predict(df[["Income", "Spending"]])

print(df)


# # Principal Component Analysis (PCA)
# 
# ### Definition
# 
# Principal Component Analysis (PCA) is a statistical technique used to reduce the number of features in a dataset while keeping the important information.
# 
# It converts the original features into a smaller number of new features called Principal Components.
# 
# ### Why Statistics is Used
# 
# PCA uses statistical concepts such as:
# 
# - Mean
# - Variance
# - Covariance
# 
# These help identify the directions in which the data has the most variation.
# 
# ### Business Example
# 
# A company may have many customer features such as:
# 
# - Age
# - Income
# - Spending
# - Purchase Frequency
# - Website Visits
# 
# PCA can reduce these many features into a smaller number of components.
# 
# ### AI/ML Example
# 
# PCA can be used for:
# 
# - Dimensionality Reduction
# - Data Visualization
# - Noise Reduction
# - Improving Model Efficiency
# 
# ### Numerical Example
# 
# Suppose a dataset has 5 features.
# 
# PCA may reduce these 5 features into 2 principal components while retaining important information from the original data.
# 
# ### Python Implementation
# 
# Scikit-learn provides `PCA()` to perform Principal Component Analysis.
# 
# ### Interpretation
# 
# PCA reduces the number of features and makes the dataset simpler while trying to preserve the most important variation in the data.

# In[12]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    "Age": [20, 25, 30, 35, 40],
    "Income": [20000, 30000, 40000, 50000, 60000],
    "Spending": [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components=2)

pca_data = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(
    pca_data,
    columns=["PC1", "PC2"]
)

print("Original Data:")
print(df)

print("\nPCA Data:")
print(pca_df)


# # Recommendation Systems
# 
# ### Definition
# 
# A Recommendation System is a machine learning system that suggests products, movies, songs, or other items to users based on their interests and previous activities.
# 
# Statistics helps analyze user behavior, ratings, preferences, and similarities to generate useful recommendations.
# 
# ### Why Statistics is Used
# 
# Statistics helps us understand:
# 
# - User preferences
# - Ratings
# - Purchase history
# - Item popularity
# - Similarity between users and items
# 
# ### Business Example
# 
# An online shopping website can recommend products based on a customer's previous purchases and browsing history.
# 
# For example, if a customer frequently buys sports shoes, the system may recommend sports clothing or accessories.
# 
# ### AI/ML Example
# 
# Recommendation systems are used in:
# 
# - E-commerce
# - Movie Streaming
# - Music Streaming
# - Social Media
# - Online Learning Platforms
# 
# ### Numerical Example
# 
# Suppose a user gives the following movie ratings:
# 
# Movie A = 5
# 
# Movie B = 4
# 
# Movie C = 2
# 
# The system can analyze these ratings and compare them with other users to recommend movies that the user may like.
# 
# ### Python Implementation
# 
# A simple recommendation system can calculate the average rating of items and recommend highly rated items.
# 
# ### Interpretation
# 
# Recommendation systems use statistical information about users and items to provide personalized suggestions.

# In[13]:


import pandas as pd

data = {
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D"],
    "Rating": [4.5, 4.8, 3.2, 4.7]
}

df = pd.DataFrame(data)

recommended_movies = df[df["Rating"] >= 4.5]

print("Recommended Movies:")
print(recommended_movies)


# In[ ]:




