# Day 2 Practice

# calculator
operator = input("Enter operation (+, -, *, /): ")

if operator not in ["+", "-", "*", "/"]:
    print("Invalid operator!")
else:
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))

    if operator == "+":
        print("Sum =", number1 + number2)
    elif operator == "-":
        print("Sub =", number1 - number2)
    elif operator == "*":
        print("Mul =", number1 * number2)
    elif operator == "/":
        print("Div =", number1 / number2)

# voting
age = int(input("What is your age? "))
if age >= 18 and age <= 120:
    print("You can vote")
elif age <= 0:
    print("Invalid input")
else:
    print("You can not vote")
