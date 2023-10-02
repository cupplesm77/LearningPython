# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 05:50:38 2023

@author: gravi
"""

# imports
import pandas as pd
import matplotlib.pyplot as plt

# construct a dataframe
dict = {'a': [1,2,3],
        'b': [4,5,6],
        'c': [7,8,9]
        }

data = pd.DataFrame(dict)
path = '../labs/data_csv'
data.to_csv(path)
print(data.head())
print('')
xlabel = 'b'
Ytest = data[[col for col in data.columns if col != xlabel]].values
Y1 = Ytest[:,0]
Y2 = Ytest[:,1]
print(f'Y1 = {Y1}')
print(f'Y2 = {Y2}')

def load_and_plot(path, xlabel, ylabel):
    """Load a data set and plot the first two principal components.
    Args:
    path (str): The location of a CSV file.
    Returns:
    tuple of ndarray: (features, labels)
    """
    data2 = pd.read_csv(path)
    X = data2[ylabel].values
    Y = data2[[col for col in data2.columns if col != xlabel]].values
    plt.scatter(X, Y)
    plt.show()
    return X, Y

x, y = load_and_plot(path, 'b', 'a')
print(x)
print('')
print(y)