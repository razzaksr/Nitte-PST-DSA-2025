def analysis(arr):
    if len(arr) < 2:
        return -1
    else:
        current_buy = arr[0]
        current_sell = arr[1]
        max_profit = current_sell - current_buy
        for cost in arr[1:]:
            current_profit = cost - current_buy
            if current_profit>max_profit:
                max_profit = current_profit
                current_sell = cost
            if cost < current_buy:
                current_buy = cost
        return (current_sell-max_profit),current_sell

print(analysis([45, 12, 3, 10, 50]))
print(analysis([7, 1, 5, 3, 6, 4]))
print(analysis([90, 40, 20, 10, 4]))
print(analysis([-10, -5, -2, -1, 1]))