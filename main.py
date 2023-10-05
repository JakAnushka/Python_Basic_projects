from menu import resources
from logo import name_tag
from logo import symbol


def sym():
    print(name_tag)
    print(symbol)


sym()


def payment():
    total = 0
    print("please pay first and then get our service 🪙")
    total += int(input("How many quarter:")) * 0.25
    total += int(input("How many Dime:")) * 0.1
    total += int(input("How many nickel:")) * 0.05
    total += int(input("How many penny:")) * 0.01
    if total <= 3 or total <= 1.5:
        print("money is not full.....refunded")
        return "No"
    else:
        return total


def check(choice):
    if choice == "latte":
        if resources["water"] < 200:
            print("Insufficient water")
            return False
        elif resources["milk"] < 150:
            print("Insufficient milk")
            return False
        elif resources["coffee"] < 24:
            print("Insufficient coffee")
            return False
        latte()
    elif choice == "espresso":
        if resources["water"] < 50:
            print("Insufficient water")
            return False
        elif resources["coffee"] < 18:
            print("Insufficient coffee")
            return False
        espresso()
    if choice == "cappuccino":
        if resources["water"] < 250:
            print("Insufficient water")
            return False
        elif resources["milk"] < 100:
            print("Insufficient milk")
            return False
        elif resources["coffee"] < 24:
            print("Insufficient coffee")
            return False
        cappuccino()


def report():
    print("REPORT:")
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "g")
    print("Money: $", resources["money"])



def espresso():
    total = payment()
    if total == "No":
        print("no service")
    else:
        print(f"You have paid {total}")
        print("Your espresso ☕ is here..ENJOY!")
        resources["money"] += total
        resources["water"] = int(resources["water"]) - 50
        resources["milk"] = int(resources["milk"]) - 0
        resources["coffee"] = int(resources["coffee"]) - 18


def latte():
    total = payment()
    if total == "No":
        print("no service")
    else:
        print(f"You have paid {total}")
        print("Your  latte ☕ is here..ENJOY!")
        resources["money"] += total
        resources["water"] = int(resources["water"]) - 200
        resources["milk"] = int(resources["milk"]) - 150
        resources["coffee"] = int(resources["coffee"]) - 24


def cappuccino():
    total = payment()
    if total == "No":
        print("no service")
    else:
        print(f"You have paid {total}")
        print("Your cappuccino ☕ is here..ENJOY!")
        resources["money"] += total
        resources["water"] = int(resources["water"]) - 250
        resources["milk"] = int(resources["milk"]) - 100
        resources["coffee"] = int(resources["coffee"]) - 24


want = True

while want:

    user_choice = input("What do you want to have?(espresso/latte/cappuccino/report)").lower()
    if user_choice == "report":
        report()
    check(user_choice)
    w = input("Wanna Try againr?(y/n)").lower()
    if w == "n":
        want = False
        print("Thank-You 😀")
        print("PLEASE VISIT US AGAIN")


