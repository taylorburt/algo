def main():
    print("test")
    purchase = 100
    cost = 5

def num_coins(cents, coins):
    if cents < 1:
        return 0
    # coins = [25, 10, 5, 1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += int(cents / coin)
        cents = cents % coin
        if cents == 0:
            break
    return num_of_coins

# 1 quarter 1 nickle 1 penny
# print(num_coins(31))

def min_coins(cents):
    coins = [25, 10, 1]
    winning_total = cents + 1
    while True:
        if len(coins) > 1:
            temp_total = num_coins(cents, coins)
            if temp_total < winning_total:
                winning_total = temp_total
            coins = coins [1:]
        else:
            break
    return winning_total

# 31: 7 but now 4
print(min_coins(31))
print(min_coins(76))
print(min_coins(5000))


