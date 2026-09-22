#!/usr/bin/env python
# coding: utf-8

# # Bernoulli Distribution
# 
# ### Definition
# 
# Bernoulli Distribution is a probability distribution for an experiment that has only two possible outcomes.
# 
# The two outcomes are usually represented as:
# 
# - 1 → Success
# - 0 → Failure
# 
# The experiment is performed only one time.
# 
# ### Formula
# 
# P(X = x) = p^x × (1 - p)^(1-x)
# 
# Where:
# 
# p = Probability of success
# 
# 1 - p = Probability of failure
# 
# x = 0 or 1
# 
# ### Where Used
# 
# Bernoulli Distribution is used when there are only two possible outcomes.
# 
# Examples:
# 
# - Yes or No
# - Success or Failure
# - Pass or Fail
# - Buy or Not Buy
# - Spam or Not Spam
# 
# ### Real-world Example
# 
# Suppose a customer either purchases a product or does not purchase it.
# 
# Purchase → 1
# 
# No Purchase → 0
# 
# If the probability of purchase is 0.6, then:
# 
# P(Purchase) = 0.6
# 
# P(No Purchase) = 1 - 0.6 = 0.4
# 
# ### AI/ML Example
# 
# Bernoulli Distribution can be used for binary classification problems.
# 
# For example, an email can be classified as:
# 
# Spam → 1
# 
# Not Spam → 0
# 
# ### Python Visualization
# 
# The following program creates a simple bar chart showing the probability of success and failure.

# In[1]:


import matplotlib.pyplot as plt

outcomes = ["Failure", "Success"]
probabilities = [0.4, 0.6]

plt.bar(outcomes, probabilities)
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.title("Bernoulli Distribution")
plt.show()


# # Binomial Distribution
# 
# ### Definition
# 
# Binomial Distribution is a probability distribution used when an experiment is repeated a fixed number of times and each trial has only two possible outcomes.
# 
# The two outcomes are usually:
# 
# - Success
# - Failure
# 
# The trials should be independent and the probability of success should remain the same for each trial.
# 
# ### Formula
# 
# P(X = k) = nCk × p^k × (1-p)^(n-k)
# 
# Where:
# 
# n = Number of trials
# 
# k = Number of successes
# 
# p = Probability of success
# 
# 1-p = Probability of failure
# 
# ### Where Used
# 
# Binomial Distribution is used when we want to find the probability of getting a particular number of successes from a fixed number of trials.
# 
# Examples:
# 
# - Number of customers who purchase a product
# - Number of students who pass an exam
# - Number of successful calls
# - Number of defective products
# 
# ### Real-world Example
# 
# Suppose a company contacts 5 customers.
# 
# The probability that one customer purchases a product is 0.6.
# 
# We can use Binomial Distribution to find the probability that exactly 3 customers purchase the product.
# 
# Here:
# 
# n = 5
# 
# k = 3
# 
# p = 0.6
# 
# ### AI/ML Example
# 
# Binomial Distribution can be used when modelling the number of successful outcomes across a fixed number of independent binary trials.
# 
# For example, predicting how many customers out of 10 are likely to respond to a campaign.
# 
# ### Python Visualization
# 
# The following program calculates and visualizes the probability of different numbers of successes in 10 trials.

# In[2]:


import math
import matplotlib.pyplot as plt

n = 10
p = 0.6

successes = list(range(n + 1))
probabilities = []

for k in successes:
    probability = (
        math.comb(n, k)
        * (p ** k)
        * ((1 - p) ** (n - k))
    )
    probabilities.append(probability)

plt.bar(successes, probabilities)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.show()


# # Poisson Distribution
# 
# ### Definition
# 
# Poisson Distribution is a probability distribution used to find the probability of a certain number of events happening in a fixed period of time or space.
# 
# It is useful when we are counting how many times an event occurs.
# 
# ### Formula
# 
# P(X = k) = (e^(-λ) × λ^k) / k!
# 
# Where:
# 
# λ = Average number of events
# 
# k = Number of events we want to find
# 
# e = Euler's number, approximately 2.718
# 
# k! = Factorial of k
# 
# ### Where Used
# 
# Poisson Distribution is used for counting events that occur over a fixed period or area.
# 
# Examples:
# 
# - Number of calls received in one hour
# - Number of customers arriving in a shop
# - Number of website requests per minute
# - Number of machine failures in a day
# 
# ### Real-world Example
# 
# Suppose a customer support center receives an average of 4 calls per hour.
# 
# We can use Poisson Distribution to find the probability of receiving exactly 2 calls in one hour.
# 
# Here:
# 
# λ = 4
# 
# k = 2
# 
# ### AI/ML Example
# 
# Poisson Distribution can be used to model count-based data.
# 
# For example, predicting the number of customer requests received by an AI-powered support system in a fixed period.
# 
# ### Python Visualization
# 
# The following program calculates and visualizes the probability of receiving different numbers of calls when the average is 4 calls per hour.

