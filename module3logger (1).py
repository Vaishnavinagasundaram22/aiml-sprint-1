#!/usr/bin/env python
# coding: utf-8

# <h3>What is Logging?</h3>
# 
# <p>Logging is the process of recording information about the activities and events that occur in an application.</p>

# In[1]:


import logging
from pathlib import Path


# <h3>Why is Logging Used?</h3>
# 
# <p>Logging is used to monitor application activities and identify problems.</p>

# <p><strong>class LoggerManager:</strong> Creates a class to manage application logging.</p>
# 
# <p><strong>__init__:</strong> Initializes the logger and log file.</p>
# 
# <p><strong>_create_log_directory:</strong> Creates the logs directory.</p>
# 
# <p><strong>_configure_logger:</strong> Configures the application logger.</p>
# 
# <p><strong>FileHandler:</strong> Writes logs into the application log file.</p>
# 
# <p><strong>Formatter:</strong> Defines the format of log messages.</p>
# 
# <p><strong>info():</strong> Records INFO messages.</p>
# 
# <p><strong>warning():</strong> Records WARNING messages.</p>
# 
# <p><strong>error():</strong> Records ERROR messages.</p>

# In[3]:


class LoggerManager:


    def __init__(self, log_file="logs/application.log"):
        self.log_file = Path(log_file)
        self._create_log_directory()
        self.logger = self._configure_logger()

    def _create_log_directory(self):

        self.log_file.parent.mkdir(parents=True, exist_ok=True) 

    def _configure_logger(self):

        logger = logging.getLogger("application")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)


# In[ ]:





# In[4]:


logger = LoggerManager()

print("Logger configured successfully")


# In[ ]:





# In[5]:


logger.info("Application started")
logger.info("Data processing started")

print("INFO logs generated")


# In[6]:


logger.warning("Input file contains missing values")

print("WARNING log generated")


# In[7]:


logger.error("Unable to process the input file")

print("ERROR log generated")


# In[8]:


log_path = Path("logs/application.log")

print("Log file exists:", log_path.exists())
print("Log file location:", log_path)


# In[ ]:




