#Welcome Screen
import sys
import pyfiglet
#Asks the user to if ready to start (loop)
print(pyfiglet.figlet_format("Welcome to the calculator! ", justify="center"))
start=input("Would you like to start now? Y/N: ")
while start.upper() == "Y":
    #Asks the user what operation to be used
    operation_list=["A", "S", "M", "D"]
    while True:
        operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division: ")
        operation=operation.upper()
        if operation in operation_list:
            break
        else:
            print("Invalid operation!")
    #Asks user the two different numbers to do an operation with
    while True:
        try:
            first_operand=float(input("Please input your first operand:"))
            break
        except ValueError:
            print("The value you entered is not a number, please try again.")
    while True:
        try:
            second_operand=float(input("Input your second operand:"))
            break
        except ValueError:
            print("The value you entered is not a number. Please try again.")
    #Does the chosen operation
    if "A" in operation:
        result=first_operand+second_operand
        print(result)
    if "M" in operation:
        result=first_operand*second_operand
        print(result)
    if "S" in operation:
        result=first_operand-second_operand
        print(result)
    if "D" in operation:
        while True:
            try:
                result=first_operand/second_operand
                break
            except ZeroDivisionError:
                print("We cannot divide by zero. Please try again.")
                second_operand=float(input("Please input a valid second operand:"))
        print(result)
        #If division, asks the user if they want to see the whole number only or the remainder only
        division_choices_list=["M", "NR"]
        while True:
            division_choices=input("To know the remainder of your equation, type M. If you want to know the result without any remainder, type NR.")
            division_choices=division_choices.upper()
            if division_choices in division_choices_list:
                break
            else:
                print("Invalid answer! Please try again.")
        if "M" in division_choices:
            result=first_operand%second_operand
            print(result)
        if "NR" in division_choices:
            result=first_operand//second_operand
            print(result)
    #Asks if user wants to perform another operation
    start=input("Would you like to perform more calculations?Y/N")
else:
    sys.exit()
