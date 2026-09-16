#!/usr/bin/env python
# coding: utf-8

# # SQL
# 
# ### Definition
# 
# SQL stands for Structured Query Language.
# 
# It is used to create, store, retrieve, update, and manage data in databases.
# 
# ### Why It Is Used
# 
# SQL helps applications work with large amounts of structured data.
# 
# ### Real-World Example
# 
# A college database can store student names, ages, courses, and marks. SQL can be used to retrieve and update this information.
# 
# ### Implementation
# 
# The following program creates a simple student table and retrieves data from it.
# 
# ### Explanation
# 
# `CREATE TABLE` creates a table, `INSERT` adds data, and `SELECT` retrieves data.

# In[1]:


import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO students VALUES (1, 'Rahul', 22)
""")

cursor.execute("SELECT * FROM students")

for student in cursor.fetchall():
    print(student)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `sqlite3` is used to connect Python with a database.
# 
# `CREATE TABLE` creates the students table.
# 
# `INSERT` adds student data.
# 
# `SELECT` retrieves the stored data.
# 
# This demonstrates how SQL is used to manage data in a database.

# # Database Design
# 
# ### Definition
# 
# Database design is the process of organizing data into tables and defining relationships between them.
# 
# ### Why It Is Used
# 
# It helps store data in an organized way and reduces duplicate data.
# 
# ### Real-World Example
# 
# In a college system, student details and course details can be stored in separate tables.
# 
# ### Implementation
# 
# The following program creates two related tables.
# 
# ### Explanation
# 
# The `students` table stores student details, and the `courses` table stores course details.

# In[2]:


import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
)
""")

connection.commit()
connection.close()

print("Tables created successfully")


# ### Program Explanation
# 
# The database contains separate tables for students and courses.
# 
# `PRIMARY KEY` uniquely identifies each record.
# 
# Separating data into tables keeps the database organized.
# 
# This is a basic example of database design.

# # SQL Queries
# 
# ### Definition
# 
# An SQL query is a command used to perform an operation on data in a database.
# 
# ### Why It Is Used
# 
# SQL queries help us retrieve, add, update, and delete data from database tables.
# 
# ### Real-World Example
# 
# A college application can use an SQL query to display all students from the student table.
# 
# ### Implementation
# 
# The following program uses a `SELECT` query to retrieve student details.
# 
# ### Explanation
# 
# The `SELECT` query is used to fetch data from a database table.

# In[3]:


import sqlite3

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()


# ### Program Explanation
# 
# `SELECT * FROM students` retrieves all records from the students table.
# 
# `fetchall()` gets all the retrieved records.
# 
# The `for` loop displays each student record.
# 
# This demonstrates how SQL queries are used to retrieve data.

# # SQL Joins
# 
# ### Definition
# 
# A SQL JOIN is used to combine data from two or more related tables.
# 
# ### Why It Is Used
# 
# It helps us retrieve related information stored in different tables.
# 
# ### Real-World Example
# 
# A college database may store student details and course details in separate tables. A JOIN can combine them to display the student's course.
# 
# ### Implementation
# 
# The following program uses an INNER JOIN to combine two tables.
# 
# ### Explanation
# 
# The `INNER JOIN` returns records that have matching values in both tables.

# In[5]:


import sqlite3

connection = sqlite3.connect("college_join.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    course_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT
)
""")

cursor.execute("INSERT INTO courses VALUES (1, 'Python')")
cursor.execute("INSERT INTO students VALUES (1, 'Rahul', 1)")

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The `students` and `courses` tables contain related data.
# 
# `INNER JOIN` combines the tables using `course_id`.
# 
# The `ON` condition specifies how the two tables are related.
# 
# The result displays the student name along with the course name.

# # UNION
# 
# ### Definition
# 
# `UNION` is used to combine the results of two or more `SELECT` queries.
# 
# ### Why It Is Used
# 
# It helps us combine similar data from different queries into a single result.
# 
# ### Real-World Example
# 
# A college can have students from different departments. `UNION` can combine student names from two different department tables.
# 
# ### Implementation
# 
# The following program combines data from two tables using `UNION`.
# 
# ### Explanation
# 
# `UNION` combines the results and removes duplicate values.

# In[6]:


import sqlite3

connection = sqlite3.connect("college_union.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS python_students (name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS sql_students (name TEXT)")

cursor.execute("DELETE FROM python_students")
cursor.execute("DELETE FROM sql_students")

cursor.execute("INSERT INTO python_students VALUES ('Rahul')")
cursor.execute("INSERT INTO sql_students VALUES ('Priya')")

cursor.execute("""
SELECT name FROM python_students
UNION
SELECT name FROM sql_students
""")

for student in cursor.fetchall():
    print(student)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The first `SELECT` gets names from `python_students`.
# 
# The second `SELECT` gets names from `sql_students`.
# 
# `UNION` combines both results into one result.
# 
# Duplicate values are removed automatically.

# # CASE
# 
# ### Definition
# 
# `CASE` is used to apply conditions in an SQL query and return different values based on those conditions.
# 
# ### Why It Is Used
# 
# It helps us categorize or display data based on a condition.
# 
# ### Real-World Example
# 
# A college can classify students based on their marks as Pass or Fail.
# 
# ### Implementation
# 
# The following program uses `CASE` to classify students based on their marks.
# 
# ### Explanation
# 
# If the marks are 40 or above, the result is `Pass`. Otherwise, it is `Fail`.

# In[7]:


import sqlite3

connection = sqlite3.connect("students_case.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 35)")

cursor.execute("""
SELECT name, marks,
CASE
    WHEN marks >= 40 THEN 'Pass'
    ELSE 'Fail'
END AS result
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The `CASE` statement checks the student's marks.
# 
# If marks are 40 or above, it returns `Pass`.
# 
# Otherwise, it returns `Fail`.
# 
# This demonstrates how SQL can apply conditions while retrieving data.

# # Subquery
# 
# ### Definition
# 
# A subquery is a query written inside another SQL query.
# 
# ### Why It Is Used
# 
# It helps us use the result of one query inside another query.
# 
# ### Real-World Example
# 
# A college can find students whose marks are greater than the average marks of all students.
# 
# ### Implementation
# 
# The following program uses a subquery to find students who scored above average.
# 
# ### Explanation
# 
# The inner query calculates the average marks, and the outer query finds students whose marks are greater than that average.

# In[8]:


import sqlite3

connection = sqlite3.connect("students_subquery.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 60)")
cursor.execute("INSERT INTO students VALUES ('Arun', 40)")

