import os
# MENU consist of fixed amount of resources required for each type of coffee. It also contain cost of each coffee.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 250,
            "coffee": 15,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 200,
            "coffee": 8,
        },
        "cost": 35,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 250,
            "coffee": 15,
        },
        "cost": 50,
    }
}

resources = {
    "water": 800,
    "milk": 700,
    "coffee": 100,
}


def resource_checking(coffee):
    """Check weather resources are sufficient to make coffee."""
    if coffee == "espresso":
        if resources["water"]<MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is no enough water.")
            return 0
        elif resources["coffee"]<MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is no enough coffee.")
            return 0

    elif coffee == "latte":
        if resources["water"]<MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is no enough water.")
            return 0
        elif resources["milk"]<MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is no enough milk.")
            return 0
        elif resources["coffee"]<MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is no enough coffee.")
            return 0

    elif coffee == "cappuccino":
        if resources["water"]<MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is no enough water.")
            return 0
        elif resources["milk"]<MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is no enough milk.")
            return 0
        elif resources["coffee"]<MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is no enough coffee.")
            return 0

def money_checking(coffee,total):
    """Checks weather money given by customer is sufficient for order."""
    if coffee == "espresso":
        if total<MENU["espresso"]["cost"]:
            return -1
        else:
            remaining_money = total - MENU["espresso"]["cost"]
            print(f"Here is Rs. {remaining_money} in change.")
            return MENU["espresso"]["cost"]

    elif coffee == "latte":
        if total<MENU["latte"]["cost"]:
            return -1
        else:
            remaining_money = total - MENU["latte"]["cost"]
            print(f"Here is Rs. {remaining_money} in change.")
            return MENU["latte"]["cost"]
    elif coffee == "cappuccino":
        if total<MENU["cappuccino"]["cost"]:
            return -1
        else:
            remaining_money = total - MENU["cappuccino"]["cost"]
            print(f"Here is Rs. {remaining_money} in change.")
            return MENU["cappuccino"]["cost"]

def resource_management(coffee):
    """Manages resources for order prepration."""
    if coffee == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif coffee == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif coffee == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]


total_money = 0
closing = True
while closing:
    need_coffee = input("Do you want to drink coffee? yes or no: ").lower()
    if (need_coffee == "yes"):
        os.system('cls')
    else:
        closing = False
        print(f"Today's earnings: Rs. {total_money}")
        continue
    # Printing menu.
    print('''MENU
    Espresso = Rs. 20
    Latte = Rs. 35
    Cappuccino = Rs. 50''')
    coffee_type = input("What will you like? (espresso/latte/cappuccino): ").lower()
# TODO1 : CHECKING RESOURCES
    # Checking for resources present in machine
    if coffee_type == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: Rs. {total_money}")
        continue

    # Checking if there is enough resources for making espresso
    elif coffee_type == "espresso":
        check1 = resource_checking("espresso")
        if check1 == 0:
            continue

    # Checking if there is enough resources for making latte.
    elif coffee_type == "latte":
        check1 = resource_checking("latte")
        if check1 == 0:
            continue

    # Checking if there is enough resources for making cappuccino.
    elif coffee_type == "cappuccino":
        check1 = resource_checking("cappuccino")
        if check1 ==0:
            continue

    # Closing coffee machine
    elif coffee_type == "off":
        closing = False
        print(f"Today's earnings: Rs. {total_money}")
        continue

    else:
        print("Wrong Input.")
        continue

# TODO2 : PAYMENT GATHERING
    print("Please insert coins.")
    # Taking money from user in form of coins.
    ten_rupee = int(input("10 rupee coins?: "))
    five_rupee = int(input("5 rupee coins?: "))
    two_rupee = int(input("2 rupee coins?: "))
    one_rupee = int(input("1 rupee coins?: "))
    grand_total = one_rupee+(two_rupee*2)+(five_rupee*5)+(ten_rupee*10)

    # Checking if the given money is sufficient.
    money = money_checking(coffee_type,grand_total)
    if money == -1:
        print("Sorry, that's not enough money.Money refunded.")
        continue
    print(f"Here is your {coffee_type} ☕. Enjoy!")

# TODO3 : MANAGING RESOURCES
    total_money +=money
    resource_management(coffee_type)