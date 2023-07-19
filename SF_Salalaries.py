-- I used Python's Pandas library to read, explore and manipulate the data from a dataset I found on Kaggle (https://www.kaggle.com/kaggle/sf-salaries) to answer a few questions.

# importing Panda
import pandas as pd

# Reading SF Salaries data file from Kaggle (https://www.kaggle.com/kaggle/sf-salaries) as a dataframe called sal
sal=pd.read_csv('Salaries.csv')


# Checking the head of the Dataframe sal
sal.head()

# Using the .info() method to find out how many entries there are
sal.info()

# What is the average BasePay Salary?
sal['BasePay'].mean()
