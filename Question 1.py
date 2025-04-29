#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import required libraries
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objs as go

# ----------------------------------
# Question 1: Tesla Stock Data
# ----------------------------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()


# In[3]:


get_ipython().system('pip install yfinance')


# In[4]:


get_ipython().system('pip install yfinance')


# In[5]:


get_ipython().system('pip install yfinance pandas plotly requests beautifulsoup4')


# In[ ]:




