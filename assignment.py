#* Q1. Function Scope and Built-in Functions (2 Marks)
#* Write a function analyze_numbers() that accepts a list of numbers and displays
#* 1.Maximum value
#* 2.Minimum value
#* 3.Sum of all values
#* 4.Average value

def analyze_numbers(numbers):
    return max(numbers), min(numbers), sum(numbers), sum(numbers)/len(numbers)

no=[10, 20, 30, 40]
Maximum_value,Minimum_value, Sum_values, Average_value = analyze_numbers(no)
print(f"Maximum value: {Maximum_value}")
print(f"Minimum value: {Minimum_value}")
print(f"Sum of all values: {Sum_values}")
print(f"Average value: {Average_value}")

#* Q2. Lambda Function (2 Marks)
#* Create a lambda function to calculate the square of a number.
#* Accept a number from the user and display its square.

number=int(input("enter number: "))
square=lambda number: number**2
print(square(number))

#* Q3. Math and Random Module (2 Marks)
#* Write a program that:
#* •Generates a random number between 1 and 100.
#* •Finds its square root using the math module.

import random, math
number=random.randint(1,100)
print(number)
print(math.sqrt(number))

#* Q4. Employee Salary Calculator using Function Arguments (4 Marks)
#* Create a function:
#* calculate_salary(basic_salary, bonus=2000)
#* The function should calculate and display:
#* Total Salary = Basic Salary + Bonus
#* Demonstrate the use of:
#* • Positional Arguments
#* • Keyword Arguments
#* • Default Arguments

def calculate_salary(basic_salary, bonus=2000):
    return basic_salary + bonus

print("Employee 1 Salary: ",calculate_salary(52000,3000))
print(" Employee 3 Salary: ",calculate_salary(basic_salary=52000,bonus=3000))
print(" Employee 2 Salary: ",calculate_salary(52000))