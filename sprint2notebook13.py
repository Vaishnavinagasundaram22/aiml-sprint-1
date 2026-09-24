#!/usr/bin/env python
# coding: utf-8

# # Histogram
# 
# ### Definition
# 
# A Histogram is a statistical graph used to show the distribution of numerical data.
# 
# It groups numerical values into intervals called bins and shows how many values fall within each interval.
# 
# ### Purpose
# 
# A histogram helps us understand:
# 
# - How the data is distributed.
# - Where most values are located.
# - The spread of the data.
# - The shape of the data.
# 
# ### When to Use
# 
# A histogram is used when we want to visualize the distribution of numerical data.
# 
# For example, we can use a histogram to show the distribution of student marks.
# 
# ### Advantages
# 
# - Easy to understand.
# - Shows the distribution of numerical data.
# - Helps identify the shape and spread of data.
# 
# ### Limitations
# 
# - The appearance can change depending on the number of bins.
# - It is mainly suitable for numerical data.
# 
# ### Python Example
# 
# Matplotlib provides the `hist()` function to create a histogram.
# 
# ### Interpretation
# 
# The height of each bar represents the number of values that fall within that particular range.

# In[1]:


import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90, 95]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show()


# # Bar Chart
# 
# ### Definition
# 
# A Bar Chart is a graph used to compare values between different categories.
# 
# Each category is represented using a rectangular bar.
# 
# ### Purpose
# 
# A bar chart helps us easily compare the values of different categories.
# 
# ### When to Use
# 
# A bar chart is used when:
# 
# - We want to compare different categories.
# - The data is categorical.
# - We want to show counts or values for different groups.
# 
# ### Advantages
# 
# - Easy to understand.
# - Easy to compare categories.
# - Clearly shows differences between values.
# 
# ### Limitations
# 
# - Too many categories can make the chart difficult to read.
# - It is not mainly used to show continuous data distribution.
# 
# ### Python Example
# 
# Matplotlib provides the `bar()` function to create a bar chart.
# 
# ### Interpretation
# 
# The height of each bar represents the value of that category.
# 
# A taller bar means a higher value.

# In[2]:


import matplotlib.pyplot as plt

departments = ["HR", "Sales", "IT", "Finance"]
employees = [20, 35, 50, 25]

plt.bar(departments, employees)

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employees by Department")

plt.show()


# # Line Chart
# 
# ### Definition
# 
# A Line Chart is a graph used to show how a value changes over a period of time or across an ordered sequence.
# 
# The data points are connected using lines to show the trend.
# 
# ### Purpose
# 
# A line chart helps us understand:
# 
# - Trends in data.
# - Increases and decreases.
# - Changes over time.
# - Patterns in sequential data.
# 
# ### When to Use
# 
# A line chart is used when:
# 
# - We want to show changes over time.
# - The data has an ordered sequence.
# - We want to identify trends or patterns.
# 
# ### Advantages
# 
# - Clearly shows trends.
# - Easy to identify increases and decreases.
# - Useful for time-series data.
# 
# ### Limitations
# 
# - Too many lines can make the chart difficult to understand.
# - It is not suitable for comparing many unrelated categories.
# 
# ### Python Example
# 
# Matplotlib provides the `plot()` function to create a line chart.
# 
# ### Interpretation
# 
# An upward line shows an increase in the values.
# 
# A downward line shows a decrease in the values.

# In[3]:


import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [100, 120, 115, 140, 160, 180]

plt.plot(months, sales, marker="o")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")

plt.show()


# # Scatter Plot
# 
# ### Definition
# 
# A Scatter Plot is a graph used to show the relationship between two numerical variables.
# 
# It represents each data value as a point on the graph.
# 
# ### Purpose
# 
# A scatter plot helps us understand:
# 
# - The relationship between two variables.
# - Positive or negative relationships.
# - Patterns in the data.
# - Possible outliers.
# 
# ### When to Use
# 
# A scatter plot is used when:
# 
# - We want to compare two numerical variables.
# - We want to identify relationships between variables.
# - We want to find patterns or outliers.
# 
# ### Advantages
# 
# - Clearly shows the relationship between two variables.
# - Helps identify patterns.
# - Helps identify possible outliers.
# 
# ### Limitations
# 
# - It can become difficult to read when there are too many data points.
# - It mainly shows relationships between two numerical variables.
# 
# ### Python Example
# 
# Matplotlib provides the `scatter()` function to create a scatter plot.
# 
# ### Interpretation
# 
# If the points move upward from left to right, there may be a positive relationship.
# 
# If the points move downward from left to right, there may be a negative relationship.
# 
# If the points are randomly spread, there may be little or no clear relationship.

