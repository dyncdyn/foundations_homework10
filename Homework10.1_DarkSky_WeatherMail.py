#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[35]:


from dotenv import load_dotenv
load_dotenv()
import os


# In[36]:


API_KEY = os.getenv("dark_sky_api_key")
url = f'https://api.darksky.net/forecast/{API_KEY}/37.8267,-122.4233'

response = requests.get(url)
data = response.json()


# In[37]:


temperature = data['currently']['temperature']
summary = data['currently']['summary']
today = data['daily']['data'][0]
temp_feeling = 'warm'
high_temp = today['temperatureHigh']
low_temp = today['temperatureLow']


# In[38]:


print(f'Right now it is {temperature} degrees out and {summary}. Today will be {temp_feeling} with a high of {high_temp} and a low of {low_temp}. RAIN_WARNING.')


# In[ ]:





# In[39]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")
date_string


# In[ ]:





# In[40]:


response = requests.post("https://api.mailgun.net/v3/SANDBOX60ABF18F48944CD784D206060B22489E.MAILGUN.ORG/messages",
                         auth=("api", "ca3ad75486548de3d51a9fed045a8cd1-29b7488f-0b33e891"),
                         data={"from": "DYN.ACD@GMAIL.COM",
                               "to": ["DYN.ACD@GMAIL.COM"],
                               "subject": "Hello",
                               "text": "Testing some Mailgun awesomness!"})
response.text


# In[ ]:





# In[ ]:




