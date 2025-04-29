#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ----------------------------------
# Question 3: GameStop Stock Data
# ----------------------------------
import yfinance as yf

gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()


# In[ ]:




