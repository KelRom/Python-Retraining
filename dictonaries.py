# Dictionary: a key value pair data structure, just like maps with c++ or hashmaps in rust
# Keys have to be immutable data types
# must be unique
mydict: dict = {
    "one": 1,
    "two": 2,
    3: "three",
    4.5: ["four", "point", "five"]
}

print(mydict)

# dictionaries are accessed with keys
print(mydict["one"])
print(mydict[3])

# set dictionary data by creating a new key
mydict["seven"] = 7
print(mydict)

# access a nonexistent key will cause error
# print(mydict["kelvin"])

# avoid by using the in operator/keyword
print("kelvin" in mydict)
print("two" in mydict)

# retrieve all keys and values of a dictionary
print(mydict.keys())
print(mydict.values())

# iterate over all items in a dictionary
for key, value in mydict.items():
    print(f"Key: {key}, value: {value}")
