#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_average_demand(data):
    """
    Calculate the average (arithmetic mean) of 'Actual_Demand' from a list of dictionaries.

    Parameters
    ----------
    data : list of dict
        A list where each element is a dictionary representing a row of data. 
        Each dictionary must include the key 'Actual_Demand' with numeric values.

    Returns
    -------
    int
        The average value of 'Actual_Demand', truncated to an integer.
    """
    # Get the total sum of all 'Actual_Demand' values
    total = sum(row["Actual_Demand"] for row in data)

    # Get the number of valid rows
    count = len(data)

    # Return the average as an integer
    return int(total / count)

def get_top_products(data, top_n=5):
    """
    Identify the top N products by total 'Units_Shipped'.

    Parameters
    ----------
    data : list of dict
        A list where each element is a dictionary representing a row of data. 
        Each dictionary must include the keys 'Product_ID' and 'Units_Shipped'.

    top_n : int, optional
        The number of top products to return (default is 5).

    Returns
    -------
    list of tuples
        A list of (Product_ID, total_units_shipped) tuples, sorted in descending order.
    """
    product_totals = {}

    for row in data:
        product = row["Product_ID"]
        units = row["Units_Shipped"]

        # Accumulate shipped units per product
        product_totals[product] = product_totals.get(product, 0) + int(units)

    # Sort products by total units shipped, in descending order
    sorted_products = sorted(product_totals.items(), key=lambda x: x[1], reverse=True)

    return sorted_products[:top_n]


# In[ ]:




