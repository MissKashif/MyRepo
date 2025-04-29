#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
import matplotlib.pyplot as plt

# Define make_graph function
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

# Make sure your DataFrame is correctly structured and sorted
tesla_data.sort_values(by="Date", inplace=True)

# Call the function to plot Tesla stock data
make_graph(tesla_data, "Tesla Stock Price Over Time")


# In[ ]:




