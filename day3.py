# for i in range(5):
#     print("Hello ",i)

# for i in range(1,5):
#     print("Hello ",i)

# for i in range(1,10,2):
#     print("Hello ",i)


# i = 1
# while i <= 5:
#     print("hello ",i)
#     i += 1

# while True:
#     print("This run forever")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i == 2:
#         continue
#     print(i)

# 🟢 1. Multiplication Table
# table = int(input("Enter number: "))
# for i in range(1,11):
#     print(table, " x ", i, " = ", table * i)


# 🟢 2. Password Retry System
def password_verifier(correct_password):
    password = input("Enter password: ")
    return password == correct_password


def main():
    attempt = 3
    while attempt > 0:
        is_correct = password_verifier("1234")
        if is_correct:
            print("Access granted")
            login = input("Do you want to login again? (Y/N): ")
            if login in ["Y", "y"]:
                attempt = 3
            else:
                break
        else:
            attempt -= 1
            if attempt == 0:
                print("Access denied!")
            elif attempt == 1:
                print("You have Last attempt!")
            else:
                print("Access denied! you have remaning ", attempt, " attempts")
        if attempt <= 0:
            print("Your account is temporory blocked you can try after 24 hours later.")
            break


main()


# 1. Verify even number
def is_even_number(num):
    if num % 2 == 0:
        return True


# 2. Sum of First N Numbers
def sum_of_numbers(num):
    total = 0
    string = ""
    for i in range(num):
        string.join([str(i), " +"])
        total = total + i
    return print(string, " = ", total)


# 3. Reverse Number
def reverse_number(num):
    # print(type(num))
    str_number = str(abs(int(num)))
    length = len(str_number)
    result = ""
    for i in range(length):
        result += str_number[length - (i + 1)]
    return result


# 4. Count Digits
def count_digit(num):
    return len(str(abs(int(num))))


user_input = input(
    "1.Verify even number \n 2.Sum of First N Numbers \n 3.Reverse Number \n 4.Count Digits\n"
)

match user_input:
    case "1":
        number = input("Enter number: ")
        if is_even_number(int(number)):
            print(number, " is even number")
        else:
            print(number, " is not even number")
    case "2":
        number = input("Enter number: ")
        sum_of_numbers(int(number))
    case "3":
        number = input("Enter number: ")
        print("Reverse number is ", reverse_number(number))
    case "4":
        number = input("Enter number: ")
        print("Number of count is ", count_digit(number))
