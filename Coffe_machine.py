
Req_coffee = input("Please enter\n E for Expresso, L for latte and C for Cappuccino:\n")
# CM_off = input("Please enter ON and OFF operation of the coffee Machine")

# amount in CM
def Money_calculation():
    Quaters =int(input("please enter number of Quaters"))
    Dimes   =int(input("please enter number of Dimes"))
    Nickles =int(input("please enter number of Nickles"))
    Pennies =int(input("please enter number of Pennies"))
    Total_money = float((0.25*Quaters)+(0.1*Dimes)+(0.05*Nickles)+(0.01*Pennies))
    print(Total_money)

Money_calculation()

#Recipe{Type,water,coffee,milk,price}
Menu1 ={"E":{"water":"50","coffee":"18","milk":"0","price":"1.50"},
"L":{"water":"200","coffee":"24","milk":"150","price":"2.50"},
"C":{"water":"250","coffee":"24","milk":"100","price":"3.00"}}

def order(ELC):
    for key, value in Menu1.items():
        if key == ELC:
            print(key, ' : ',value)
order(Req_coffee)

# start with
CM_Fill ={"water": 300,"Milk": 200,"Coffee": 100}



