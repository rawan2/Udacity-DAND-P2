#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset (Medical Appointment No Shows!)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# Medical Appointment No Shows dataset collects information
# from 100k medical appointments in
# Brazil and is focused on the question
# of whether or not patients show up
# for their appointment. 

# In[1]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
#  
# ### General Properties

# In[2]:


rawan = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
rawan.head()


# In[3]:


rawan.info()


# In[4]:


rawan.shape


# In[5]:


rawan.isnull().sum()


# In[6]:


rawan.duplicated().sum()


# In[7]:


rawan.nunique()


#  

#  
# 
# ### Data Cleaning  

# <span style="color:blue">1-Fix the name of the column<span>
# 

# In[8]:


rawan.rename(columns={'Handcap': 'Handicap'}, inplace=True)


# <span style="color:blue">2-Convert the datatype to datetime then apply changes<span>

# In[9]:


rawan['ScheduledDay']=pd.to_datetime(rawan['ScheduledDay'])


# In[10]:


rawan['AppointmentDay']=pd.to_datetime(rawan['AppointmentDay'])


# In[11]:


rawan.info()


# <span style="color:blue"> 3-Find if there 0 value or -1 in Age the delete it make sense<span>

# In[12]:


rawan.query('Age == "0"')


# In[13]:


rawan.drop(rawan.loc[rawan['Age']==0].index, inplace=True)
 


# In[14]:


rawan.query('Age == "-1"')


# In[15]:


rawan.drop(rawan.loc[rawan['Age']==-1].index, inplace=True)


# <span style="color:blue">5-Delete unused columns in analysis <span>

# In[16]:


rawan.drop(['PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay','Neighbourhood','Scholarship'], axis=1, inplace=True)


# In[17]:


rawan.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
#  
# 
# ### Research Question 1 (Comparison between  patients gender! )

# <span style="color:blue"> As you can see below the pie chart shows that the numbers of female patients is greater than male </span>

# In[18]:


F=rawan[rawan['Gender']== 'F'] 
M=rawan[rawan['Gender']== 'M'] 
 


# In[19]:


Fn='Female= '+str(len(F))
Mn='Male= '+str(len(M))
tgender = [Fn, Mn]
series = pd.Series([len(F),len(M)], 
                   index=tgender, 
                   name='Gender')

series.plot.pie(figsize=(5, 5))


# ### Research Question 2  (Comparison between Patients show up or not )

# <div style="color:blue"> As you can see below the pie chart shows that the numbers of Patients <span style="color:red">NOT</span> show up is greater than Patients show up</div>

# In[20]:


N=rawan[rawan['No-show']== 'No'] 
Y=rawan[rawan['No-show']== 'Yes'] 


# In[21]:


NO='NO= '+str(len(N))
YSE='YSE= '+str(len(Y))
showup = [NO, YSE]
series = pd.Series([len(N),len(Y)], 
                   index=showup, 
                   name='Patients show up')

series.plot.pie(figsize=(5, 5))


# ### Research Question 3  (Comparison between Patients SMS received & show up )

# <div style="color:blue"> As you can see below the pie chart shows that the numbers of Patients SMS <span style="color:red">NOT</span> received & show up is greater than Patients SMS received & show up</div>

# In[22]:


A=rawan.query('SMS_received== "1"')+ rawan[rawan['No-show']== 'Yes'] 
 
B=rawan.query('SMS_received== "0"')+rawan[rawan['No-show']== 'Yes'] 
 


# In[23]:


Ysms='SMS received & show up= '+str(len(A))
Nsms='SMS NOT received & show up= '+str(len(B))
showup = [Ysms,Nsms]
series = pd.Series([len(A),len(B)], 
                   index=showup, 
                   name='Patients SMS state & show up')

series.plot.pie(figsize=(5, 5))


# ### Research Question 4  (Comparison between Patients SMS received & Patients SMS NOT received )

# <div style="color:blue"> As you can see below the pie chart shows that the numbers of Patients SMS <span style="color:red">NOT</span> received is greater than Patients SMS received </div>

# In[24]:


c=rawan.query('SMS_received== "1"')
d=rawan.query('SMS_received== "0"')


# In[25]:


Yre='SMS received = '+str(len(c))
Nre='SMS NOT received = '+str(len(d))
rece = [Yre,Nre]
series = pd.Series([len(c),len(d)], 
                   index=rece, 
                   name='Patients SMS received ')

series.plot.pie(figsize=(5, 5))


# ### Research Question 5  (Age range )

#  <span style="color:blue"> The below boxplot chart shows that the most age is between 19 and 56</span>

# In[26]:


rawan.boxplot(column='Age')


# In[27]:


rawan.Age.describe()


# ### Research Question 6  (Comparison between Diseases )

#  <span style="color:blue">This bar chart shows that the Hipertension got the highest value </span>

# In[28]:


df = pd.DataFrame({'Diseases':[  'Hipertension','Diabetes', 'Alcoholism','Handicap'], 
                    'value':[rawan.Hipertension.sum(), rawan.Diabetes.sum(), rawan.Alcoholism.sum(),rawan.Handicap.sum()]})
df.plot.bar(x='Diseases', y='value', rot=0 ,title="Comparison between Diseases")
 
 
 
 


# <a id='conclusions'></a>
# ## Conclusions
# At the end the dataset was almost clean, And I found that the largest percentage is for patients who did not show up in the appointment and also for the patients did not receive the SMS, addition for the diseases I found that the Hipertension got the highest value , due to these founds I suggest the following solutions :<br> 1- send SMS to all patients .
# <br>2- Educating the community about the dangers of Hipertension disease and how to prevent it.
# <br>3- put a financial penalty for not attending the appointment :) .    
# 

# Reference:<br>
# <br>1-Numerical Python Course
# <br>2-pandas.pydata.org
# <br>3-matplotlib.org
