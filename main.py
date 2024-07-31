# Calculator to perform Calculations like Addition, Subtraction, Multiplication, Division, Square, Cube, Square Root and Cube Root

import math # Importing math module to calculate square root and cube root
import time # Importing time to delay the program exit


def add(): # Function for sum
    num1 = int(input("\nEnter the 1st number to add: "))
    num2 = int(input("Enter the 2nd number to add: "))
    sum = num1 + num2
    print(f"\n{num1} + {num2} = {sum}")

def sub(): # Function for subtraction
    num1 = int(input("\nEnter the 1st number to subtract: "))
    num2 = int(input("Enter the 2nd number to subtract: "))
    difference = num1 - num2
    print(f"\n{num1} - {num2} = {difference}")

def multi(): # Function to mutiply
    num1 = int(input("\nEnter the 1st number to multiply: "))
    num2 = int(input("Enter the 2nd number to multiply: "))
    product = num1 * num2
    print(f"\n{num1} x {num2} = {product}")

def div(): # Function to divide
    num1 = int(input("\nEnter the 1st number to divide: "))
    num2 = int(input("Enter the 2nd number to divide: "))
    quotient = num1 / num2
    print(f"\n{num1} ÷ {num2} = {quotient}")

def square(): # Function to calculate square
    num = int(input("\nEnter a number to calculate its square: "))
    sq = (num ** 2)
    print(f"\n{num}² = {sq}")

def cube(): # Function to calculate cube
    num = int(input("\nEnter a number to calculate its cube: "))
    c = (num ** 3)
    print(f"\n{num}³ = {c}")

def sqare_root(): # Function to calculate square root
    num = int(input("\nEnter a number to calculate its Square Root: "))
    sqrt = math.sqrt(num)
    print(f"\n√ {num} = {sqrt}")

def cube_root(): # Function to calculate square root
    num = int(input("\nEnter a number to calculate its Cube Root: "))
    c_rt = math.cbrt(num)
    print(f"\n∛ {num} = {c_rt}")


while True:
    # Creating Program's Main Menu
    print("\n---------------------------------------------------------------------")
    print("|             *** Calculator (Created in Python) ***                |")
    print("---------------------------------------------------------------------")
    print("  * This Program will Perform any of the following Calculations *    ")
    print("---------------------------------------------------------------------")
    choice = int(input("\nPress 1 - Sum\nPress 2 - Subtraction\nPress 3 - Multiplication\nPress 4 - Division\nPress 5 - Square\nPress 6 - Cube\nPress 7 - Square Root\nPress 8 - Cube Root\nPress 9 - Quit/Exit\n\nSelect an option: "))

    # Creating Condition

    if choice<1 or choice>9:
        print("\nInvalid choice, Select number between 1 and 5\n")
    elif choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        multi()
    elif choice == 4:
        div()
    elif choice == 5:
        square()
    elif choice == 6:
        cube()
    elif choice == 7:
        sqare_root()
    elif choice == 8:
        cube_root()
    elif choice == 9:
        print("\nExiting the Program.....\n")
        time.sleep(2) # Delaying the loop break for 5 seconds
        break