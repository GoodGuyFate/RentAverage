import pandas as pd
import numpy as np
import scipy.stats as stats
import csv

with open(".csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    data = list(reader)

max_rent = 1000000  # Adjust this threshold as needed

filtered_data = [(row[0], float(row[1])) for row in data if float(row[1]) <= max_rent]

with open(".csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(filtered_data)
