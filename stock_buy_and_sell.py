def stock_buy_and_sell(arr):
    min_price = arr[0]
    max_profit = 0
    for x in arr:
        if x<min_price:
            min_price = x
    for x in arr:
        if x-min_price>max_profit:
            max_profit = x-min_price
    return max_profit

arr = [7,1,5,3,6,4]
print(stock_buy_and_sell(arr))
