import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


while True:
 answer = input("What would you like?  ")
 if  answer == "latte" or answer == "cappuccino":
    coins = 0
    if(MENU[answer]["ingredients"]["water"] <= resources["water"]):
        if(MENU[answer]["ingredients"]["milk"] <= resources["milk"]):
            if(MENU[answer]["ingredients"]["coffee"] <= resources["coffee"]):

                print("Please insert your coins! ")
                quarters = 0.25
                dimes = 0.10
                nickles = 0.05
                pennies = 0.01
                q = input("How many quarters? ")
                d = input("How many dimes? ")
                n = input("How many nickles? ")
                p = input("How many pennies? ")
                coins = float(q) * quarters + float(d) * dimes + float(n) * nickles + float(p) * pennies
                cost = MENU[answer]["cost"]
                if coins == cost:
                    print("Here is your " + answer +" enjoy!")
                    resources["milk"] = resources["milk"] - MENU[answer]["ingredients"]["milk"]
                    resources["water"] = resources["water"] - MENU[answer]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU[answer]["ingredients"]["coffee"]
                    resources["money"] = resources["money"] + cost
                elif coins > cost:
                    print("Here is your change back " + "$"+(round(coins - cost , 2)).__str__())
                    print("Enjoy your "+ answer)
                    resources["milk"] = resources["milk"] - MENU[answer]["ingredients"]["milk"]
                    resources["water"] = resources["water"] - MENU[answer]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU[answer]["ingredients"]["coffee"]
                    resources["money"] = resources["money"] + cost
                elif coins<cost:
                    print("Sorry that is not enough money! Here is your refund")
                    break



            elif(MENU[answer]["ingredients"]["coffee"] > resources["coffee"]):
                print("Sorry there is not enough coffee")
        elif(MENU[answer]["ingredients"]["milk"] > resources["milk"]):
            print("Sorry there is not enough milk")
    elif(MENU[answer]["ingredients"]["water"] > resources["water"]):
        print("Sorry there is not enough water")
        break


 elif answer == "espresso":
    if (MENU[answer]["ingredients"]["water"] <= resources["water"]):
        if (MENU[answer]["ingredients"]["coffee"] <= resources["coffee"]):

            print("Please insert your coins! ")
            quarters = 0.25
            dimes = 0.10
            nickles = 0.05
            pennies = 0.01
            q = input("How many quarters? ")
            d = input("How many dimes? ")
            n = input("How many nickles? ")
            p = input("How many pennies? ")
            coins = float(q) * quarters + float(d) * dimes + float(n) * nickles + float(p) * pennies
            cost = MENU[answer]["cost"]
            if coins == cost:
                print("Here is your " + answer + " enjoy!")
                resources["water"] = resources["water"] - MENU[answer]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[answer]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + cost
            elif coins > cost:
                print("Here is your change back " + "$" +(round(coins - cost , 2)).__str__())
                print("Enjoy your " + answer)
                resources["water"] = resources["water"] - MENU[answer]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[answer]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + cost
            elif coins < cost:
                print("Sorry that is not enough money! Here is your refund")
            money = coins
        elif (MENU[answer]["ingredients"]["coffee"] > resources["coffee"]):
           print("Sorry there is not enough coffee")
           break
    elif (MENU[answer]["ingredients"]["water"] > resources["water"]):
           print("Sorry there is not enough water")


 elif answer == "off":
    break

 elif answer == "report":
    print("milk: "+ resources["milk"].__str__() +"ml"+"\n"+"water: " + resources["water"].__str__() +"ml" + "\n" + "coffee: " + resources["coffee"].__str__() +"gr"+ "\nMoney= $" + round(resources["money"]).__str__())


 # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
 # Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
 # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52