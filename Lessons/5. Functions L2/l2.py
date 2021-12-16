print()

print("$5 - Chicken Burger")
print("$8 - Beef Burger")
print("$9 - Vegan Burger")

print()

x = (input("Enter the amount of money nesseary for the item you need, $"))
#word to number
x = int(x)  

print("-----------------------------")
def food(amount_paid):
    if (amount_paid == 5):
        print("Your order has been placed")
        print("1 Chicken Burger")
 
    if (amount_paid == 8):
        print("Your order has been placed")
        print("1 Beef Burger")

    if (amount_paid == 9):
        print("Your order has been placed")
        print("1 Veagn Burger")
food(x)
print("-----------------------------")

print()
