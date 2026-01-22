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
print(var[[1, 3]])  # access multiple values

# Some useful Series attributes

print(var.values)   # underlying data
print(var.index)    # index labels
print(var.dtype)    # data type

# Creating Series from a dictionary
data = {'a': 100, 'b': 200, 'c': 300}
var = pd.Series(data)
print(var)

# can also apply arithmetic opearations
print(var + 10)     # add scalar
print(var * 2)      # multiply

s1 = pd.Series([1, 2, 3], index=['a','b','c'])
s2 = pd.Series([10, 20, 30], index=['a','b','c'])

print(s1 + s2)  # pandas align with idx

s = pd.Series([10, 20, None, 40])
print(s)

print(s.isnull())     # check missing values
print(s.notnull())    # opposite