# In[3]:


import math
import matplotlib.pyplot as plt

lam = 4

events = list(range(0, 11))
probabilities = []

for k in events:
    probability = (math.exp(-lam) * (lam ** k)) / math.factorial(k)
    probabilities.append(probability)

plt.bar(events, probabilities)
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.title("Poisson Distribution")
plt.show()


# # Uniform Distribution
# 
# ### Definition
# 
# Uniform Distribution is a probability distribution where all possible values have equal probability.
# 
# In simple words, every possible outcome has the same chance of occurring.
# 
# There are two types:
# 
# 1. Discrete Uniform Distribution
# 2. Continuous Uniform Distribution
# 
# ### Formula
# 
# For a continuous uniform distribution:
# 
# f(x) = 1 / (b - a)
# 
# Where:
# 
# a = Minimum value
# 
# b = Maximum value
# 
# ### Where Used
# 
# Uniform Distribution is used when all values in a given range have an equal chance of occurring.
# 
# Examples:
# 
# - Random number generation
# - Random selection
# - Simulation
# - Computer experiments
# 
# ### Real-world Example
# 
# Suppose a random number is selected between 1 and 10 and every number has an equal chance of being selected.
# 
# Each number has the same probability.
# 
# ### AI/ML Example
# 
# Uniform Distribution can be used for generating random values during simulations and testing.
# 
# It can also be useful when creating random samples within a specified range.
# 
# ### Python Visualization
# 
# The following program generates random values between 0 and 1 and displays their distribution.

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(0, 1, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Uniform Distribution")
plt.show()


# # Normal Distribution
# 
# ### Definition
# 
# Normal Distribution is a continuous probability distribution that is symmetric and has a bell-shaped curve.
# 
# In a normal distribution, most of the values are close to the mean, while fewer values occur far away from the mean.
# 
# ### Formula
# 
# f(x) = 1 / (σ√(2π)) × e^(-(x-μ)² / (2σ²))
# 
# Where:
# 
# μ = Mean
# 
# σ = Standard Deviation
# 
# x = Value
# 
# ### Where Used
# 
# Normal Distribution is commonly used to represent data where values are concentrated around the average.
# 
# Examples:
# 
# - Heights of people
# - Measurement errors
# - Test scores
# - Manufacturing measurements
# 
# ### Real-world Example
# 
# Suppose the heights of students in a large population are approximately normally distributed.
# 
# Most students will have heights close to the average height, while very short and very tall students will be fewer.
# 
# ### AI/ML Example
# 
# Normal Distribution is useful in statistical modelling and machine learning.
# 
# It can be used to understand the distribution of numerical features and is also used in methods that make assumptions about normally distributed data.
# 
# ### Python Visualization
# 
# The following program generates random data with a normal distribution and displays it using a histogram.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Normal Distribution")
plt.show()


# # Exponential Distribution
# 
# ### Definition
# 
# Exponential Distribution is a continuous probability distribution used to model the waiting time between events.
# 
# In simple words, it tells us how long we may need to wait until the next event happens.
# 
# ### Formula
# 
# f(x) = λe^(-λx)
# 
# Where:
# 
# λ = Rate of events
# 
# x = Waiting time
# 
# e = Euler's number, approximately 2.718
# 
# ### Where Used
# 
# Exponential Distribution is used when we are interested in the time between events.
# 
# Examples:
# 
# - Waiting time for a customer
# - Time between phone calls
# - Time between machine failures
# - Time until the next website request
# 
# ### Real-world Example
# 
# Suppose a customer support center receives calls at an average rate of 2 calls per hour.
# 
# Exponential Distribution can be used to model the waiting time until the next call arrives.
# 
# ### AI/ML Example
# 
# Exponential Distribution can be used in time-to-event modelling.
# 
# For example, it can help model the time until a machine fails or the waiting time between requests received by an AI system.
# 
# ### Python Visualization
# 
# The following program generates random waiting times using an exponential distribution and displays them using a histogram.

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=2, size=1000)

plt.hist(data, bins=20)
plt.xlabel("Waiting Time")
plt.ylabel("Frequency")
plt.title("Exponential Distribution")
plt.show()


# In[ ]:




