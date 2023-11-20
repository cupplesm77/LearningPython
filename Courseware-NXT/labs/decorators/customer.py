# customer.py

import pandas as pd

customers = pd.read_csv("customer.csv", header=0, sep=" ")

print(customers)