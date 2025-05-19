
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

# exercise


def is_palindrome(teststr):
    # Your code goes here.
    newstring = ""
    for letter in teststr:
        if letter.isalnum():
            print(letter.lower())
            newstring += letter.lower()

    print(f"{newstring} is new string")
    # reversedstring = "".join(reversed(newstring)) # original method I came up with
    # another option that could be done. This makes more sense to me
    reversedstring = newstring[::-1]
    print(f"{reversedstring} is reversed string")
    if reversedstring == newstring:
        return True
    return False


# test_word = "Madam, I'm Adam."
# test_word = "RACE CAR!"
# test_word = "Hello, world"
# test_word = "Radar?"
test_word = "A man, a plan, a canal Panama!"

result = is_palindrome(test_word)
