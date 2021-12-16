o = float(input("Enter the money u want to retrive: $"))
t = float(input("Enter tax percentage: "))
n = (1 + t/100)*o
calculation = "${:.2f} taxed by {:.2f}% is ${:.2f}".format(o, t, n)
print(calculation)