import random as r
from math import pi
import math
from tabulate import tabulate

print("The square root of 16 is", math.sqrt(16))

# importing a specific module
print(f"Pi is {pi}")

# importing a module and giving it a different name
print(r.randint(100, 200))

# using tabulate to print tabulate data

# sample data
data = [
    ["Product", "Price", "Stock"],
    ["Laptop", 999.99, 45],
    ["Mouse", 24.99, 128],
    ["Keyboard", 59.99, 89]
]

# Creating a formatted table
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
