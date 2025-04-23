#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv

def write_csv(data, filepath):
    """
    Writes a list of dictionaries to a CSV file.

    Parameters:
    ----------
    data : list of dict
        A list where each element is a dictionary representing a row of data.
        All dictionaries must have the same keys (i.e., same columns).
    filepath : str
        The full file path (including filename and .csv extension) where the output CSV will be saved.

    Returns:
    -------
    None
        This function writes the file to disk but does not return any value.
    """
    # Return early if there's no data to write
    if not data:
        return

    # Open the file in write mode with UTF-8 encoding
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a DictWriter using the keys of the first dictionary as column headers
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())

        # Write the header row (column names)
        writer.writeheader()

        # Write each row of data
        writer.writerows(data)

