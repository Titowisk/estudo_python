# coding=utf-8

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

"""
Mostra o inventário e o total de items.
"""
def displayInventory(inventory):
    sum = 0
    for item, n in inventory.items():
        print('{0}  {1}'.format(n, item))
        sum = sum + n
    print('Total number of items: {}'.format(sum))

displayInventory(inventory)

"""
Adiciona os items do loot ao inventário do nosso nobre herói ou heroína.
"""
def updateInventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory.setdefault(item, 1)

    displayInventory(inventory)

updateInventory(inventory, dragon_loot)
