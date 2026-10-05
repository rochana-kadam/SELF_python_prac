items=[]
prices=[]
total=0

while True:
    item=input("enter a items to purchase (q to quit ): ")
    if item.lower()=='q':
        break
    else:
        items.append(item)
        price=float(input(f"enter price for {item}: $ "))
        prices.append(price)
        total+=price

print("-------Your Cart-------")
print("Items          Price")
for item, price in zip(items, prices):
# *zip pairs them
# *Pizza  → 10
# *Burger → 8
# *Pasta  → 12

    print(f"{item:13} ${price}")
# * add's padding and if u add 0 before 13 it will fill it with zero's
# *left justify
# *right justify-  :>13
# *center align-  :^13

print(f"Your total is ${total:.2f}")


# *print(f"Your total is ${total:010}") 
# *it will give a padding of zero's before the text