cursor.execute("""
SELECT name, marks
FROM students
WHERE marks > (
    SELECT AVG(marks)
    FROM students
)
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The inner query calculates the average marks using `AVG()`.
# 
# The outer query selects students whose marks are greater than the average.
# 
# This demonstrates how one SQL query can be used inside another query.

# # CTE
# 
# ### Definition
# 
# CTE stands for Common Table Expression.
# 
# It is a temporary result created using the `WITH` keyword and used inside an SQL query.
# 
# ### Why It Is Used
# 
# It makes complex SQL queries easier to read and understand.
# 
# ### Real-World Example
# 
# A college can first create a temporary list of students who scored above 60 and then retrieve their details.
# 
# ### Implementation
# 
# The following program uses a CTE to find students who scored above 60.
# 
# ### Explanation
# 
# The `WITH` statement creates the temporary result, which is then used by the main query.

# In[9]:


import sqlite3

connection = sqlite3.connect("students_cte.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 55)")
cursor.execute("INSERT INTO students VALUES ('Arun', 75)")

cursor.execute("""
WITH passed_students AS (
    SELECT name, marks
    FROM students
    WHERE marks > 60
)
SELECT * FROM passed_students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The `WITH` keyword creates a CTE named `passed_students`.
# 
# The CTE selects students who scored more than 60.
# 
# The main query retrieves the data from the CTE.
# 
# This makes the query easier to understand and organize.

# # Views
# 
# ### Definition
# 
# A View is a virtual table created from an SQL query.
# 
# ### Why It Is Used
# 
# It helps us save frequently used queries and display required data easily.
# 
# ### Real-World Example
# 
# A college can create a view containing only student names and marks instead of showing all columns from the main table.
# 
# ### Implementation
# 
# The following program creates a view and retrieves data from it.
# 
# ### Explanation
# 
# `CREATE VIEW` creates a virtual table based on an SQL query.

# In[10]:


import sqlite3

connection = sqlite3.connect("students_view.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 75)")

cursor.execute("""
CREATE VIEW IF NOT EXISTS student_marks AS
SELECT name, marks
FROM students
""")

cursor.execute("SELECT * FROM student_marks")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# The `students` table stores student details.
# 
# `CREATE VIEW` creates a virtual table named `student_marks`.
# 
# The view contains only the `name` and `marks` columns.
# 
# The `SELECT` query retrieves data from the view.

# # Indexes
# 
# ### Definition
# 
# An index is used to make searching and retrieving data from a database table faster.
# 
# ### Why It Is Used
# 
# It improves query performance when searching for data in a large table.
# 
# ### Real-World Example
# 
# A college database may have thousands of students. An index on the student name can help find a student faster.
# 
# ### Implementation
# 
# The following program creates an index on the student name.
# 
# ### Explanation
# 
# `CREATE INDEX` creates an index that helps the database search the column efficiently.

# In[11]:


import sqlite3

connection = sqlite3.connect("students_index.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_student_name
ON students(name)
""")

cursor.execute("""
SELECT * FROM students
WHERE name = 'Rahul'
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `CREATE INDEX` creates an index on the `name` column.
# 
# The index helps the database find matching names more efficiently.
# 
# The `SELECT` query searches for a student using the indexed column.
# 
# Indexes are especially useful when working with large tables.

# # Window Functions
# 
# ### Definition
# 
# Window functions perform calculations on a group of related rows without combining them into one row.
# 
# ### Why It Is Used
# 
# They help us compare each row with other rows and calculate rankings or previous and next values.
# 
# ### Real-World Example
# 
# A college can use window functions to rank students based on their marks.
# 
# ### Implementation
# 
# The following program uses `ROW_NUMBER()` to give each student a rank.
# 
# ### Explanation
# 
# `ROW_NUMBER()` assigns a unique number to each row based on the marks.

# In[12]:


import sqlite3

connection = sqlite3.connect("students_window.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 92)")
cursor.execute("INSERT INTO students VALUES ('Arun', 75)")

cursor.execute("""
SELECT name, marks,
ROW_NUMBER() OVER (ORDER BY marks DESC) AS rank
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `ROW_NUMBER()` assigns a number to each student.
# 
# `ORDER BY marks DESC` arranges students from highest marks to lowest marks.
# 
# The result shows each student's name, marks, and rank.
# 
# This demonstrates how a window function works.

# # ROW_NUMBER()
# 
# ### Definition
# 
# `ROW_NUMBER()` is a window function that assigns a unique number to each row.
# 
# ### Why It Is Used
# 
# It is used to give a sequence or position to records based on a specific order.
# 
# ### Real-World Example
# 
# A college can use `ROW_NUMBER()` to assign positions to students based on their marks.
# 
# ### Implementation
# 
# The following program assigns a row number to each student based on marks.
# 
# ### Explanation
# 
# `ROW_NUMBER()` gives each student a unique number, starting from 1.

# In[13]:


import sqlite3

connection = sqlite3.connect("students_row_number.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students VALUES ('Priya', 92)")
cursor.execute("INSERT INTO students VALUES ('Arun', 75)")

cursor.execute("""
SELECT name, marks,
ROW_NUMBER() OVER (ORDER BY marks DESC) AS row_number
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `ROW_NUMBER()` assigns a unique number to every row.
# 
# `ORDER BY marks DESC` arranges students from highest marks to lowest marks.
# 
# The result contains the student's name, marks, and row number.

# # RANK()
# 
# ### Definition
# 
# `RANK()` is a window function used to assign a rank to each row based on a specific order.
# 
# ### Why It Is Used
# 
# It is useful for ranking records such as students based on their marks.
# 
# ### Real-World Example
# 
# If two students have the same marks, both students receive the same rank.
# 
# ### Implementation
# 
# The following program ranks students based on their marks.
# 
# ### Explanation
# 
# `RANK()` gives the same rank to rows with the same value and skips the next rank.

# In[14]:


import sqlite3

connection = sqlite3.connect("students_rank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 90)")
cursor.execute("INSERT INTO students VALUES ('Priya', 90)")
cursor.execute("INSERT INTO students VALUES ('Arun', 75)")

cursor.execute("""
SELECT name, marks,
RANK() OVER (ORDER BY marks DESC) AS student_rank
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `RANK()` assigns ranks based on marks.
# 
# Rahul and Priya have the same marks, so they receive the same rank.
# 
# The next student receives rank 3 because `RANK()` skips a rank after a tie.

# # DENSE_RANK()
# 
# ### Definition
# 
# `DENSE_RANK()` is a window function used to assign ranks to rows based on a specific order.
# 
# ### Why It Is Used
# 
# It is useful when we want the same rank for equal values without skipping the next rank.
# 
# ### Real-World Example
# 
# If two students have the same marks, both receive the same rank, and the next student gets the next consecutive rank.
# 
# ### Implementation
# 
# The following program ranks students based on their marks.
# 
# ### Explanation
# 
# `DENSE_RANK()` gives the same rank to equal values and does not skip any rank.

# In[15]:


import sqlite3

connection = sqlite3.connect("students_dense_rank.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 90)")
cursor.execute("INSERT INTO students VALUES ('Priya', 90)")
cursor.execute("INSERT INTO students VALUES ('Arun', 75)")

cursor.execute("""
SELECT name, marks,
DENSE_RANK() OVER (ORDER BY marks DESC) AS student_rank
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `DENSE_RANK()` assigns ranks based on marks.
# 
# Rahul and Priya have the same marks, so they receive the same rank.
# 
# Arun receives rank 2 because `DENSE_RANK()` does not skip ranks.

# # LAG()
# 
# ### Definition
# 
# `LAG()` is a window function used to access the value from a previous row.
# 
# ### Why It Is Used
# 
# It helps us compare the current row with the previous row.
# 
# ### Real-World Example
# 
# A company can use `LAG()` to compare the current month's sales with the previous month's sales.
# 
# ### Implementation
# 
# The following program compares each student's marks with the previous student's marks.
# 
# ### Explanation
# 
# `LAG()` returns the marks from the previous row based on the given order.

# In[16]:


import sqlite3

connection = sqlite3.connect("students_lag.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 60)")
cursor.execute("INSERT INTO students VALUES ('Priya', 75)")
cursor.execute("INSERT INTO students VALUES ('Arun', 90)")

cursor.execute("""
SELECT name, marks,
LAG(marks) OVER (ORDER BY marks) AS previous_marks
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `LAG()` gets the value from the previous row.
# 
# The students are ordered by their marks.
# 
# For the first row, there is no previous value, so it returns `NULL`.
# 
# This helps compare the current value with the previous value.

# # LEAD()
# 
# ### Definition
# 
# `LEAD()` is a window function used to access the value from the next row.
# 
# ### Why It Is Used
# 
# It helps us compare the current row with the next row.
# 
# ### Real-World Example
# 
# A company can use `LEAD()` to compare the current month's sales with the next month's sales.
# 
# ### Implementation
# 
# The following program compares each student's marks with the next student's marks.
# 
# ### Explanation
# 
# `LEAD()` returns the marks from the next row based on the given order.

# In[17]:


import sqlite3

connection = sqlite3.connect("students_lead.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.execute("INSERT INTO students VALUES ('Rahul', 60)")
cursor.execute("INSERT INTO students VALUES ('Priya', 75)")
cursor.execute("INSERT INTO students VALUES ('Arun', 90)")

cursor.execute("""
SELECT name, marks,
LEAD(marks) OVER (ORDER BY marks) AS next_marks
FROM students
""")

for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()


# ### Program Explanation
# 
# `LEAD()` gets the value from the next row.
# 
# The students are ordered by their marks.
# 
# For the last row, there is no next value, so it returns `NULL`.
# 
# This helps compare the current value with the next value.

# In[ ]:




