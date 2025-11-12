#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import requests


# In[24]:


url = 'http://127.0.0.1:9696/predict'


# In[25]:


customer = {
  "gender": "female",
  "seniorcitizen": 0,
  "partner": "yes",
  "dependents": "no",
  "tenure": 1,
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "monthlycharges": 29.85,
  "totalcharges": 29.85
}


# In[26]:


response = requests.post(url, json=customer)


# In[27]:


print(response.json())


# In[ ]:




