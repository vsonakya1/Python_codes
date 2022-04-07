    

# start with


order_coffee = input("What would you like: \n E for Expresso, L for latte and C for Cappuccino:\n")

def order(a):
    if a =="E":
        return ["EXPRESSO","1.50"]
    elif a =="L":
        return ["LATTE","2.50"]
    elif a =="C":
        return ["CAPPUCCINO","3.00"]

orders = order(order_coffee)[0]
cost  = order(order_coffee)[1]

print(f"You ordered {orders} and it cost $ "+ cost)

Custmer_give = float(input("Here you go: \n"))

def cal(money):
    Q = int(money / 0.25)
    D = int((money-(Q*0.25))/0.10)
    N = int((money-((Q*0.25)+(D*0.10)))/0.05)
    P = int(round(((money-((Q*0.25)+(D*0.10)+(N*0.10)))/0.01),2))
    print("Quaters:"+str(Q)+" and Dimes: "+str(D)+" and Nickels: "+str(N)+" and Pennies: "+str(P))

def money():
    
    if float(cost) <= Custmer_give:
        print("return $"+str(round(Custmer_give -float(cost),2)))
        a=Custmer_give -float(cost)
        cal(a)
    else:
        print("Ask for $"+str(round(Custmer_give -float(cost),2)))
        cal(a)
money()

#Recipe{Type,water,coffee,milk,price}
Menu1 ={"EXPRESSO":{"Water":50,"Coffee":18,"Milk":0,"price":1.50},
"LATTE":{"Water":200,"Coffee":24,"Milk":150,"price":2.50},
"CAPPUCCINO":{"Water":250,"Coffee":24,"Milk":100,"price":3.00}}

CM_Fill ={"Water": 300,"Coffee": 100,"Milk": 200}

# def report():
#     for key, value in Menu1.items():
#         if key == orders:
#             x=value
#             x.update({"Water":(CM_Fill.get("Water")-50),"Coffee":(CM_Fill.get("Coffee")-18),"Milk":(CM_Fill.get("Milk")-0)})
#     for key1, value1 in x.items():
#         print(key1,":",value1)

# report()

def report():
    for key, value in Menu1.items():
        if key == orders:
            x=value
            x.update({"Water":(CM_Fill.get("Water")-x.get("Water"))
                    ,"Coffee":(CM_Fill.get("Coffee")-x.get("Coffee"))
                    ,"Milk":(CM_Fill.get("Milk")-x.get("Milk"))})
            [print(key,":",value) for key, value in x.items()]
report()











# def Make_coffee(order):
#     print("Turn On the Machine")


# # amount in CM
# def Money_calculation():
#     Quaters =int(input("please enter number of Quaters"))
#     Dimes   =int(input("please enter number of Dimes"))
#     Nickles =int(input("please enter number of Nickles"))
#     Pennies =int(input("please enter number of Pennies"))
#     Total_money = round(float((0.25*Quaters)+(0.1*Dimes)+(0.05*Nickles)+(0.01*Pennies)),2)
#     print(Total_money)

# Money_calculation()


