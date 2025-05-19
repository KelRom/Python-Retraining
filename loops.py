x: int = 0

# while loop
while x < 5:
    print(x)
    x += 1

print("\n")
answer: str = input("Should I stop? ")
while answer.lower() != "yes":
    print(answer)
    answer: str = input("Should I stop? ")

# define a for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    print(day)

print("\n")
# using break and continue statements
for day in days:
    if day == "Wed":
        break
    print(day)

print("\n")
for day in days:
    if day == "Thu":
        continue  # skips the rest of code in the loop this iteration
    print(day)


# using enumerate to get an index and the item
for index, item in enumerate(days):
    print(f"Index is {index} and item is {item}")
