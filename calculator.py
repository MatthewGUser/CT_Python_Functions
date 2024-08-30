# [ Task 1 ]

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed." # <== [ Task 3 ] 
    return num1 / num2

# [ Task 2 ]

opp = input("add, subtract, multiply, or divide? ")

loop = True
while loop:
    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        
        if opp == "add":
            print(f"The result is: {add(num1, num2)}")
        elif opp == "subtract":
            print(f"The result is: {subtract(num1, num2)}")
        elif opp == "multiply":
            print(f"The result is: {multiply(num1, num2)}")
        elif opp == "divide":
            print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation.")
        
        loop = False

    # Catch issue
    except ValueError:
        print("Error: Please enter valid numbers.")
