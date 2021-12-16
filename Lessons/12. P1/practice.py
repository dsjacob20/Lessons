print()

doc = open("doc.txt", "r", encoding= "utf-8-sig")
 
for aline in doc:
    values = aline.split()
    print('In', values[0], 'the average crime rate for violaent crime is', values[1], 'and property realted crime is', values[2], '.')
 
doc.close()





# file = open("../PYTHON FILES CREDIT/ccdata.txt")
# for aline in file:
#     values = aline.split()
#     print('In', values[0], 'the average crime rate for violaent crime is', values[1], 'and property realted crime is', values[2], '.')
 
# file.close()



print()