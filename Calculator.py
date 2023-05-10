#Welcome Screen
#Asks the user to if ready to start (loop)
start=input("Welcome to the calculator! Would you like to start now? Y/N")
while start.upper() == "Y":
    #Asks the user what operation to be used
    operation=["A", "S", "M", "D"]
    while True:
        operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division.")
        if operation.upper()==operation:
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
        #If division, asks the user if they want to see the whole number only or the remainder only