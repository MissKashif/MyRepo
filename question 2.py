#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Set up URL and headers to simulate a browser visit
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# Step 2: Fetch the page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Look for all tables
tables = soup.find_all("table")

# Step 4: Try to find the Tesla Quarterly Revenue table
revenue_table = None
for table in tables:
    if "Tesla Quarterly Revenue" in table.get_text():
        revenue_table = table
        break

# Step 5: Error if not found
if revenue_table is None:
    raise ValueError("Revenue table not found. Please check the page manually or adjust the scraping logic.")

# Step 6: Parse and clean the table
tesla_revenue = pd.read_html(str(revenue_table))[0]
tesla_revenue.columns = ["Date", "Revenue"]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(float)

# Step 7: Show the final DataFrame
print(tesla_revenue.head())


# In[ ]:




