
print()

m = []

print("Input % only")
print()

for x in range(5):
    a = int(input("mark, % "))
    m.append(a)

print()
x = (sum(m)/5)
print("Average =", x,"%")

print()
d = m
d.sort()
print("Highest % is ", d[-1],"%")

print()