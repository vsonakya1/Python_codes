
# import Games

# Games.game()


def cal(money):
    Q = (money / 0.25)
    print(money)
    print(money / 0.25)
    print(int(money / 0.25))
    print(int(money / 0.25)*0.25)
    print(round((money-((int(money / 0.25))*0.25)),2))
    # print(round(money-(int(money / 0.25)*0.25)),2)
    # print(float(money / 0.25))
    # print(float(money-(Q*0.25)))
    # print(float((money-(Q*0.25))/0.10))

    # D = ((money-(Q*0.25))/0.10)
    # print(D)
    # N = ((money-((Q*0.25)+(D*0.10)))/0.05)
    # print(N)
    # print(((money-((Q*0.25)+(D*0.10)))/0.05))
    # P = ((money-((Q*0.25)+(D*0.10)+(N*0.05)))/0.01)
    # print(P)
    # print(str(int(Q))+" "+str(D)+" "+str(N)+" "+str(P))
cal(2.80)

