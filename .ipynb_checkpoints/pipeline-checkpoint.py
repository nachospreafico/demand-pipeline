#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Import necessary modules
from src.reader import read_csv
from src.cleaner import clean_data
from src.analyzer import get_average_demand, get_top_products
from src.writer import write_csv

# Step 1: Read raw data
raw_data = read_csv('data/raw/dummy_demand_data.csv')

# Step 2: Clean and standardize data
cleaned_data = clean_data(raw_data)

# Step 3: Analyze cleaned data
avg_demand = get_average_demand(cleaned_data)
top_products = get_top_products(cleaned_data)

# Step 4: Display results
print(f"\n📊 Average Actual Demand: {avg_demand}\n")
print("🏆 Top Products by Units Shipped:")
for i, (product, units) in enumerate(top_products, 1):
    print(f"{i}. {product} → {int(units)} units")

# Step 5: Write cleaned data to new CSV
write_csv(cleaned_data, 'data/clean/cleaned_data.csv')


# In[ ]:




