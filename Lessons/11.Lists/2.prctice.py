
print()

def m(n,d):
    months = ["Jan.", "Feb.", "March", "April", "May", "June", "July","Aug.", "Sept.", "Oct.", "Nov.", "Dec.",]
    n = n - 1
    print ( n+1, " - ", months[n], d)
    return n 



x = int(input("Enter the numeric of your birth month ('1-12'), "))
w = int(input("The date you were born in ('1-31'), "))
x = m(x,w)
print()
y = int(input("Enter the numeric of this month right now ('1-12'), "))
z = int(input("Enter today's date ('1-31'), "))

print()
if x == y:
    if w > z:
        print("WOW your b-day is real close!")
    if w == z:
        print("WOW your b-day is Today!")
        print("Congratulations!")
    if w < z:
        print("Just passed your b-day!")
elif x > y:
    print("Your b-day has not passed!")
elif x < y:
    print("Your b-day has already passed!")


print()