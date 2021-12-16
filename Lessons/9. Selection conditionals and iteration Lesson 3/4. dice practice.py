
print()

def alpha(y,m):
    if y > m:
        return "You 😥"
    elif y < m:
        return "Me 😜" 
    elif y == m:
        return "Tied 😑"



import random
y = int(random.randrange(1,7))
m = int(random.randrange(1,7))

w = alpha(y,m)

print ("You", '\t', "Me", '\t', "Winner",)
print ("-----", '\t', "-----", '\t', "-------")
print (y, '\t', m, '\t', w)

print()