
# will cause an error
# x = 10 / 0

# Better
try:
    x = 10 / 0
except:
    print("Well that didn't work")

try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero ")
except ValueError as e:
    print(f"You didn't give me a valid number {e}")
finally:
    print("Finally always runs")
