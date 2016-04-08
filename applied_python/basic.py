import datetime

day_today = datetime.date.today().strftime("%A")
print "Today is {day}".format(day=day_today)

if day_today is "Friday":
    print "Today is Friday!!"
else:
    print "Today is {day}".format(day=day_today)

# ------------------------
# multiply each number by 2

numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print number ** 2

# ------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = range(1, 11)

for number in numbers:
    if number % 2 == 0:
        print "Number {} is even".format(number)
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)

# ----------------------
# List comprehension

even_numbers = [number for number in range(1,11) if number % 2 == 0]
odd_numbers = [number for number in range(1,11) if number % 2 == 1]
print "Even numbers: ", even_numbers
print "Odd numbers:", odd_numbers

# -- sets 

numbers = range(1, 30)
even_numbers = [number for number in range(1,11) if number % 2 == 0]

even_numbers = set(even_numbers)
numbers = set(numbers)

# difference (-) -> new set with elements in numbers but not in even_numbers
# so we can get odd_numbers

odd_numbers = list(numbers - even_numbers)
print "Odd numbers: ", odd_numbers


# ----------------------

while True:
    number = input("Please provide number: ")
    if number % 2 == 0:
        print "Number {} is even".format(number)
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)
    break

def is_number_even(number):
    if number % 2 == 0:
        print "Number {} is even".format(number)
        return True
    elif number % 2 == 1:
        print "Number {} is odd".format(number)
    else:
        print "is it number: {}?".format(number)
    return False


while True:
    number = input("Please provide number: ")
    is_number_even(number)
    break


while True:
    number = input("Please provide number: ")
    try:
        number = int(number)
    except ValueError as exc:
        print "Do we have number or not?"
        break
    is_number_even(number)
    break

# ---------------
# very simple calc

def add_numbers(n1, n2):
    return n1 + n2

def multiply_numbers(n1, n2):
    return n1 * n2

def subtract_numbers(n1, n2):
    return n1 - n2

def divide_numbers(n1, n2):
    return n1 / n2

actions = {
        'add': add_numbers,
        'multiply': multiply_numbers,
        'subtract': subtract_numbers,
        'divide': divide_numbers,
}

action = raw_input("Choose one action [add|multiply|subtract|divide|]:")
number1 = raw_input("Provide first number: ")
number2 = raw_input("Provide second number: ")

# convert to int
number1 = int(number1)
number2 = int(number2)

print "You will {action} two numbers {number1} and {number2}".format(**locals())
result = actions[action](number1, number2)
print "Result is: ", result

# ----------------------------

class SimpleCalc(object):
    def __init__(self, number1, number2):
        self.n1 = number1
        self.n2 = number2

    def add(self):
        return self.n1 + self.n2

    def multiply(self):
        return self.n1 * self.n2

    def subtract(selt):
        return self.n1 - self.n2

    def divide(self):
        return self.n1 / self.n2

simple_calc = SimpleCalc(number1, number2)
action = getattr(simple_calc, action)
result = action()
print result
