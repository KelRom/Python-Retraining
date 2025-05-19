

def hello_function() -> None:
    print("hello world")
    name: str = input("What is your name? ")
    print(f"Nice to meet you {name}")


hello_function()


def hello_function2(greeting: str) -> None:
    print("hello world")
    name: str = input("What is your name? ")
    print(greeting, name)


hello_function2("How are you doing")
hello_function2("Hey what's up")


def cube(x: int) -> int:
    return x * x * x


result = cube(3)
print(result)

# functions with default values


def hello_function3(greeting: str, name=None) -> None:
    print("hello world")
    if name == None:
        name = input("What is your name? ")
    print(greeting, name)


hello_function3("Good evening", "Kelvin")

# function with variable number of parameter
# *variable_name will be the last parameter


def multi_add(start, *numbers):
    result = start
    for number in numbers:
        result += number
    return result


print(multi_add(4, 5, 10, 4, 1000))
