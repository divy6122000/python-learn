def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def verify_is_valid_number_array(arr):
    valid = True
    for i in arr:
        is_valid = is_valid_number(i)
        if not is_valid:
            valid = False
            break
    return valid


def user_input():
    num1 = input("Enter Number 1: ")
    is_valid = is_valid_number(num1)
    if not is_valid:
        print("Invalid number")
        return [False, False]
    num2 = input("Enter Number 2: ")
    is_valid = is_valid_number(num2)
    if not is_valid:
        print("Invalid number")
        return [False, False]
    return [int(num1), int(num2)]


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculate_average(total, number_of_subjects):
    return total / number_of_subjects


def sum_of_array(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total


def get_grade(avg):
    if avg > 95:
        return "A+"
    elif avg > 85:
        return "A"
    elif avg > 80:
        return "B+"
    elif avg > 75:
        return "B"
    elif avg > 60:
        return "C"
    elif avg > 40:
        return "D"
    else:
        return "Failed"


# 🟢 1. Calculator Using Functions
# def main():
#     user_val = input(
#         "1.Add \n 2.subtract \n 3.multiply \n 4.divide \n Choose any option: "
#     )
#     [num1, num2] = user_input()
#     if not num1:
#         return
#     if not num2:
#         return
#     match user_val:
#         case "1":
#             print(num1, "+", num2, "=", add(num1, num2))
#         case "2":
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         case "3":
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         case "4":
#             print(num1, "/", num2, "=", divide(num1, num2))

# 🟢 2. Student Grade System
# def main():
#     number_of_subjects = input("How many subjects? :")
#     is_valid = is_valid_number(number_of_subjects)
#     if not is_valid:
#         False
#     number_of_subjects = int(number_of_subjects)
#     marks_arr = []
#     for i in range(number_of_subjects):
#         print("Enter marks of subject ", i + 1)
#         mark = input(": ")
#         marks_arr.append(mark)
#     if not verify_is_valid_number_array(marks_arr):
#         return False
#     avg = calculate_average(sum_of_array(marks_arr), number_of_subjects)
#     print("Average is ", avg)
#     print("Grade is ", get_grade(avg))


# 🟢 3. Bank System
def deposit(amount, balance):
    balance += float(amount)
    return balance


def withdraw(amount, balance):
    balance -= float(amount)
    return balance


def check_balance(balance):
    return float(balance)


def add_transaction(type, amount, transaction):
    transaction.append({"type": type, "amount": amount})
    return transaction


def get_transactions(transactions, check_balance):
    print("Amount(₹)", "\t", "\t")
    for transaction in transactions:
        if transaction["type"] == "DEBIT":
            print("₹", transaction["amount"], "\t", transaction["type"])
        elif transaction["type"] == "CREDIT":
            print("₹", transaction["amount"], "\t\t", transaction["type"])
    print("\nAvailable balance: ", check_balance)


# 🧪 PRACTICE TASKS functions
def find_largest_number(arr):
    max = 0
    for num in arr:
        if max < num:
            max = num
    return max


# Function to check palindrome
def verify_palindrome(str):
    reverse_str = str[::-1]
    if str == reverse_str:
        return "Palindrome"
    else:
        return "Not Palindrome"


# Factorial Function
def factorial(factorial):
    fact = 1
    for f in range(factorial - 1):
        fact += (f + 1) * fact
    return fact


def is_even(num):
    return num % 2


# Prime | composite | Neither
def verify_prime_number(num):
    if num == 0:
        return "Neither"
    elif num == 1:
        return "Neither"
    # f(n)=(nn!mod(n+1)​)(n−1)+2

    # step:1
    val1 = num + 1
    # if it is even number so it's composite
    if is_even(val1):
        return "composite"

    # Find factorial
    fact = factorial(num)
    rem = fact % val1

    div = rem / num
    mul = div * (num - 1)
    add = mul + 2

    if add == 2:
        return "composite"
    else:
        return "prime"


# def main():
#     balance = 0
#     transactions = []
#     DEBIT = "DEBIT"
#     CREDIT = "CREDIT"

#     print("1.Deposite\n2.Withdraw\n3.Check Balance\n4.Transactions List\n5.Exit")
#     while True:
#         user_input = input("Choose option: ")
#         match user_input:
#             case "1":
#                 amount = input("Enter Deposite amount: ")
#                 valid = is_valid_number(amount)
#                 if not valid:
#                     print("Invalid deposite amount!")
#                     continue
#                 balance = deposit(amount, balance)
#                 add_transaction(CREDIT, amount, transactions)
#                 print(
#                     "₹",
#                     amount,
#                     " is successfully deposite\nYour current balance is ₹",
#                     check_balance(balance),
#                 )
#             case "2":
#                 amount = input("Enter Withdraw amount: ")
#                 valid = is_valid_number(amount)
#                 if not valid:
#                     print("Invalid withdraw amount!")
#                     continue
#                 if balance < float(amount):
#                     print("You don't have a suficent balance")
#                     continue
#                 balance = withdraw(amount, balance)
#                 add_transaction(DEBIT, amount, transactions)
#                 print(
#                     "₹",
#                     amount,
#                     " is successfully Withdraw\nYour current balance is ₹",
#                     check_balance(balance),
#                 )
#             case "3":
#                 print("Your available balance: ₹", check_balance(balance))
#             case "5":
#                 print("Good bye! Thanks for using our service")
#                 break
#             case "4":
#                 get_transactions(transactions, check_balance(balance))

#             case _:
#                 print("Please choose only 1 to 5 only")


# 🧪 PRACTICE TASKS
# 🔹 1. Function to find largest numbers
def main():
    print("1. largest number\n 2.pallindrom\n3.factorial\n4.prime number")
    user_input = input("Choose option: ")
    match user_input:
        case "1":
            numbers_arr = []
            for i in range(5):
                num = input("Enter number: ")
                valid = is_valid_number(num)
                if not valid:
                    print("Invalid number!")
                numbers_arr.append(float(num))
            largest = find_largest_number(numbers_arr)
            print("Largest number is ", largest)
        case "2":
            user_str = input("Enter value of checking pallindrom: ")
            print(f"{user_str} is ", verify_palindrome(user_str))
        case "3":
            fact_number = int(input("Enter factorial: "))
            print("Factorial is ", factorial(fact_number))
        case "4":
            num = int(input("Enter number for checking prime: "))
            print(verify_prime_number(num))
        case _:
            print("Please choose only 1 to 4 only")


main()


# ❓ QUICK TEST
# Difference between print and return?
# -> print has no return any value and use of print is display values and return is used for return a value after return scope function not executed.
# What is parameter?
# -> pass a variable to the function is called parameter.
# What is scope?
# -> we can not access a variable out side the function if declere a in that scope.
# Why functions are important?
# -> Because it's provide a reuable functonality so we can use multiple times.
