




#t = total price
#g = with GST
#d = after Discount
#f = Final price

def calc(t, d):
    g = t * 1.05           #Adds GST
    g = round(g, 2)
    print(  "+GST                 $",g)

    print(  "Discount            ", d,"%")
    d = d/100              #Discount
    d = g * d
    d = round(d, 2)
    print(  "                  = -$",d)

    f = g - d              #Subtracts 
    f = round(f, 2)
    return f


print()

#customer inputs price
q = (input("Input the price of your first item, $"))
q = float(q)
q = round(q, 2)
print()
w = (input("Input the price of your second item, $"))
w = float(w)
w = round(w, 2)
print()
e = (input("Input the price of your first item, $"))
e = float(e)
e = round(e, 2)

# tprice
t = q + w + e   

t = round(t, 2)


import random                        #Random(discount)
d = random.choice (["10", "15", "20"])
d = float(d)

print()
print("--------------------------------")
print ("            Receipt        ")
print(  "Item 1               $", q, "  ")
print(  "Item 2               $", w, "  ")
print(  "Item 3               $", e, "  ")
print(  "                     ----------")
print(  "Total                $", t, "  ")

f = calc(t, d)                          #CALLS def...

print(  "                     ----------")
print("Amount Due           $", f)
print()
print("--------------------------------")
print()
