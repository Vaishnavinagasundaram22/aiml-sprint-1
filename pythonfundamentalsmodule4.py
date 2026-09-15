#!/usr/bin/env python
# coding: utf-8

# # Logging
# 
# ### Definition
# 
# Logging is used to record information about what happens inside a program.
# 
# ### Why Logging is Used
# 
# Logging helps us monitor the program, find errors, and understand what is happening while the program runs.
# 
# ### Real-World Example
# 
# In a bank application, logs can record when a user logs in, makes a payment, or when an error occurs.
# 
# ### Implementation
# 
# The following program creates a simple log message.
# 
# ### Explanation
# 
# The logging module is used to record information instead of using only print statements.

# In[1]:


import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")


# ### Program Explanation
# 
# In this program, the `logging` module is imported.
# 
# `logging.info()` records normal information.
# 
# `logging.warning()` records a warning.
# 
# `logging.error()` records an error.
# 
# Logging helps us track what happens in a program.

# # Why Logging is Used
# 
# ### Definition
# 
# Logging is used to keep a record of important events that happen in a program.
# 
# ### Why It Is Used
# 
# It helps developers monitor the program, identify errors, and understand program activities.
# 
# ### Real-World Example
# 
# In an online shopping application, logging can record when a user logs in, places an order, or when an error occurs.
# 
# ### Implementation
# 
# The following program records important activities using logging.
# 
# ### Explanation
# 
# Different log levels can be used to record different types of information.

# In[2]:


import logging

logging.basicConfig(level=logging.INFO)

logging.info("User logged in")
logging.warning("Low stock available")
logging.error("Payment failed")


# ### Program Explanation
# 
# In this program, logging records different events.
# 
# `INFO` records normal activities.
# 
# `WARNING` records a possible problem.
# 
# `ERROR` records an error.
# 
# This makes it easier to monitor and troubleshoot the program.

# # Print vs Logging
# 
# ### Definition
# 
# `print()` is mainly used to display information to the user.
# 
# Logging is used to record important information about the program for monitoring and troubleshooting.
# 
# ### Real-World Example
# 
# `print()` is like telling a customer something directly.
# 
# Logging is like keeping a record of what happened for future checking.
# 
# ### Implementation
# 
# The following program shows the difference between `print()` and logging.
# 
# ### Explanation
# 
# `print()` displays a message, while logging records messages with different log levels.

# In[4]:


import logging

logging.basicConfig(level=logging.INFO)

print("Program started")

logging.info("User logged in")
logging.warning("Low balance")
logging.error("Payment failed")


# ### Program Explanation
# 
# `print()` displays messages directly on the screen.
# 
# Logging records messages with levels such as `INFO`, `WARNING`, and `ERROR`.
# 
# Logging is more useful for monitoring and troubleshooting applications.

# ### Program Explanation
# 
# `print()` displays messages directly on the screen.
# 
# Logging records messages with levels such as `INFO`, `WARNING`, and `ERROR`.
# 
# Logging is more useful for monitoring and troubleshooting applications.

# # Logging Levels
# 
# ### Definition
# 
# Logging levels are used to show the importance or severity of a log message.
# 
# ### Types
# 
# - DEBUG → Detailed information for debugging
# - INFO → Normal program information
# - WARNING → Something may cause a problem
# - ERROR → An error has occurred
# - CRITICAL → A serious problem has occurred
# 
# ### Implementation
# 
# The following program uses different logging levels.
# 
# ### Explanation
# 
# Each logging level represents a different type of message.

# In[5]:


import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debugging information")
logging.info("Program started")
logging.warning("Low balance")
logging.error("Payment failed")
logging.critical("System failure")


# ### Program Explanation
# 
# `DEBUG` gives detailed information.
# 
# `INFO` records normal activities.
# 
# `WARNING` shows a possible problem.
# 
# `ERROR` shows an error.
# 
# `CRITICAL` shows a serious problem.

