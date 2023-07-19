# I used Python's Pandas library to read, explore and manipulate the data from a dataset I found on Kaggle (https://www.kaggle.com/kaggle/sf-salaries) to answer a few questions.

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


# What is the highest amount of OvertimePay in the dataset?
sal['OvertimePay'].max()


# What is the job title of JOSEPH DRISCOLL?
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# What is the name of highest paid person (including benefits)?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]

# What is the name of lowest paid person (including benefits)?
sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].min()]

# What was the average (mean) BasePay of all employees per year?
sal.groupby('Year').mean(numeric_only=True)['BasePay']

# How many unique job titles are there? 
sal['JobTitle'].nunique()

# What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head(5)

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
(sal[sal['Year']==2013]['JobTitle'].value_counts()==1).sum()

# How many people have the word Chief in their job title? 
sal[sal['JobTitle'].str.contains('chief', case=False)].count()

# Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr() # The coefficients are close to zero (-0.036878) and thus no correlations

