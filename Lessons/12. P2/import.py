print()
# marks = open("doc.txt", "r", encoding= "utf-8-sig")
 
# for aline in marks:
#     six = aline.split()
#     #print (six) # check to see lists printed
#     if len(six)>7:
#         print (six)
 
# marks.close()




# marks = open("doc.txt", "r", encoding= "utf-8-sig")
 
# for aline in marks:
#     avs = aline.split()
#     #print (avs) #check to see lists printed
#     sum = 0
#     for total in avs[1:]:
#         number_of_tests = len(avs)-1
#         total = int(total)
#         sum = sum + total
#         average = sum/number_of_tests
#         average = (round(average,0))
   
#     print (avs[0], "wrote", number_of_tests, "tests. Overall average was:",average)
#     print()
 
# marks.close()






marks = open("doc.txt", "r", encoding= "utf-8-sig")
 
for aline in marks:
    min_max = aline.split()
    #print (min_max) #check to see lists printed
    max = 0
    min = 100
    for check_max in min_max[1:]:
        check_max = int(check_max)
        if check_max > max:
            max = check_max
    for check_min in min_max[1:]:
        check_min = int(check_min)
        if check_min < min:
            min = check_min
 
    print (min_max[0], "Maximum Score was:", max)
    print (min_max[0], "Minimum score was:", min)
    print ()
 
marks.close()



print()