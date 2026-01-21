# types of data structures:Ll

# 1. series: a 1-D array, capable of storing various data types.

import pandas as pd

x = [10,20,30,40,50]
var = pd.Series(x)
print(var)
print(type(var)) # type of var
print("value at idx 2",var[2]) # to access using index

# Creating a Series with a custom index
var = pd.Series(x, index=['a','b','c','d','e'])
print(var)

print(var['c'])  # access using label
