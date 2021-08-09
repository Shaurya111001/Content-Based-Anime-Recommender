#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
data = pd.read_csv('Anime_data.csv')
sample = data
st.title("Anime Recommender System")


# In[2]:


def a(s):
    s = s.strip('[]')
    s = s.replace("'","")
    s = s.split(',')
    return s
    


list = []
sample['Genre'].fillna("",inplace = True)
for i in sample['Genre']:
    s = a(i)
    for j in s:
        j = j.lstrip()
        if j not in list:
            list.append(j)


# In[3]:


list = pd.Series(list)


# In[4]:


for i in list:
    sample[i] = 0


c = 0
for i in sample['Genre']:
    for j in list:
        if i.find(j) != -1:
            sample.iloc[c, sample.columns.get_loc(j)] = 1
    c = c + 1
n = st.text_input("Enter Your Fav Anime show or movie (japanese or english)")

# In[5]:


sample = sample.drop('Type',axis=1)
sample = sample.drop('Producer',axis = 1)
sample = sample.drop('Synopsis',axis = 1)
sample = sample.drop('Studio',axis = 1)
#sample = sample.drop('Rating',axis = 1)
#sample = sample.drop('ScoredBy',axis = 1)
sample = sample.drop('Popularity',axis = 1)
sample = sample.drop('Members',axis = 1)
sample = sample.drop('Episodes',axis = 1)
sample = sample.drop('Source',axis = 1)
sample = sample.drop('Aired',axis = 1)
sample = sample.drop('Link',axis = 1)
sample = sample.drop('',axis = 1)


# In[6]:


#sample = sample.drop('Title',axis = 1)
#sample = sample.drop('Genre',axis = 1)


# In[7]:


sample['Rating'].fillna(5.0, inplace = True)
sample['ScoredBy'].fillna(1.0, inplace = True)
sample['Genre'] = sample['Genre'].replace(r'^\s*$', np.NaN, regex=True)
sample.dropna(subset = ["Genre"], inplace=True)


if n:
    name = sample.loc[sample['Title'].str.contains(n, case=False)]
    a = name['Title'].tolist()
    sel = st.selectbox("Select Shows from this : ", a)
    if sel:
        User_movies = sample.loc[sample['Title'] == sel]
        user_rating = User_movies['Rating'] 



        # In[9]:


        User_movies = User_movies.drop('Title',axis = 1)
        User_movies = User_movies.drop('Anime_id',axis =1)
        User_movies = User_movies.drop('Genre',axis =1)
        User_movies = User_movies.drop('Rating',axis =1)
        User_movies = User_movies.drop('ScoredBy',axis =1)


        # In[10]:



        # In[11]:



        # In[12]:


        User_matrix = User_movies.transpose().dot(user_rating)


        # In[13]

        # In[14]:


        all_rating = sample['Rating']
        all_genre = sample.set_index(sample['Anime_id'])
        all_genre = all_genre.drop('Anime_id', 1).drop('Title', 1).drop('Genre', 1).drop('Rating',1).drop('ScoredBy',1)


        # In[15]:


        # In[16]:


        recomm_table = ((all_genre*User_matrix).sum(axis=1))/(User_matrix.sum())
        recomm_table = recomm_table.sort_values(ascending=False)

        # In[20]:


        r = data.loc[data['Anime_id'].isin(recomm_table.head(10).keys())]
        st.dataframe(r['Title'])
        
st.write("Created by Shaurya Aditya singh")
st.write("Github : github.com/Shaurya111001")


# In[ ]:





# 

# In[ ]:




