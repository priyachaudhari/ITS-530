{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from faker import Faker\
import pandas as pd\
import random\
\
# create a Faker instance\
fake = Faker()\
boolChoice = ['Yes', 'No']\
businessTravel = ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']\
department = ['Research & Development', 'Sales', 'Human Resources']\
educationField = ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources']\
gender = ['Male', 'Female']\
jobRole = ['Research Scientist', 'Manager', 'Sales Executive', 'Laboratory Technician', 'Research Director', 'Manufacturing Director']\
maritalStatus = ['Single', 'Divorced', 'Married']\
boolSingle = ['Y', 'N']\
\
\
# generate some dummy data\
rows = []\
for i in range(1700):\
    Age = fake.random_int(min=18, max=65)\
    Attrition =  random.choice(boolChoice)\
    BusinessTravel = random.choice(businessTravel)\
    Department = random.choice(department)\
    DistanceFromHome = fake.random_int(min=18, max=65)\
    Education = fake.random_int(min=1, max=5)\
    EducationField = random.choice(educationField)\
    EmployeeCount = 1\
    EmployeeNumber = 1701+i\
    Gender = random.choice(gender)\
    JobLevel = fake.random_int(min=1, max=5)\
    JobRole = random.choice(jobRole)\
    MaritalStatus = random.choice(maritalStatus)  \
    MonthlyIncome = fake.random_int(min=1000, max=19990) * 10\
    NumCompaniesWorked = fake.random_int(min=0, max=9)\
    Over18 = random.choice(boolSingle)\
    PercentSalaryHike = fake.random_int(min=11, max=25)\
    StandardHours = 8\
    StockOptionLevel = fake.random_int(min=0, max=3)\
    TotalWorkingYears = fake.random_int(min=1, max=40)\
    TrainingTimesLastYear = fake.random_int(min=0, max=9)\
    YearsAtCompany = fake.random_int(min=0, max=35)\
    YearsSinceLastPromotion = fake.random_int(min=0, max=15)\
    YearsWithCurrManager = fake.random_int(min=0, max=10)\
    rows.append((Age, Attrition, BusinessTravel, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, Gender, JobLevel, JobRole, MaritalStatus, MonthlyIncome, NumCompaniesWorked, Over18, PercentSalaryHike, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, YearsAtCompany, YearsSinceLastPromotion, YearsWithCurrManager))\
\
# create a pandas DataFrame from the dummy data\
df = pd.DataFrame(rows, columns=['Age', 'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education' , 'EducationField', 'EmployeeCount', 'EmployeeNumber', 'Gender', 'JobLevel', 'JobRole', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'Over18', 'PercentSalaryHike', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager'])\
\
# append the new data to your existing dataset\
existing_data = pd.read_csv('existing_data.csv')\
updated_data = pd.concat([existing_data, df], ignore_index=True)\
\
# save the updated dataset to a new CSV file\
updated_data.to_csv('updated_data.csv', index=False)\
}