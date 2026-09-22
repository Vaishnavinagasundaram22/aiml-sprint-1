#!/usr/bin/env python
# coding: utf-8

# # Introduction to Probability
# 
# ### Definition
# 
# Probability is a measure of how likely an event is to happen.
# 
# The probability value is always between 0 and 1.
# 
# 0 means the event is impossible.
# 
# 1 means the event is certain to happen.
# 
# ### Formula
# 
# Probability = Number of Favorable Outcomes / Total Number of Possible Outcomes
# 
# ### Numerical Example
# 
# Suppose we toss a coin.
# 
# Possible outcomes are:
# 
# Head, Tail
# 
# Total outcomes = 2
# 
# There is 1 favorable outcome for getting Head.
# 
# Therefore:
# 
# P(Head) = 1 / 2
# 
# P(Head) = 0.5
# 
# So, there is a 50% probability of getting Head.
# 
# ### Business Example
# 
# A company can use probability to estimate the chance that a customer will purchase a product.
# 
# For example, if historical data shows that 70 out of 100 customers purchase a product:
# 
# Probability of purchase = 70 / 100 = 0.7
# 
# ### AI/ML Example
# 
# Probability is important in machine learning because many models work with probabilities.
# 
# For example, a classification model may predict:
# 
# Customer will buy = 0.80
# 
# Customer will not buy = 0.20
# 
# This means the model estimates an 80% probability of purchase.
# 
# ### Python Implementation
# 
# The following program calculates the probability of getting Head when tossing a fair coin.

# In[1]:


favorable_outcomes = 1
total_outcomes = 2

probability = favorable_outcomes / total_outcomes

print("Probability of getting Head:", probability)
print("Probability in percentage:", probability * 100, "%")


# ### Interpretation
# 
# The probability of getting Head is 0.5 or 50%.
# 
# This means that when a fair coin is tossed, there is a 50% chance of getting Head.
# 
# Probability helps us measure uncertainty and make predictions based on possible outcomes.

# # Events
# 
# ### Definition
# 
# An event is a specific outcome or a group of outcomes that we are interested in during a probability experiment.
# 
# For example, when we roll a dice, getting an even number is an event.
# 
# ### Types of Events
# 
# Some common types of events are:
# 
# 1. Simple Event
#    - Contains only one outcome.
#    - Example: Getting 6 when rolling a dice.
# 
# 2. Compound Event
#    - Contains more than one outcome.
#    - Example: Getting an even number: 2, 4, 6.
# 
# 3. Certain Event
#    - An event that will definitely happen.
#    - Probability = 1
# 
# 4. Impossible Event
#    - An event that cannot happen.
#    - Probability = 0
# 
# ### Numerical Example
# 
# Suppose we roll a fair dice.
# 
# Possible outcomes:
# 
# 1, 2, 3, 4, 5, 6
# 
# Event A = Getting an even number.
# 
# Favorable outcomes:
# 
# 2, 4, 6
# 
# Total outcomes = 6
# 
# Therefore:
# 
# P(A) = 3 / 6
# 
# P(A) = 0.5
# 
# So, the probability of getting an even number is 50%.
# 
# ### Business Example
# 
# A company may define an event as:
# 
# "Customer purchases a product."
# 
# The company can calculate the probability of this event using historical customer data.
# 
# ### AI/ML Example
# 
# In machine learning, an event can represent a particular outcome.
# 
# For example:
# 
# Event A = Customer will leave the company.
# 
# A model can estimate the probability of this event.
# 
# ### Python Implementation
# 
# The following program calculates the probability of getting an even number when rolling a dice.

# In[2]:


possible_outcomes = [1, 2, 3, 4, 5, 6]
favorable_outcomes = [2, 4, 6]

probability = len(favorable_outcomes) / len(possible_outcomes)

print("Possible Outcomes:", possible_outcomes)
print("Favorable Outcomes:", favorable_outcomes)
print("Probability of Even Number:", probability)
print("Probability in Percentage:", probability * 100, "%")


# ### Interpretation
# 
# There are 6 possible outcomes when rolling a dice.
# 
# There are 3 favorable outcomes: 2, 4 and 6.
# 
# Therefore, the probability of getting an even number is 0.5 or 50%.
# 
# An event represents the outcome or group of outcomes that we are interested in.

# # Sample Space
# 
# ### Definition
# 
# Sample Space is the set of all possible outcomes of a probability experiment.
# 
# It is usually represented by the symbol S.
# 
# ### Numerical Example
# 
# Suppose we toss a coin.
# 
# The possible outcomes are:
# 
# Head (H)
# Tail (T)
# 
# Therefore:
# 
# S = {H, T}
# 
# There are 2 possible outcomes.
# 
# Now suppose we roll a dice.
# 
# The possible outcomes are:
# 
# S = {1, 2, 3, 4, 5, 6}
# 
# There are 6 possible outcomes.
# 
# ### Business Example
# 
# A company can use sample space to represent possible customer responses.
# 
# For example:
# 
# S = {Buy, Not Buy}
# 
# These are the possible outcomes for a simple purchase decision.
# 
# ### AI/ML Example
# 
# Sample spaces help us define all possible outcomes before calculating probabilities.
# 
# For example, in a binary classification problem:
# 
# S = {Positive, Negative}
# 
# These represent the possible prediction classes.
# 
# ### Python Implementation
# 
# The following program creates the sample space for rolling a dice.

# In[3]:


sample_space = [1, 2, 3, 4, 5, 6]

print("Sample Space:", sample_space)
print("Number of Possible Outcomes:", len(sample_space))


# # Independent Events
# 
# ### Definition
# 
# Independent Events are events where the occurrence of one event does not affect the occurrence of another event.
# 
# In simple words, one event happens, but it does not change the probability of the other event.
# 
# ### Formula
# 
# P(A and B) = P(A) × P(B)
# 
# ### Numerical Example
# 
# Suppose we toss a coin two times.
# 
# Probability of getting Head in the first toss:
# 
# P(Head) = 1/2
# 
# Probability of getting Head in the second toss:
# 
# P(Head) = 1/2
# 
# Since the first toss does not affect the second toss:
# 
# P(Head and Head) = 1/2 × 1/2 = 1/4
# 
# So, the probability of getting Head in both tosses is 0.25 or 25%.
# 
# ### Business Example
# 
# A company sends promotional emails to two different customers.
# 
# If the action of one customer does not affect the action of another customer, their actions can be considered independent events.
# 
# ### AI/ML Example
# 
# In some machine learning situations, individual observations are assumed to be independent.
# 
# For example, if one customer's purchase does not affect another customer's purchase, the observations may be treated as independent.
# 
# ### Python Implementation
# 
# The following program calculates the probability of getting Head in two independent coin tosses.

# In[4]:


probability_first_head = 1 / 2
probability_second_head = 1 / 2

probability_both_heads = probability_first_head * probability_second_head

print("Probability of Head in first toss:", probability_first_head)
print("Probability of Head in second toss:", probability_second_head)
print("Probability of getting Head in both tosses:", probability_both_heads)
print("Percentage:", probability_both_heads * 100, "%")


# ### Interpretation
# 
# The probability of getting Head in both independent tosses is 0.25 or 25%.
# 
# The first toss does not change the probability of getting Head in the second toss.
# 
# This concept is useful in probability calculations and is also important when understanding assumptions about data in machine learning.

# # Dependent Events
# 
# ### Definition
# 
# Dependent Events are events where the occurrence of one event affects the probability of another event.
# 
# In simple words, first event happens, and because of that, the probability of the next event changes.
# 
# ### Formula
# 
# P(A and B) = P(A) × P(B|A)
# 
# Here,
# 
# P(B|A) means the probability of event B happening after event A has already happened.
# 
# ### Numerical Example
# 
# Suppose there are 5 cards:
# 
# A, B, C, D, E
# 
# We select one card without replacement.
# 
# Probability of selecting A first:
# 
# P(A) = 1/5
# 
# After selecting A, only 4 cards remain.
# 
# So, the probability of selecting B second is:
# 
# P(B|A) = 1/4
# 
# Therefore:
# 
# P(A and B) = 1/5 × 1/4 = 1/20
# 
# So, the probability is 0.05 or 5%.
# 
# ### Business Example
# 
# Suppose a company has 10 products in stock and a customer buys one product.
# 
# If the product is not replaced immediately, the number of products available for the next customer changes.
# 
# Therefore, the second purchase probability can depend on the first purchase.
# 
# ### AI/ML Example
# 
# In machine learning, some observations may not be independent.
# 
# For example, customer transactions from the same customer can be related to each other.
# 
# One transaction may affect or provide information about another transaction.
# 
# ### Python Implementation
# 
# The following program calculates the probability of selecting two specific cards without replacement.

# In[5]:


total_cards = 5

probability_first_card = 1 / total_cards

remaining_cards = total_cards - 1
probability_second_card = 1 / remaining_cards

probability_both = probability_first_card * probability_second_card

print("Probability of first card:", probability_first_card)
print("Probability of second card:", probability_second_card)
print("Probability of selecting both cards:", probability_both)
print("Percentage:", probability_both * 100, "%")


# # Conditional Probability
# 
# ### Definition
# 
# Conditional Probability means finding the probability of an event when we already know that another event has happened.
# 
# In simple words, one condition is already given, and based on that condition we find the probability.
# 
# ### Formula
# 
# P(A|B) = P(A and B) / P(B)
# 
# Here,
# 
# P(A|B) means the probability of event A happening when event B has already happened.
# 
# ### Numerical Example
# 
# Suppose a class has 10 students.
# 
# 6 students are girls.
# 
# Among those 6 girls, 3 students play cricket.
# 
# If we already know that a student is a girl, the probability that the student plays cricket is:
# 
# P(Cricket | Girl) = 3 / 6 = 0.5
# 
# So, the conditional probability is 50%.
# 
# ### Business Example
# 
# A company wants to know the probability that a customer purchases a product given that the customer clicked on an advertisement.
# 
# Here:
# 
# Event A = Customer purchases the product
# 
# Event B = Customer clicked the advertisement
# 
# The company can use conditional probability to understand customer behaviour.
# 
# ### AI/ML Example
# 
# Conditional probability is used in machine learning models such as classification.
# 
# For example, in spam detection, we can calculate the probability that an email is spam given that certain words appear in the email.
# 
# ### Python Implementation
# 
# The following program calculates the probability of a student playing cricket given that the student is a girl.

# In[6]:


total_girls = 6
girls_who_play_cricket = 3

conditional_probability = girls_who_play_cricket / total_girls

print("Total Girls:", total_girls)
print("Girls who play Cricket:", girls_who_play_cricket)
print("P(Cricket | Girl):", conditional_probability)
print("Percentage:", conditional_probability * 100, "%")


# # Bayes' Theorem
# 
# ### Definition
# 
# Bayes' Theorem is used to find the probability of an event when we have some new information about it.
# 
# In simple words, we start with an initial probability and update it using new information.
# 
# ### Formula
# 
# P(A|B) = [P(B|A) × P(A)] / P(B)
# 
# Here,
# 
# P(A|B) = Probability of A given B
# 
# P(B|A) = Probability of B given A
# 
# P(A) = Initial probability of A
# 
# P(B) = Probability of B
# 
# ### Numerical Example
# 
# Suppose a company has two machines.
# 
# Machine A produces 60% of the products.
# 
# Machine B produces 40% of the products.
# 
# Suppose:
# 
# - 2% of products from Machine A are defective.
# - 5% of products from Machine B are defective.
# 
# If we randomly select a defective product, Bayes' Theorem can help us find the probability that it came from Machine B.
# 
# Bayes' Theorem helps us update our belief about the source of the product after getting new information that the product is defective.
# 
# ### Business Example
# 
# A company can use Bayes' Theorem to identify which customer group is more likely to respond to an advertisement based on new customer behaviour.
# 
# ### AI/ML Example
# 
# Bayes' Theorem is an important concept in classification.
# 
# For example, in spam email detection, we can calculate the probability that an email is spam after seeing certain words in the email.
# 
# Naive Bayes is a machine learning algorithm based on Bayes' Theorem.
# 
# ### Python Implementation
# 
# The following program demonstrates a simple Bayes' Theorem calculation.

# In[7]:


probability_a = 0.6
probability_b_given_a = 0.8
probability_b = 0.7

probability_a_given_b = (probability_b_given_a * probability_a) / probability_b

print("P(A):", probability_a)
print("P(B|A):", probability_b_given_a)
print("P(B):", probability_b)
print("P(A|B):", probability_a_given_b)
print("Percentage:", probability_a_given_b * 100, "%")


# ### Interpretation
# 
# Using Bayes' Theorem, the probability of A given B is approximately 0.686 or 68.57%.
# 
# This means that after getting information about event B, our probability for event A is updated to approximately 68.57%.
# 
# Bayes' Theorem is useful when new information becomes available and we want to update a probability.

# # Probability Rules
# 
# ### Definition
# 
# Probability Rules are basic rules used to calculate the probability of events.
# 
# They help us find the probability of one event, multiple events, or the probability that an event does not happen.
# 
# ### Formula
# 
# #### 1. Complement Rule
# 
# P(not A) = 1 - P(A)
# 
# This gives the probability that event A does not happen.
# 
# #### 2. Addition Rule
# 
# For mutually exclusive events:
# 
# P(A or B) = P(A) + P(B)
# 
# #### 3. Multiplication Rule
# 
# For independent events:
# 
# P(A and B) = P(A) × P(B)
# 
# ### Numerical Example
# 
# Suppose we roll a dice.
# 
# The probability of getting an even number is:
# 
# P(Even) = 3/6 = 0.5
# 
# Using the Complement Rule:
# 
# P(Not Even) = 1 - 0.5 = 0.5
# 
# So, the probability of getting an odd number is 0.5 or 50%.
# 
# ### Business Example
# 
# A company can use probability rules to calculate the chance of customers purchasing different products or responding to different marketing campaigns.
# 
# ### AI/ML Example
# 
# Probability rules are used in machine learning for calculating probabilities of events and predictions.
# 
# They are also used in classification algorithms and probabilistic models.
# 
# ### Python Implementation
# 
# The following program demonstrates the complement rule using a dice.

