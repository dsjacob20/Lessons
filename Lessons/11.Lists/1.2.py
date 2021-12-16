print()




# def doubleStuff(aList):
#     """ Overwrite each element in aList with double its value. """
#     for position in range(len(aList)):
#         aList[position] = 2 * aList[position]
 
# things = [2, 5, 9]
# print(things) #[2, 5, 9]
# doubleStuff(things)
# print(things) #[4, 10, 18]



# def doubleStuff(a_list):
#     """ Return a new list in which contains doubles of the elements in a_list. """
#     new_list = [] #initiate new list
#     for value in a_list:
#         new_elem = 2 * value
#         new_list.append(new_elem) #add new item to new list
#     return new_list #This is using the new created list instead of changing the original
 
# things = [2, 5, 9]
# print(things) # [2, 5, 9]
# things = doubleStuff(things)
# print(things) # [4, 10, 18]






# mylist = [1,2,3,4,5, 11]
 
# yourlist = [item ** 2 for item in mylist if item<10]
 
# print(yourlist) # [1, 4, 9, 16, 25] - DOESN'T incluse the 11 from "mylist"



# mylist = [1,2,3,4,5, 11]
# yourlist = [item ** 2 for item in mylist] #doesn't have IF clause
 
# print(yourlist) #[1, 4, 9, 16, 25, 121]





# nested = ["hello", 2.0, 5, [10, 20]]
# innerlist = nested[3]
# print(innerlist) #Extracted index 3: [10, 20]
# item = innerlist[1]
# print(item) #Extracted index [1] from nested list: 20
 
# print(nested[3][1]) #Also 20 - combines the two steps above















# song = "The rain in Spain..."
# wds = song.split() #Creates a LIST of each word (between whitespace)
# print(wds) # ['The', 'rain', 'in', 'Spain...']



# myname = "Edgar Allan Poe"
# namelist = myname.split()
# print (namelist) #['Edgar', 'Allan', 'Poe']
# init = ""
# for aname in namelist:
#     init = init + aname[0] #Iterates with FIRST INDEX from each string
# print(init) # EAP



# wds = ["red", "blue", "green"]
# glue = '; ' #The "separator string" is designated as ";"
# s = glue.join(wds)
# print(s) # red; blue; green
# print(wds) # Prints the list: ['red', 'blue', 'green']

# print(" *** ".join(wds)) # *** is set as "separator string", outputs: red *** blue *** green
# print(" ".join(wds)) # Empty whitespace as separator: outputs: red blue green













# xs = list("Green Frog")
# print(xs) # ['G', 'r', 'e', 'e', 'n', ' ', 'F', 'r', 'o', 'g']


# xs = list("Green Frog" + "Black Dog")
# print(xs) # ['G', 'r', 'e', 'e', 'n', ' ', 'F', 'r', 'o', 'g', 'B', 'l', 'a', 'c', 'k', ' ', 'D', 'o', 'g']


# xs = list("12345")
# print(xs) # ['1', '2', '3', '4', '5']











# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# print(julia[2])
# print(julia[2:6])
 
# print(len(julia))
 
# for field in julia:
#     print(field)
 
# julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
# print(julia) # ('Julia', 'Roberts', 1967, 'Eat Pray Love', 2010, 'Actress', 'Atlanta, Georgia')




# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# (name, surname, birth_year, movie, movie_year, profession, birth_place) = julia
 
# print (surname) #Roberts
# print (birth_place) #Atlanta, Georgia










# def circleInfo(r):
#     """ Return (circumference, area) of a circle of radius r """
#     c = 2 * 3.14159 * r
#     a = 3.14159 * r * r
#     return (c, a)
 
# print(circleInfo(10))





# def space_layout (l, w, h):
#     """Return area and volume of a space with given length, width, height"""
#     floor_space = l * w
#     volume_space = l * w * h
#     return (floor_space, volume_space)
 
# specs = space_layout (10.5, 18, 8)
# print (specs) #(189.0, 1512.0)
 
# (area, volume) = specs
# print (area) # 189.0
# print (volume) # 1512.0








print()