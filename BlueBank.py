# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:06:39 2023

@author: Vidya Nittala
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print (data)

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()


#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#create a column which has the exponent (EXP()) of the log to get the annual income
AnnualIncome = np.exp(loandata['log.annual.inc'])
loandata['AnnualIncome'] = AnnualIncome


#working with Arrays
#0d arra
arr = np.array(49)
#1d arra
arr = np.array([1,2,3,4])
#2d arra
arr = np.array([[1,2,3], [4,5,6]])

#working with if statements
"""
a=4000
b=5000
if b>a:
    print('b is greater')
elif a>b:
    print ('a is greater')
else:
    print ('a is equal to b')
"""
#FICO Score
fico = 400

# fico: The FICO credit score of the borrower.
# - 300 - 400: Very Poor
# - 400 - 600: Poor
# - 601 - 660: Fair
# - 660 - 700: Good
# - >= 700: Excellent

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif  fico >= 400 and fico <600:
    ficocat = 'Poor'
elif  fico >= 601 and fico <660:
    ficocat = 'Fair'
elif  fico >= 660 and fico <700:
    ficocat = 'Good'
elif  fico >= 700:
    ficocat = 'Excellent'
else: 
    ficocat = 'Undefined'
    
print(ficocat)

#forloops
fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print (x)
    y = x+' fruit'
    print(y)
    
for x in range(0,2):
    y= fruits[x]
    print(y)
    
    
length = len(loandata)
ficocat = []    
#applying for loops to loan data using first 10
for x in range(0,length):
    category = loandata['fico'][x]
    try:        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif  category >= 400 and category <600:
            cat = 'Poor'
        elif  category >= 601 and category <660:
            cat = 'Fair'
        elif  category >= 660 and category <700:
            cat = 'Good'
        elif  category >= 700:
            cat = 'Excellent'
        else: 
            cat = 'Undefined'     
    except:
        cat = 'Exception - Undefined'
        
    ficocat.append(cat)    
    
#if you're working with data analysis tasks, especially involving structured data like tables, 
#the pandas Series is a powerful and convenient data structure. 
#If you need a general-purpose collection of elements in Python, you would typically use a list.
#as of now ficocat is a list and we need series.
ficocat = pd.Series(ficocat)
loandata['fico.category'] =  ficocat

# df.loc as conditional statements
# df.loc[df[columnname]] condition, newcolumnname] = 'value if the condition is met'

# for interest rates, a new column name is wanted. rate>0.12 then high else low
loandata.loc[ loandata['int.rate']>0.12, 'int.rate.type'] = 'High'
loandata.loc[ loandata['int.rate']<=0.12, 'int.rate.type'] = 'Less'

#number of loans/rows by fico.category

# from your loandata, do groupby fico.category and the count the number of rows
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'orange', width = 0.2)
plt.show()

purplot = loandata.groupby(['purpose']).size()
purplot.plot.bar(color = 'blue', width = 0.2)
plt.show()

#scatter plots
# high annual income the debt to interest (dti) is low
xpoint =  loandata['dti'] 
ypoint = loandata['AnnualIncome']
plt.scatter(xpoint, ypoint, color = 'pink', edgecolors='red')
plt.show

#writing to csv
loandata.to_csv('LoanCleaned.csv', index = True)













