#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv("C:/Users/Lenovo/Downloads/Diwali Sales Data.csv", encoding='windows-1252')


# In[3]:


df


# In[4]:


df.shape 


# In[5]:


df.size


# In[6]:


df.describe()


# In[7]:


df.head(10) # first 10 rows


# In[8]:


df.tail(10) # last 10 rows


# In[9]:


df.info() # to give brief info about data


# In[10]:


# we can drop unrelated or blank columns
df.drop(["Status", "unnamed1"], axis = 1, inplace = True)
# axix == whole row 


# In[11]:


df.info() # it gives total info and detailed about each and every column


# In[12]:


pd.isnull(df)


# In[13]:


pd.isnull(df).sum()


# there is 12 null values in Amount column

# In[14]:


df.shape


# In[15]:


# now drop null values
df.dropna(inplace=True)


# In[16]:


df.shape 


# In[17]:


# check Null values agaian
pd.isnull(df).sum()


# Now there is no Null Values

# In[18]:


# Inplace = True 
# Example 
data_test = [["Ram", 20], ["Aakash", 18], ["Scope", ], ['Sumago', 100]]

df_test = pd.DataFrame(data_test, columns=["Name", "Age"])

df_test


# In[19]:


#There is one Null value
# now we can remove it
df_test.dropna()


# In[20]:


df_test # it will show again null value 


# In[21]:


# now we use Inplace = True
df_test.dropna(inplace=True)
df_test


# In[22]:


# Change data type of coulmn Amount (There is float values)
df["Amount"] = df["Amount"].astype("int")


# In[23]:


df["Amount"].dtypes


# In[24]:


df.columns


# In[25]:


df.describe() # It gives returns description of the data in the DataFrame (count, mean,std deviation, etc)


# In[26]:


# i just want describe specifics columns 
df[["Age", 'Orders', "Amount"]].describe()


# # Exploaratory Data Analysis

# # Gender

# In[27]:


ax = sns.countplot(x = "Gender", data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)


# In[29]:


sales_gender = df.groupby(["Gender"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)
sns.barplot(x = "Gender", y = "Amount", data = sales_gender)


# Females are more buyers than men

# # Age 

# In[30]:


ax = sns.countplot(x = "Age Group", hue = "Gender", data= df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


ax = sns.countplot(x = "Age Group", data= df) # Wuthout hue


# In[32]:


# Compare total Amount vs Age group
sales_age = df.groupby(["Age Group"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.barplot(x = "Age Group", y = "Amount", data = sales_age)


# from above group we can see that most of the buyers are age group between 26-35 yrs female.

# # State 

# In[33]:


df.columns


# In[34]:


# Total number of oreder from top 10 states  
sales_states = df.groupby(["State"], as_index = False)["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)

sns.set(rc = {"figure.figsize":(15,5)})
sns.barplot(data = sales_states, x = "State", y ="Orders")


# In[35]:


# Total amount/sales from top 10 states 
sales_state = df.groupby(["State"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False).head(10)

sns.set(rc = {"figure.figsize":(15,5)})
sns.barplot(data = sales_state, x = "State", y = "Amount")


# From Above Graphs we can see that most of the orders from uttar pradesh, Maharshtra and karnataka and intresting fact is more amount spent by Haryana and bihar than kerala but kerala state has more orders

# # Marital status

# In[36]:


ax = sns.countplot(data = df, x = "Marital_Status")
sns.set(rc = {"figure.figsize":(5,3)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[37]:


sales_state = df.groupby(["Marital_Status", "Gender"],as_index= False)["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.set(rc={'figure.figsize': (6,3)})
sns.barplot(data = sales_state, x = "Marital_Status", y = "Amount", hue = "Gender")


# from above graph more shopping is done by married females and purchasing power is also more than men

# # Occupation 

# In[38]:


sales_state = df.groupby(["Occupation"], as_index = False)["Amount"].sum().sort_values(by = "Amount", ascending = False)
sns.set(rc = {"figure.figsize": (20,5)})
sns.barplot(data = sales_state, x = "Occupation", y = "Amount")


# From above graph we can see that most if the buyers are working in IT sector, Healthcare, and Aviation Sector

# # Product Category 

# In[39]:


sales_state = df.groupby(["Product_Category"], as_index = False)["Amount"].sum().sort_values(by ="Amount", ascending = False).head(10)

sns.set(rc= {"figure.figsize":(20,5)})
sns.barplot(data= sales_state, x = "Product_Category", y = "Amount")


# In[40]:


sns.set(rc= {"figure.figsize":(25,8)})
ax = sns.countplot(data= df, x = "Product_Category")

for bars in ax.containers:
    ax.bar_label(bars)


# from above graph we can see that there is max orders of clothing , Food ane electronic Gadgets respectively (By Product Category) but when we analyze By amount Food,Clothing and Electronic Gadgets respectively.

# In[41]:


# To understand top 10 most sold products
sales_state = df.groupby(["Product_ID"],as_index = False)["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)
sns.set(rc = {"figure.figsize":(15,5)})
sns.barplot(data = sales_state, x = 'Product_ID', y = "Orders")                                                                       
                                                                        
                                                                        


# # Conclusion :-

# The married Women age group 26-35 years from UP, MH, And Karnataka working in IT sector, Healthcare Sector, and Aviation are more likely to buy food, cloth, and Electronic products 

# In[ ]:




