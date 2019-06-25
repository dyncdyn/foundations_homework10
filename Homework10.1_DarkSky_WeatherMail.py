#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[37]:


from dotenv import load_dotenv
load_dotenv()
import os


# In[38]:


API_KEY = os.getenv("dark_sky_api_key")
url = f'https://api.darksky.net/forecast/{API_KEY}/37.8267,-122.4233'

response = requests.get(url)
data = response.json()
data


# In[ ]:





# In[39]:


from datetime import datetime
timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))


# In[40]:


data.keys()


# In[41]:


temperature = data['currently']['temperature']
summary = data['currently']['summary']
today = data['daily']['data'][0]
temp_feeling = 'warm'
high_temp = today['temperatureHigh']
low_temp = today['temperatureLow']


# In[42]:


print(f'Right now it is {temperature} degrees out and {summary}. Today will be {temp_feeling} with a high of {high_temp} and a low of {low_temp}. RAIN_WARNING.')


# In[ ]:





# In[43]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d, %Y")
date_string


# In[45]:


api_key = os.getenv('mailgun_api_key')


# In[46]:


response = requests.post("https://api.mailgun.net/v3/SANDBOX60ABF18F48944CD784D206060B22489E.MAILGUN.ORG/messages",
                         auth=("api", api_key),
                         data={"from": "DYN.ACD@GMAIL.COM",
                               "to": ["DYN.ACD@GMAIL.COM"],
                               "subject": "8AM Weather forecast:.",
                               "text": "Good Morning! Here is today's weather forecast."})
response.text


# In[ ]:





# In[ ]:




