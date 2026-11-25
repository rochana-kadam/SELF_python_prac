# Write a program containing an outer function calculate() and an inner function addition().
# - The outer function should accept two numbers.
# - The inner function should calculate their sum.
# - Call the inner function from the outer function.

def calculate():
    n1=int(input("enter n1: "))
    n2=int(input("enter n2: "))
    def cal_sum(a,b):
        return a+b

    result=cal_sum(n1,n2)
    print(result)

calculate()