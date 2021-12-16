
# def grade(g):
#     if g >= 80:
#         print("A")
#     elif g = 65 – 79:
#         print("B")
#     elif g = 50 – 64:
#         print("C")
#     elif g <= 50:
#         print("F")

# grade(90)




# def  oddeven (n):
#     if n % 2 == 1:
#         print(" that nuber is odd")
#     elif n 



# for choices in ["PS10", "TV", "PC",]:
#     print ("hello,", choices)




# def sumTotal(number_for_accumulation):
#     theSum = 0
#     for aNumber in range(1, number_for_accumulation + 1):
#         theSum = theSum + aNumber
#         print (aNumber)
#     return theSum
 
# accumulation_amount = sumTotal(4)
# print("Adds up to", accumulation_amount)




# def invesrtment(money):
#     total = 0
#     for interest in range(40):
#         intersest = 1.50
#         yearly = money * interest
#         total = total + yearly
        
#-----------------------------------------------------------------

# # table setup
# print ("N1", '\t', "N2", '\t', "N1 * N2",)
# print ("-----", '\t', "-----", '\t', "-------")
 
# for x in range (1,11):
#     print (x, '\t', x, '\t', x*x)

# print ("Thanks", '\n', "Goodbye")


# ------------------------------------------------------------
# secret = 'swordfish'
# pw = ''
 
# auth = False
# count = 0
# max_attempt = 5
 
# while pw != secret:
# 	count += 1
# 	if count > max_attempt: break
# 	pw = input(f"Attempt {count}: What's the secret word? ")
# else:
# 	auth = True
# print ("Authorized" if auth else "Calling the cops...")
# ------------------------------------------------------------

secret = "swordfish"
pw = ''
 
auth = False
count = 0
max_attempt = 5
 
while pw != secret:
	count += 1
	if count > max_attempt: break
	if count ==3: continue #Skips attempt #3
	pw = input(f"Attempt {count}: What's the secret word? ")
else:
	auth = True
print ("Authorized" if auth else "Calling the cops...")