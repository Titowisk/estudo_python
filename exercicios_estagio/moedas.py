
coins = [2, 6, 10, 15]
cost = 16
coins.sort(reverse=True)

for coin in coins:
    if coin <= cost:
        cost -= coin 
    else:
        continue

if cost == 0:
    print("sim")
else:
    print("não")
