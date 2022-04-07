    


order_coffee = input("What would you like: \n E for Expresso, L for latte and C for Cappuccino:\n")

def order(a):
    if a =="E":
        return("Expresso")
    elif a =="L":
        return("latte")
    elif a =="C":
        return("Cappuccino")

def cost():
    if order(order_coffee) =="Expresso":
        return("1.50")
    elif order(order_coffee) =="latte":
        return("2.50")
    elif order(order_coffee) =="Cappuccino":
        return("3.00")

print(f"You ordered {order(order_coffee)} and it cost $ "+ cost())

Custmer_give = float(input("Here you go: \n"))
def cal(money):
    Q = int(money / 0.25)
    D = int((money-(Q*0.25))/0.10)
    N = int((money-((Q*0.25)+(D*0.10)))/0.05)
    P = int(round(((money-((Q*0.25)+(D*0.10)+(N*0.10)))/0.01),2))
    print("Quaters:"+str(Q)+" and Dimes: "+str(D)+" and Nickels: "+str(N)+" and Pennies: "+str(P))

def money():
    
    if float(cost()) <= Custmer_give:
        print("return $"+str(round(Custmer_give -float(cost()),2)))
        a=Custmer_give -float(cost())
        cal(a)
    else:
        print("Ask for $"+str(round(Custmer_give -float(cost()),2)))
        cal(a)
money()


#cal(Custmer_give)





# #Recipe{Type,water,coffee,milk,price}
# Menu1 ={"E":{"water":"50","coffee":"18","milk":"0","price":"1.50"},
# "L":{"water":"200","coffee":"24","milk":"150","price":"2.50"},
# "C":{"water":"250","coffee":"24","milk":"100","price":"3.00"}}

# def order(ELC):
#     for key, value in Menu1.items():
#         if key == ELC:
#             print(key, ' : ',value)
# order(Req_coffee)
# print(order(Req_coffee))

# # start with
# CM_Fill ={"water": 300,"Milk": 200,"Coffee": 100}

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


