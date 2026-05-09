# Day 1
# This is comment
import pandas

print("Hello \rworld!")

# Practice
# 1 print name
name = input("Whats your name?")
print("Welcome ", name, " to AI world")

# 2 sum /avg
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
print("The sum of two number is ", number1 + number2)
print("The average is ", (number1 + number2) / 2)

# 3 Celsius → Fahrenheit
celsius = float(input("Enter celsius: "))
fahrenheit = celsius * (9 / 5) + 32
print("The fahrenheit of ", celsius, "celsius is ", fahrenheit)

"""
What is a variable?
-> Variable is a just like container it used for to store a data for example a = 5 so value of a is 5 
Difference between int and float?
-> these both are datatype interger store a positive and nagative value and float is store a decimal value for example a = 5 so 5 is int datatype and b = 5.6 so it is a decimal value 
What does input() return?
-> input is take a value form user it is ask a value for user when user give a value so it is assign to variable.
Why do we use int()?
->it used for conver datatype to integer like a = "5" so if we use int(a) so it's return integer value 
"""
