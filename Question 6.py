#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import yfinance as yf

# Define the make_graph function
def make_graph(stock_data, title):
    plt.figure(figsize=(14, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Step 1: Extract GameStop Stock Data using yfinance
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

# Step 2: Call make_graph function to plot GameStop stock data
make_graph(gme_data, "GameStop Stock Price Over Time")


# In[ ]:




