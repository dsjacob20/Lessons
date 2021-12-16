print()


# starts the funtion
def withdraw_money(opening_balance, amount):
    if (opening_balance>=amount):
        new_balance = opening_balance - amount
        return new_balance

#main program
updated_amount = withdraw_money(10,130)

print("Your new balance is", updated_amount)

if (updated_amount <= 0):
    print("We need the make a deposit")
else:
    print("Nothing to see here, funds are good")

print()