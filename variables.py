myint: int = 10
myfloat: float = 13.2576
mystr: str = "This is a string"
mybool: bool = True

print(myint)
print(mystr)

print(myint + myfloat)
print(myint * myfloat)
print(myint / myfloat)
print(myint % 3) 

another_str: str = "This is another string"
print(mystr + another_str)
print("nom " * 3)

# Logical and comparison operator
print(myint == 10)
print(myfloat != 20)
print(myint > 20)
print(myfloat < 10)

print(myint > 5 and myfloat < 25.0)
print(myint < 5 or myfloat < 25.0)
print(not (myint < 5 or myfloat < 25.0))

