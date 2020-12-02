#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Code as c  #Importing code as c
import json       #To convert values into json format


# In[2]:


c.file()          #Creating and accessng file location


# In[3]:


a={"age":20,"Height":167,"Education":"Mecahnical Engineering"}
b=json.dumps(a)      #Converting to json format
c.create("Ashwin",b) #Creating using key and value


# In[4]:


c.read("Ashwin")     #Reading the data


# In[5]:


c.create("Ashwin",b) #Re-creating an existing data


# In[6]:


c.delete("Ashwin")   #Deletion operation


# In[7]:


c.create("Ashwin",b,10) #Creating using key,value and time limit


# In[8]:


c.read("Ashwin")        #Reading data after time limit exceeded


# In[9]:


c.delete("Ashwin")      #Deleting data after time limit exceeded


# In[ ]:


#Accessing data using treading


# In[10]:


t1=Thread(target=c.create("Aditiya",b))
t1.start()
t2=Thread(target=c.read("Aditiya"))
t2.start()
t3=Thread(target=c.create("Naveen",b))
t3.start()
t4=Thread(target=c.read("Naveen"))
t4.start()

