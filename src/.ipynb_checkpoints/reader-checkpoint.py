#!/usr/bin/env python
# coding: utf-8

import csv

def read_csv(filepath):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.

    Parameters
    ----------
    filepath : str
        Path to a standard CSV (comma-separated values) file.

    Returns
    -------
    list of dict
        A list where each element is a dictionary representing a row in the CSV file.
        Keys are column headers and values are string representations of cell data.
    """
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data
     
        