# # Logging Formatter
# 
# ### Definition
# 
# A logging formatter defines how log messages are displayed or stored.
# 
# ### Why It Is Used
# 
# It helps us include useful details such as time, log level, and message.
# 
# ### Real-World Example
# 
# In an application log, we may want to record when an error happened and what type of error occurred.
# 
# ### Implementation
# 
# The following program uses a formatter to format log messages.
# 
# ### Explanation
# 
# The formatter adds the time, logging level, and message to each log entry.

# In[6]:


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("Low balance")
logging.error("Payment failed")


# ### Program Explanation
# 
# `format` defines the structure of the log message.
# 
# `%(asctime)s` shows the time.
# 
# `%(levelname)s` shows the logging level.
# 
# `%(message)s` shows the actual log message.

# # File Handler
# 
# ### Definition
# 
# A File Handler is used to store log messages in a file.
# 
# ### Why It Is Used
# 
# It helps us save logs so that we can check them later.
# 
# ### Real-World Example
# 
# In a banking application, error details can be saved in a log file for future checking.
# 
# ### Implementation
# 
# The following program stores log messages in a file named `application.log`.
# 
# ### Explanation
# 
# The `FileHandler` sends logging messages to a file instead of displaying them only on the screen.

# In[7]:


import logging

logger = logging.getLogger("application")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("application.log")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Program started")
logger.warning("Low balance")
logger.error("Payment failed")


# ### Program Explanation
# 
# `FileHandler` creates and writes logs to `application.log`.
# 
# The formatter defines the format of each log message.
# 
# The logger records `INFO`, `WARNING`, and `ERROR` messages in the file.

# # Console Handler
# 
# ### Definition
# 
# A Console Handler is used to display log messages in the console or terminal.
# 
# ### Why It Is Used
# 
# It helps us see program activities and errors while the program is running.
# 
# ### Real-World Example
# 
# While testing an application, developers can see log messages directly in the terminal.
# 
# ### Implementation
# 
# The following program displays log messages in the console.
# 
# ### Explanation
# 
# The `StreamHandler` sends logging messages to the console.

# In[8]:


import logging

logger = logging.getLogger("application")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info("Program started")
logger.warning("Low balance")
logger.error("Payment failed")


# ### Program Explanation
# 
# `StreamHandler` displays log messages in the console.
# 
# The formatter defines the format of each message.
# 
# The logger records `INFO`, `WARNING`, and `ERROR` messages while the program is running.

# # Rotating Logs
# 
# ### Definition
# 
# Rotating logs means creating a new log file when the current log file reaches a certain size.
# 
# ### Why It Is Used
# 
# It prevents one log file from becoming too large.
# 
# ### Real-World Example
# 
# In a large application, many log messages are generated every day. Rotating logs helps manage these log files.
# 
# ### Implementation
# 
# The following program creates a rotating log file.
# 
# ### Explanation
# 
# `RotatingFileHandler` creates a new log file when the specified size is reached.

# In[9]:


import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("application")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "application.log",
    maxBytes=1000,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Application started")
logger.warning("This is a warning")
logger.error("An error occurred")


# ### Program Explanation
# 
# `RotatingFileHandler` manages the size of the log file.
# 
# `maxBytes=1000` sets the maximum file size.
# 
# `backupCount=3` keeps up to 3 backup log files.
# 
# This prevents the log file from growing too large.

# # Logging Best Practices
# 
# ### Definition
# 
# Logging best practices are simple rules used to create clear, useful, and manageable logs.
# 
# ### Important Practices
# 
# - Use proper logging levels.
# - Use meaningful log messages.
# - Do not log sensitive information.
# - Use formatters for clear log messages.
# - Store important logs in files when required.
# 
# ### Real-World Example
# 
# In a banking application, we can log that a payment failed, but we should not store passwords or PIN numbers in the logs.
# 
# ### Implementation
# 
# The following program demonstrates simple logging practices.
# 
# ### Explanation
# 
# The program uses the correct logging level and a meaningful message without storing sensitive information.

# In[10]:


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("User logged in successfully")
logging.warning("Account balance is low")
logging.error("Payment failed")


# ### Program Explanation
# 
# The program uses different logging levels for different situations.
# 
# The messages are clear and meaningful.
# 
# Sensitive information such as passwords and PINs should not be written in logs.

# In[ ]:




