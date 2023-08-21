# Simple Calculator using functions
# For Basic arithmetic operations like addition,subtraction,multiplication and division
calci_art = ''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''


def add(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


def multi(a, b):
    result = a * b
    return result


def div(a, b):
    result = a / b
    return result


def calculator():
    calculate = True
    while calculate:
        print(calci_art)
        L = ["Addition(+)", "Subtraction(-)", "Multiplication(*)", "Division(/)"]
        for i in L:
            print(i, "\n")
        choice = input("Enter Your Choice:")
        print("\n")
        if choice.lower() == "addition" or choice == "+":
            x = float(input("Enter Number:"))
            y = float(input("Enter Number: "))
            s = add(x, y)
            print(f"Addition of {x} and {y} is {s} \n")
        elif choice.lower == "subtraction" or choice == "-":
            x = float(input("Enter Number:"))
            y = float(input("Enter Number:"))
            s = sub(x, y)
            print(f"subtraction of {x} and {y} is {s} \n")
        elif choice.lower == "division" or choice == "/":
            x = float(input("Enter Number:"))
            y = float(input("Enter Number:"))
            s = div(x, y)
            print(f"Division of {x} and {y} is {s}")
        elif choice.lower == "multiplication" or choice == "*":
            x = float(input("Enter Number:"))
            y = float(input("Enter Number:"))
            s = multi(x, y)
            print(f"Multiplication of {x} and {y} is {s} \n")
        else:
            print("please choose which operation you want to perform!\n")

        user_choice = input("Want to do more calculations? (YES/NO)").lower()
        if user_choice == "yes":
            calculate = True

        else:
            calculate = False
            print("Thankyou for using ME:)\n")


calculator()
