
print()




# list_1 = [10, 20, 30]
# list_2 = ["red", "blue", "green"]
# list_3 = [5, "six", 7.0, [8,9,0], True] #int, str, float, list, bool
# list_4 = []

# vocabulary = ["iteration", "selection", "control"]
# numbers = [17, 123]
# empty = []
# mixedlist = ["hello", 2.0, 5*2, [10, 20]]
 
# print(numbers) # [17, 123]
# print(mixedlist) # ['hello', 2.0, 10, [10, 20]]
# print (empty) # []
# print (mixedlist) # ['hello', 2.0, 10, [10, 20]]
 
# def list_change(info):
#     newlist = info
#     print (newlist) # [[17, 123], ['iteration', 'selection', 'control']]
 
# list_change ([ numbers, vocabulary ]) #call function using list






# alist =  ["hello", 2.0, 5, [10, 20]]
# print(len(alist)) #prints 4
# print(len(['spam!', 1, ['Brie', 'Chedder', 'Swiss'], [1, 2, 3]])) #Also prints 4






# items = ["one", "two", [1,2,3], "three", "four", "five"]
# print (items[2]) #[1,2,3]
# print (items[-1]) #five
# print (items[0], (items[len(items)-1])) #one five


# days = ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun",]
# for i,d in enumerate(days):
#    print (i, d)






# fruit = ["apple", "orange", "banana", "cherry"]
 
# print("apple" in fruit) #True
# print("pear" in fruit) #False
# print ("grape" not in fruit) #True

# nums = [1, 2.0, 3, 4, "five"]
 
# print("five" in nums) #True
# print(2.01 in nums) #False
# print (5 not in nums) #True







# x = ["yes", "ya", "oui", "si",]
 
# answer = input ("Is Comp Sci fun? ")
 
# if answer in x:
#     print ("Yes, I agree!")
 
# else:
#     print ("Well, I think it is fun, so we don't agree")


# x = ["one", "two", "three", "four"]
# y = "two"
 
# if y is x[1]:
#     print ("True")
# else:
#     print ("Not true")






# fruit = ["apple", "orange", "banana", "cherry"]
# print([1, 2] + [3, 4]) #[1, 2, 3, 4]
# print(fruit + [6, 7, 8, 9]) #['apple', 'orange', 'banana', 'cherry', 6, 7, 8, 9]
# print([0] * 4) #[0, 0, 0, 0]
# print([1, 2, ["hello", "goodbye"]] * 2) #[1, 2, ['hello', 'goodbye'], 1, 2, ['hello', 'goodbye']]
# print (fruit[0] * 3) #appleappleapple


# fruit = ["apple", "orange", "banana", "cherry"]
# numlist = [6, 7]
# newlist = fruit + numlist
# zeros = [0] * 4
# print (type(newlist), newlist, zeros) 
# #<class 'list'> ['apple', 'orange', 'banana', 'cherry', 6, 7] [0, 0, 0, 0]






# a_list = ['a', 'b', 'c', 'd', 'e', 'f']
# print(a_list[1:3]) #['b', 'c']
# print(a_list[:4]) #['a', 'b', 'c', 'd']
# print(a_list[3:]) #['d', 'e', 'f']
# print(a_list[:]) #['a', 'b', 'c', 'd', 'e', 'f']


# fruit = ["banana", "apple", "cherry"]
# print(fruit) #['banana', 'apple', 'cherry']
 
# fruit[0] = "pear" #Item Assignment – pear goes into index slot 0
# fruit[-1] = "orange" #Item Assignment – orange goes into index slot -1 (last item always)
# print(fruit) #['pear', 'apple', 'orange']


# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = ['x', 'y']
# print(alist) #['a', 'x', 'y', 'd', 'e', 'f']

# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# alist[1:3] = []
# print(alist) #['a', 'd', 'e', 'f']

# alist = ['a', 'd', 'f']
# alist[1:1] = ['b', 'c'] #updates or creates new list
# print(alist) #['a', 'b', 'c', 'd', 'f']
# alist[4:4] = ['e'] #updates or creates new list
# print(alist) #['a', 'b', 'c', 'd', 'e', 'f']





# a = ['one', 'two', 'three']
# del a[1] #removes the 2nd element
# print(a) #['one', 'three']
 
# alist = ['a', 'b', 'c', 'd', 'e', 'f']
# del alist[1:5] #removes element 1 to 4, leaving 0 and 5
# print(alist) #['a', 'f']


