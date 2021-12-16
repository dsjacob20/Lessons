
# eng_to_span = {} #Creates empty dictionary
 
# eng_to_span ["one"] = "uno" #Key/ Value Pair (object) is added
# #Left side gives the DICTIONARY and the KEY being associated
# #Right side gives the value being associated with the key
# eng_to_span ["two"] = "dos" #Key/ Value Pair (object) is added
# eng_to_span ["three"] = "tres" #Key/ Value Pair (object) is added
 
# print (eng_to_span["two"]) #Prints dos



# eng_to_span = {"one": "uno", "two": "dos", "three": "tres", }
 
# print (eng_to_span["two"]) #Prints dos
# print (eng_to_span) #prints entire dictionary



# eng_to_span = {"one": "uno", "two": "dos", "three": "tres", }
 
# item = eng_to_span ["two"]
# print (item) #Also prints dos



# holiday_options = {
#     'Mexico': 5000,
#     'Las Vegas': 3000,
#     'Vancouver': 2000,
#     'Leduc': 175,
#     'needs': ("Suitcase", "Sunglasses", "Money",)
# }
 
# choice = holiday_options['Mexico']
# print ("Cost will be $", choice, ", and don't forget", holiday_options['needs'])

# print ("Cost will be $", choice, ", and don't forget", holiday_options['needs'][1])

















# pirate = {
#   "hello": "avast",
#   "man": "matey",
#   "your": "yer",
# }
# for suggestions in pirate.keys():
#     print (suggestions)



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200, 'pears': 75}
# del inventory ['pears']
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200}



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200, 'pears': 75}
# inventory ['pears'] = 0 #Modified the value for pears to now be ‘0’
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200, 'pears': 0}



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200, 'pears': 75}
# inventory ['bananas'] = inventory['bananas'] + 200 #updates to add 200 more bananas
# print (inventory) #{'apples': 250, 'bananas': 350, 'oranges': 200, 'pears': 75}



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# print (inventory) #{'apples': 250, 'bananas': 150, 'oranges': 200, 'pears': 75}
# inventory ['bananas'] = inventory['bananas'] + 200 #updates to add 200 more bananas
# print (inventory) #{'apples': 250, 'bananas': 350, 'oranges': 200, 'pears': 75}
# inventory ['grapes'] = inventory['oranges'] + inventory['apples'] #add new item value-pair
# print (inventory) #{'apples': 250, 'bananas': 350, 'oranges': 200, 'pears': 75, 'grapes': 450}



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# for a_key in inventory.keys(): #order is not defined
#     print ("Got key", a_key, "which maps to value", inventory[a_key]) #second part reads  value
 
# key_list = list(inventory.keys())
# print (key_list)



# inventory = {
#     'apples': 250,
#     'bananas': 150,
#     'oranges': 200,
#     'pears': 75,
# }
# print (list(inventory.values())) #[250, 150, 200, 75]
# print (list(inventory.items())) #[('apples', 250), ('bananas', 150), ('oranges', 200), ('pears', 75)]
 
# for (keys, values) in inventory.items():
#     print ("Got", keys, "that map to", values)
 
# for keys in inventory:
#     print ("Got", keys, "that map to", inventory[keys])



# #-------------------------------------------------------------------------------
# inventory = {
#    'apples': 250,
#    'bananas': 150,
#    'oranges': 200,
#    'pears': 75,
# }
# for a_key in inventory.keys(): #order is not defined
#    print ("{:<20}{}".format(a_key, inventory[a_key]))

# for a_key in inventory.keys(): #order is not defined
#    print ("{:<20}:{:>10}".format(a_key, inventory[a_key]))
# #-------------------------------------------------------------------------------



# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# print('apples' in inventory) #True
# print('cherries' in inventory) #False
 
# if 'bananas' in inventory:
#     print(inventory['bananas']) #312
# else:
#     print("We have no bananas")



# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
 
# print(inventory.get("apples")) #430
# print(inventory.get("cherries")) #None
# print(inventory.get("cherries", 0)) #0



# mydictionary = {"cat":12, "dog":6, "elephant":23, "bear":20}

# keylist = list(mydictionary.keys())
# keylist.sort()
# print(keylist)
# val_list = list(mydictionary.values())
# val_list.sort()
# print (val_list)

# new = mydictionary.keys()
# print (sorted(new))










# opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
# print (opposites) #{'up': 'down', 'right': 'wrong', 'true': 'false'}
 
# alias = opposites
# print(alias is opposites) #True
 
# alias['right'] = 'left'
# print(opposites['right']) #left
 
# print (opposites) #{'up': 'down', 'right': 'left', 'true': 'false'}




# opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
# print (opposites) #{'up': 'down', 'right': 'wrong', 'true': 'false'}
 
# acopy = opposites.copy() #makes a copy of dictionary assigned to "acopy" variable
# print(acopy is opposites) #False
 
# acopy['right'] = 'left' #doesn't change the "opposites" dictionary - only the copy!
# print(opposites['right']) #wrong
 
# print (opposites) #{'up': 'down', 'right': 'left', 'true': 'false'}
# print (acopy) #{'up': 'down', 'right': 'left', 'true': 'false'}