# In[4]:


import matplotlib.pyplot as plt

study_hours = [2, 3, 4, 5, 6, 7, 8, 9]
marks = [50, 55, 60, 65, 70, 75, 82, 88]

plt.scatter(study_hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()


# # Pie Chart
# 
# ### Definition
# 
# A Pie Chart is a circular graph used to show how different categories contribute to a whole.
# 
# The circle is divided into slices, where each slice represents a category.
# 
# ### Purpose
# 
# A pie chart helps us understand the proportion or percentage of each category.
# 
# ### When to Use
# 
# A pie chart is used when:
# 
# - We want to show parts of a whole.
# - The number of categories is small.
# - We want to compare percentages or proportions.
# 
# ### Advantages
# 
# - Easy to understand.
# - Clearly shows proportions.
# - Useful for showing percentage distribution.
# 
# ### Limitations
# 
# - Difficult to compare similar-sized slices.
# - Too many categories make the chart difficult to read.
# - Not suitable for showing trends over time.
# 
# ### Python Example
# 
# Matplotlib provides the `pie()` function to create a pie chart.
# 
# ### Interpretation
# 
# Each slice represents a category.
# 
# A larger slice represents a larger proportion of the total data.

# In[5]:


import matplotlib.pyplot as plt

departments = ["HR", "Sales", "IT", "Finance"]
employees = [20, 35, 50, 25]

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%"
)

plt.title("Employee Distribution by Department")

plt.show()


# # Density Plot
# 
# ### Definition
# 
# A Density Plot is a graph used to show the distribution of numerical data as a smooth curve.
# 
# It shows where the data values are concentrated.
# 
# ### Purpose
# 
# A density plot helps us understand:
# 
# - The distribution of data.
# - Where values are concentrated.
# - The shape of the data.
# - Whether the data has one or more peaks.
# 
# ### When to Use
# 
# A density plot is used when:
# 
# - We want to visualize the distribution of numerical data.
# - We want a smooth representation of the data distribution.
# - We want to compare distributions between groups.
# 
# ### Advantages
# 
# - Shows a smooth distribution.
# - Easy to identify peaks and patterns.
# - Useful for comparing distributions.
# 
# ### Limitations
# 
# - The shape can change depending on the smoothing method.
# - It may be difficult for beginners to interpret.
# - It is mainly used for numerical data.
# 
# ### Python Example
# 
# A density plot can be created using Pandas `plot()` with `kind="density"`.
# 
# ### Interpretation
# 
# The peaks of the density curve show where values are more concentrated.
# 
# A higher peak indicates a higher concentration of data around that range.

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90, 95]

data = pd.Series(marks)

data.plot(kind="density")

plt.xlabel("Marks")
plt.title("Density Plot of Student Marks")

plt.show()


# # Box Plot
# 
# ### Definition
# 
# A Box Plot is a statistical graph used to show the distribution and spread of numerical data.
# 
# It shows the minimum value, first quartile, median, third quartile, and maximum value. It can also help identify possible outliers.
# 
# ### Purpose
# 
# A box plot helps us understand:
# 
# - The spread of the data.
# - The median value.
# - The quartiles.
# - Possible outliers.
# - The overall distribution of the data.
# 
# ### When to Use
# 
# A box plot is used when:
# 
# - We want to understand the spread of numerical data.
# - We want to compare distributions between groups.
# - We want to identify possible outliers.
# 
# ### Advantages
# 
# - Clearly shows the median and quartiles.
# - Helps identify possible outliers.
# - Useful for comparing multiple groups.
# 
# ### Limitations
# 
# - It does not show every individual data value.
# - It can be difficult for beginners to understand at first.
# 
# ### Python Example
# 
# Matplotlib provides the `boxplot()` function to create a box plot.
# 
# ### Interpretation
# 
# The line inside the box represents the median.
# 
# The box represents the middle 50% of the data.
# 
# Points outside the whiskers may represent possible outliers.

