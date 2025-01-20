Menu = {
    "Latte": {
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":150
    },
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}
profit=0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients: #water #milk #coffee
         if order_ingredients[item] > resources[item]:
              print(f"Not enough resources {item}")
              return False
    return True

def process_coins():
     print("Please Enter Coins.")
     total=0
     coins_five = int(input("How many 5rs coins?: "))
     coins_ten = int(input("How many 10rs coins?: "))
     coins_twenty = int(input("How many 20rs coins?: "))
     total = coins_five*5 + coins_ten*10 + coins_twenty*20
     return total

def is_payment_successful(money_recieved, coffee_cost):
    if money_recieved >= coffee_cost:
       global profit
       profit += coffee_cost
       change = money_recieved-coffee_cost
       print(f"Here is your Rs.{change} in change.")
       return True
    else:
        print("Sorry you did not pay enough. Refunded!")
        return False
    
def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name} ... Enjoy!!")
is_on=True
while is_on:
    choice=input("What would you like to have? (Latte/Espresso/Cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs{profit}")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])