# a = ['one', 'two', 'three']
# del a[-1] #removes the last element
# print(a) #['one', 'two']






# a = "banana"
# b = "banana"
# print (a is b) #True


# a = [81, 82, 83]
# b = [81, 82, 83]
 
# print(a is b) #False
# print(a == b) #True


# a = [81, 82, 83]
# b = a
 
# print(a is b) #True
# print(a == b) #True

# b[0] = 5
# print (a) #[5, 82, 83]





# a = [81, 82, 83]
# b = a[:]
 
# print(a is b) #False
# print(a == b) #True
 
# b[0] = 5
# print (a) #[81, 82, 83]
# print (b) #[5, 82, 83]






# origlist = [45, 76, 34, 55]
# print(origlist * 3) #[45, 76, 34, 55, 45, 76, 34, 55, 45, 76, 34, 55]
 
# newlist = [origlist] * 3
# print(newlist) #[[45, 76, 34, 55], [45, 76, 34, 55], [45, 76, 34, 55]]



# origlist [1] = 99
# newlist = [origlist] * 3
# print(newlist) #[[45, 99, 34, 55], [45, 99, 34, 55], [45, 99, 34, 55]]







# mylist = []
# mylist.append(5)
# mylist.append(27)
# mylist.append(3)
# mylist.append(12)
# print(mylist) #[5, 27, 3, 12]


# mylist.insert(1, 12) # Insert 12 at pos 1, shift other items up
# print(mylist) #[5, 12, 27, 3, 12]


# print(mylist.count(12)) #How many times is 12 in mylist? - Returns 2


# print(mylist.index(27)) #Find index of first 3 in mylist - Returns 2
# print(mylist.count(5)) #There is ONE instance of "5" in list - Returns 1


# mylist.reverse() #Reverses the list
# print(mylist) #[12, 3, 27, 12, 5]


# mylist.sort() #Sorts the list in ascending order
# print(mylist) #[3, 5, 12, 12, 27]


# mylist.remove(12) # Removes the first 12 in the list
# print(mylist) #[3, 5, 12, 27]


# lastitem = mylist.pop()     # Removes and returns the last item of the list
# print(lastitem) #27
# print(mylist) #[3, 5, 12]


# lastitem = mylist.pop(2)     # Removes and returns the item at set position
# print(lastitem) #12
# print(mylist) #[3, 5, 27]







# origlist = [45, 32, 88]
# origlist.append ("cat")
 
# print (origlist) #[45, 32, 88, 'cat']

        ##OR

# origlist = [45, 32, 88]
# origlist = origlist + ["cat"] #Concatenation of TWO LISTS
 
# print (origlist) #[45, 32, 88, 'cat']






# fruits = ["apple", "orange", "banana", "cherry"]
 
# for afruit in fruits:     # traverses list by item
#     print(afruit) #Prints each item going down list


# fruits = ["apple", "orange", "banana", "cherry"]
# print(len(fruits))
# for position in range(len(fruits)):     # traverses list in range of items by index
#     print(fruits[position]) #prints each position - same result going down list


# numbers = [1, 2, 3, 4, 5]
# print(numbers) #[1, 2, 3, 4, 5]
 
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] ** 2 #Squares the number
 
# print(numbers) #[1, 4, 9, 16, 25]


# alist = [4, 2, 8, 6, 5]
# blist = [ ]
# for item in alist:
#     blist.append(item%2 ==0)
# print(blist) #[True, True, True, True, False]








# sum = 0
# for num in [1, 3, 5, 7, 9]:
#     sum = sum + num
# print(sum) #25 has been accumulated


# long_names = 0
# for name in ["Joe", "Sally", "Amy", "Brad"]:
#     if len(name) > 3:
#         long_names += 1 #Different way of using accumulator - could have used long_names = long_names + 1
# print(long_names) #2


# s = "what if we went to the zoo"
# num_vowels = 0
# for i in s:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         num_vowels += 1
# print(num_vowels) #Outputs 8 as there are 8 vowels in string


# nums = [9, 3, 8, 11, 5, 29, 2]
# best_num = 0
# for n in nums:
#     if n > best_num:
#         best_num = n
# print(best_num) #Outputs 29 as that was iterated to be highest value from list


# list= [5, 2, 1, 4, 9, 10]
# min_value = 0
# for item in list:
#    if item < min_value:
#        min_value = item
# print(min_value)


# nums = [9, 3, 8, 11, 5, 29, 2]
# best_num = nums[0]







print()