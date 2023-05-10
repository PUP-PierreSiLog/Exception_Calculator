#Welcome Screen
#Asks the user to if ready to start (loop)
start=input("Welcome to the calculator! Would you like to start now? Y/N")
while start.upper() == "Y":
    #Asks the user what operation to be used
    operation=input("Please input an operation to use. Type the letters indicated for each operation: A for Addition, M for multiplication, S for subtraction, D for division.")
    #Asks user the two different numbers to do an operation with
    first_operand=float(input("Input your first operand:"))
    second_operand=float(input("Input your second operand:"))
    #If division, asks the user if they want to see the whole number only or the remainder only