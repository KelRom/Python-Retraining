# Sequences: Lists and Tuples

mylist: list = [0, 1, "two", 3.2, False]
print(len(mylist))

# to access a member of a sequence type, use []
print(mylist[2])
print(mylist[-1])
mylist[0] = 10
print(mylist)

# add a list to another list
another_list: list = [6, 7, 8]
mylist = mylist + another_list
print(mylist)

# strings are immutable
mystr: str = "This is a string"
print(mystr[2])  # this will print i

# use slices to get parts of a sequence
print(mylist[1:4])  # start value: end value : step value

# gives the same values but in reverse
print(mylist[3:0:-1])  # start value: end value : step value

# can use slices to reverse a sequence
print(mylist[::-1])

# tuples are like list but immutable
mytuple: tuple = (0, 1, 2, "three")
# mytuple: tuple[int, int, int, str] = (0, 1, 2, "three") # I could do this to be very explicit like in rust but the top line looks better and matches the programming language
print(mytuple[2])
# mytuple[2] = 3 sets are immutable so this will cause an error

# Sets contain unique values
myset: set = {1, 2, 3, 2, 1, "hello there"}
print(myset)
# myset[3] = 4 does not work because sets are unordered with no index

# test for membership
print(1 in mylist)  # use in operator to see if value is in a sequence/collection
print(3 in mytuple)
print(5 in myset)