# In[8]:


probability_even = 3 / 6

probability_not_even = 1 - probability_even

print("Probability of Even Number:", probability_even)
print("Probability of Not Even Number:", probability_not_even)
print("Even Percentage:", probability_even * 100, "%")
print("Not Even Percentage:", probability_not_even * 100, "%")


# ### Interpretation
# 
# A dice has 6 possible outcomes.
# 
# There are 3 even numbers: 2, 4 and 6.
# 
# Therefore:
# 
# P(Even) = 3/6 = 0.5
# 
# Using the Complement Rule:
# 
# P(Not Even) = 1 - 0.5 = 0.5
# 
# So, the probability of getting an even number and an odd number is 50% each.

# # Random Variables
# 
# ### Definition
# 
# A Random Variable is a variable that assigns a numerical value to the outcome of a random event.
# 
# In simple words, a random variable stores the numerical result of an uncertain event.
# 
# There are two main types:
# 
# 1. Discrete Random Variable
# 2. Continuous Random Variable
# 
# ### Formula
# 
# There is no single formula for a random variable.
# 
# A random variable is usually represented by X.
# 
# Example:
# 
# X = Number of heads obtained when tossing a coin.
# 
# ### Numerical Example
# 
# Suppose we toss a coin 2 times.
# 
# Possible outcomes are:
# 
# HH, HT, TH, TT
# 
# Let X represent the number of Heads.
# 
# HH → X = 2
# 
# HT → X = 1
# 
# TH → X = 1
# 
# TT → X = 0
# 
# Therefore, X can have the values:
# 
# 0, 1, 2
# 
# ### Business Example
# 
# A company can define a random variable X as the number of products purchased by a customer.
# 
# For example:
# 
# Customer 1 → 2 products
# 
# Customer 2 → 5 products
# 
# Customer 3 → 1 product
# 
# Here, the number of products purchased is a random variable.
# 
# ### AI/ML Example
# 
# Random variables are used to represent uncertain values in machine learning.
# 
# For example, in a prediction problem, X can represent customer age, number of purchases, or other measurable values.
# 
# Probability distributions are used to describe how likely the different values of a random variable are.
# 
# ### Python Implementation
# 
# The following program shows the possible values of a random variable representing the number of Heads in two coin tosses.

# In[9]:


outcomes = ["HH", "HT", "TH", "TT"]

random_variable_values = []

for outcome in outcomes:
    number_of_heads = outcome.count("H")
    random_variable_values.append(number_of_heads)

print("Outcomes:", outcomes)
print("Random Variable Values:", random_variable_values)


# ### Interpretation
# 
# The random variable X represents the number of Heads obtained in two coin tosses.
# 
# For HH, X = 2.
# 
# For HT and TH, X = 1.
# 
# For TT, X = 0.
# 
# Therefore, the random variable can take the values 0, 1, and 2.
# 
# Random variables are useful for representing uncertain outcomes numerically.

# # Expected Value
# 
# ### Definition
# 
# Expected Value is the average value we expect from a random event when the experiment is repeated many times.
# 
# In simple words, Expected Value tells us the average outcome we can expect based on the probability of each outcome.
# 
# ### Formula
# 
# E(X) = Σ [x × P(x)]
# 
# Here,
# 
# x = Possible outcome
# 
# P(x) = Probability of that outcome
# 
# ### Numerical Example
# 
# Suppose a game has the following outcomes:
# 
# Win ₹100 with probability 0.5
# 
# Win ₹50 with probability 0.3
# 
# Win ₹0 with probability 0.2
# 
# Expected Value:
# 
# E(X) = (100 × 0.5) + (50 × 0.3) + (0 × 0.2)
# 
# E(X) = 50 + 15 + 0
# 
# E(X) = ₹65
# 
# Therefore, the expected value is ₹65.
# 
# ### Business Example
# 
# A company can use Expected Value to estimate the average revenue from different possible customer outcomes.
# 
# For example, a company can estimate expected revenue based on the probability of customers making different purchases.
# 
# ### AI/ML Example
# 
# Expected Value is used in probabilistic models and decision-making.
# 
# For example, a machine learning system can use expected values to estimate the average outcome based on different probabilities.
# 
# ### Python Implementation
# 
# The following program calculates the Expected Value of a simple game.

# In[10]:


outcomes = [100, 50, 0]
probabilities = [0.5, 0.3, 0.2]

expected_value = 0

for outcome, probability in zip(outcomes, probabilities):
    expected_value += outcome * probability

print("Outcomes:", outcomes)
print("Probabilities:", probabilities)
print("Expected Value: ₹", expected_value)


# In[ ]:




