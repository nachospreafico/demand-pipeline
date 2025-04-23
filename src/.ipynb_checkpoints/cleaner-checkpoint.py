#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clean_data(data):
    """
    Standardizes and cleans the dataset by converting numeric fields to float and dropping incomplete rows.

    Parameters
    ----------
    data : list of dict
        A list where each element is a dictionary representing a row of data.
        Each dictionary must contain the keys 'Planned_Demand', 'Actual_Demand', and 'Units_Shipped'.

    Returns
    -------
    list of dict
        A new list containing only rows where all required numeric fields are present and valid.
        The structure and order of fields in each dictionary remain unchanged.
    """
    cleaned = []

    for row in data:
        try:
            # Attempt to convert numeric fields to float, treat empty strings or invalid entries as None
            row["Planned_Demand"] = int(float(row["Planned_Demand"])) if row["Planned_Demand"] else None
            row["Actual_Demand"] = int(float(row["Actual_Demand"])) if row["Actual_Demand"] else None
            row["Units_Shipped"] = int(float(row["Units_Shipped"])) if row["Units_Shipped"] else None

            # Only keep rows where all three key fields are valid (not None)
            if None not in (row["Planned_Demand"], row["Actual_Demand"], row["Units_Shipped"]):
                cleaned.append(row)

        except (ValueError, TypeError):
            # Skip rows with conversion issues (e.g., non-numeric strings or malformed values)
            continue

    return cleaned