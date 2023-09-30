# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:28:11 2023

@author: Vidya Nittala
"""
#PIP is a package-managing system to install or uninstall packages like pandas
import pandas as pd
import datetime as dt

"""
#playing with variables
#tuple is similar to list only thing is it could not change
var = ('apple', 'pear', 'banana')
var = range(10)
#dictionary
var = {'name':'Vidya', 'location':'RR'}
#set
var = {'apple', 'pear', 'banana'}
#boolean
var = False
"""
#file_name = pd.read_csv('file.csv') <--format of read_csv
data = pd.read_csv('transaction2.csv', sep=';')
#explore the first 5 rows using head
data.head()

#change column types
#day = data['Day'].astype(str)
#month = data['Month'].astype(str)
#myDate = day + month
                        
#combining data fields
# Sample DataFrame with Date as field
data['MyDate'] = data['Month'] +'-'+ data['Day'].astype(str) +'-'+  data['Year'].astype(str)   

#working with calculations
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#mathematical operations on Python
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction  = NumberOfItemsPurchased * CostPerItem
SellingPerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#variable = dataframe['column_name']
CostPerItem = data['CostPerItem']
SellingPricePerItem = data['SellingPricePerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#adding new column to the dataframe
data['CostPerTransaction']   = data['NumberOfItemsPurchased'] * data['CostPerItem']
data['SellingPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']
data['ProfitPerTransaction'] = data['NumberOfItemsPurchased'] * data['ProfitPerItem']

#profit = sales - cost
data['profit'] = data['SellingPerTransaction']  - data['CostPerTransaction'] 

#markup = (sales - cost )/cost
data['markup'] = data['profit'] / data['CostPerTransaction'] 
data['markup'] =  round(data['markup'], 2) 

#both rows and columns start with 0
data.iloc[0] #using iloc to view specific columns all rows
data.iloc[0:3]#using iloc to view specific 1st 3 rows
data.iloc[-5:]#using iloc to view specific last 5 rows
data.iloc[:,2]#using iloc to view specific last 3rd column all rows
data.iloc[4,2:9]#4th row 2nd to 9th column

#Feb-2-2019-12:50:00

#using split to split the client keywords field
#new_split_var = colum.str.split('sep', exapnd =True)
split_col = data['ClientKeywords'].str.split(',', expand = True)
#creating new columns for the split columns in client keywords and use replace function
data['ClientAge'] = split_col[0].str.replace('[', '')
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2].str.replace(']', '')

#using lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', ';')
#merging files: merge_datafile = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on ='Month')

#dropping columns
#df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day','Month', 'Year','Time'] , axis = 1)
      
#exporting the file to csv
data.to_csv('ValueIncCleaned.csv', index = False)
  
# syntax to get the index of rows in a pandas DataFrame whose column matches specific values:
#df.index[df['column_name']==value].tolist()
myItemList = data.index[data['ItemCode'] == 465780].tolist() 














