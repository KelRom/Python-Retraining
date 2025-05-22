import os
from os import path
import time
from datetime import datetime

# printing the name of the operating system we are currently using
print(os.name)

# check for item existence and type
print("Item exists: ", path.exists("textfile.txt"))
print("Item is a file: ", path.isfile("textfile.txt"))
print("Item is a directory: ", path.isdir("textfile.txt"))


# working with file paths
print("Items path is: ", path.realpath("textfile.txt"))
print("Items path and name: ", path.split(path.realpath("textfile.txt")))

# get the modification
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))

# calculate how long ago the etime was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"It has been {td} since the file was last modified")
print(f"Or, {td.total_seconds()} seconds")