# In[7]:


import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 80, 95]

plt.boxplot(marks)

plt.ylabel("Marks")
plt.title("Box Plot of Student Marks")

plt.show()


# # Violin Plot
# 
# ### Definition
# 
# A Violin Plot is a statistical graph that shows the distribution of numerical data using a combination of a box plot and a density plot.
# 
# It shows both the spread and the shape of the data distribution.
# 
# ### Purpose
# 
# A violin plot helps us understand:
# 
# - The distribution of data.
# - The spread of values.
# - The median and quartiles.
# - Where the data is more concentrated.
# 
# ### When to Use
# 
# A violin plot is used when:
# 
# - We want to compare distributions between groups.
# - We want to understand the shape of numerical data.
# - We want more distribution information than a box plot provides.
# 
# ### Advantages
# 
# - Shows the shape of the data distribution.
# - Shows more information than a simple box plot.
# - Useful for comparing multiple groups.
# 
# ### Limitations
# 
# - Can be difficult for beginners to interpret.
# - The distribution shape depends on the smoothing method.
# - It is mainly used for numerical data.
# 
# ### Python Example
# 
# Seaborn provides the `violinplot()` function to create a violin plot.
# 
# ### Interpretation
# 
# The wider part of the violin represents a higher concentration of data.
# 
# The narrower part represents a lower concentration of data.

# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 80, 85, 90, 95]

sns.violinplot(y=marks)

plt.ylabel("Marks")
plt.title("Violin Plot of Student Marks")

plt.show()


# # Pair Plot
# 
# ### Definition
# 
# A Pair Plot is a statistical visualization that shows the relationships between multiple numerical variables in a dataset.
# 
# It creates scatter plots between pairs of variables and shows the distribution of each variable along the diagonal.
# 
# ### Purpose
# 
# A pair plot helps us understand:
# 
# - Relationships between multiple numerical variables.
# - Correlations between features.
# - Data distributions.
# - Possible patterns and outliers.
# 
# ### When to Use
# 
# A pair plot is used when:
# 
# - We want to explore several numerical features at the same time.
# - We want to find relationships between features.
# - We want to understand a dataset before building a machine learning model.
# 
# ### Advantages
# 
# - Shows relationships between many variables in one visualization.
# - Helps identify patterns and correlations.
# - Useful for initial data exploration.
# 
# ### Limitations
# 
# - Can become difficult to read when there are many features.
# - Can be computationally expensive for large datasets.
# - Requires numerical features for meaningful scatter plots.
# 
# ### Python Example
# 
# Seaborn provides the `pairplot()` function to create a pair plot.
# 
# ### Interpretation
# 
# Each scatter plot shows the relationship between two variables.
# 
# The diagonal shows the distribution of each individual variable.

# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 80, 90],
    "Attendance": [60, 65, 70, 80, 85]
}

df = sns.load_dataset("iris")

sns.pairplot(df)

plt.show()


# # Heatmap
# 
# ### Definition
# 
# A Heatmap is a visualization that represents numerical values using different shades of color.
# 
# It is commonly used to identify patterns and relationships in a dataset.
# 
# ### Purpose
# 
# A heatmap helps us understand:
# 
# - Relationships between variables.
# - Correlation between features.
# - Patterns in numerical data.
# - High and low values quickly.
# 
# ### When to Use
# 
# A heatmap is used when:
# 
# - We want to visualize a correlation matrix.
# - We want to compare many numerical values.
# - We want to identify patterns in a dataset.
# 
# ### Advantages
# 
# - Easy to identify patterns visually.
# - Useful for correlation analysis.
# - Can display a large amount of numerical information in a compact form.
# 
# ### Limitations
# 
# - Too many variables can make it difficult to read.
# - The interpretation depends on the color scale.
# - It is mainly useful for numerical data.
# 
# ### Python Example
# 
# Seaborn provides the `heatmap()` function to create a heatmap.
# 
# ### Interpretation
# 
# In a correlation heatmap:
# 
# - Values close to +1 show a strong positive relationship.
# - Values close to -1 show a strong negative relationship.
# - Values close to 0 show a weak or no linear relationship.

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 80, 90],
    "Attendance": [60, 65, 70, 80, 85]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True)

plt.title("Correlation Heatmap")

plt.show()


# In[ ]:




