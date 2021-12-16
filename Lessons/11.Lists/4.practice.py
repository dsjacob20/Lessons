
print()

info = ['Name', 'Phone', 'E-mail']
infoa = ['Address', 'Postal Code']

print("Befor we start")
input("Make sure to captalize and put in special charecters when nessesary")
print()

print("This will be the template used to store your information")
print(info)
print(infoa)
input()

x = input("Full name?, ")
info[0] = x

x = input("Phone number?, ")
info[1] = x

x = input("Email?, ")
info[2] = x

print()

x = input("Address?, ")
infoa[0] = x

x = input("Postal Code?, ")
infoa[1] = x



print()
print("Your updated information is...")
print()
print(info)
print(infoa)


print()