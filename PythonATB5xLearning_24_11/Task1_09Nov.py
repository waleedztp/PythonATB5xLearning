#Print quotient and remainder of two numbers
from math import remainder

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

quotient_res = int(num1/num2)
remainder_res = num1%num2

print(quotient_res)
print(remainder_res)