#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance requests beautifulsoup4 pandas')


# In[6]:


get_ipython().system('pip install selenium pandas beautifulsoup4')


# In[8]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome()  # You can specify the path to chromedriver if not in PATH
driver.get("https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue")
time.sleep(5)  # Let the JavaScript load

# Get page source *before* closing the browser
html = driver.page_source

# Now you can safely quit
driver.quit()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract the correct table
revenue_table = soup.find("table", attrs={"class": "historical_data_table table"})

if revenue_table is None:
    raise ValueError("Revenue table not found. The website structure may have changed.")

# Convert to DataFrame
gme_revenue = pd.read_html(str(revenue_table))[0]
gme_revenue.columns = ["Date", "Revenue"]
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "").str.replace(",", "")
gme_revenue.dropna(inplace=True)

# Display the last 5 rows
print(gme_revenue.tail())


# In[ ]:




