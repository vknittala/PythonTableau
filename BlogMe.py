# -*- coding: utf-8 -*-
"""
Created on Tue OCT 05 2023

@author: Vidya Nittala
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx file
data = pd.read_excel('articles.xlsx')

#summary of the data
data.describe()

#summary of the column
data.info()

#counting hte number of articles per source
#format of groupby: df.groupby(['columnToGroup'])['columnToCountOrSum'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column: axis =1 is column and 0 is a row
data = data.drop('engagement_comment_plugin_count', axis = 1)


#Functions in Python
def thisFunction():
    print('This is my First Funciton')
    
print(thisFunction())

#this is a function with variables
def aboutMe(name, lname, location):
    fname = 'This is my Name - ' + name +' lastname is '+lname+'- location is '+location
    print (fname)
    return fname

aa = aboutMe('vidya', 'nittala', 'Roundrock') 
print ('my name - ' + aa)

#using for loops in functions
def favfood(food):
    for x in food:
        print('Top food is ' + x) 
    
fastfood = ['burgers', 'pizza', 'pie'] 
favfood(fastfood)
    
 
# #creating a keyword flag
# keyword = 'crash'

#creating a function with user input keyword to check in the title
#lets create a for loop to isolate each title row
def keywordflag(keyword):    
    length_data = len(data)
    keyword_flag = []    
    for x in range(0,length_data):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
                keyword_flag.append(flag)  
            else:
                flag = 0 
                keyword_flag.append(flag)          
        except:
            flag = 0            
            keyword_flag.append(flag)  
    return keyword_flag
keywordflag = keywordflag('murder')
    
#creating a new column in data dataframe

data['keyword_flag'] = pd.Series(keywordflag)
    
#SentimentIntensityAnalyzer
# sent_int = SentimentIntensityAnalyzer()
# text = data['title'][16]
# senti = sent_int.polarity_scores(text)

# neg = senti['neg']
# pos = senti['pos']
# new = senti['neu']

#adding a for loop to extract sentiment per title
title_neg_sentiment =[]
title_pos_sentiment =[]
title_neu_sentiment =[]
length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]    
        sent_int = SentimentIntensityAnalyzer()
        senti = sent_int.polarity_scores(text)
        neg = senti['neg']
        pos = senti['pos']
        neu = senti['neu']
    except:    
        neg = senti['neg']
        pos = senti['pos']
        new = senti['neu']
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

data.to_excel('BlogMe.xlsx', sheet_name = 'blogmeData', index = False )   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 
    
 
    
 
    
 
    
 
    
 
    
 