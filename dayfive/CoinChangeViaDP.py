# def dispense(denominations,required):
#     poss = [required+1]*(required+1)
#     poss[0] = 0
#     for currency in denominations:
#         for index in range(currency,len(poss)):
#             poss[index] = min(poss[index],poss[index-currency]+1)
#     return poss[required] if poss[required]<=required else -1

def dispense(coins,amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    
    for i in range(amount):
        if dp[i]==amount+1:
            continue
        for coin in coins:
            if i+coin<=amount:
                dp[i+coin] = min(dp[i]+1,dp[i+coin])
    return -1 if dp[amount]==amount+1 else dp[amount]

print(dispense([100,500,200],200))
print(dispense([100,500,200],1100))
print(dispense([100,500,200],8700))
print(dispense([100,500,200],1950))
print(dispense([500,300],1100))