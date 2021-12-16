print()


# ccfile = open("ccdata.txt", "r")
 
# for aline in ccfile1:
#     values = aline.split()
#     print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emissions were', values[2], 'gigatons.')
 
# ccfile.close()



# check_file = open("ccdata.txt", "r") #Opens the file from location path
 
# check_a_line = check_file.readline() #Reads first line ***ENDS when it reaches the "NEW LINE" (enter =  \n)
# print (check_a_line)
 
# check_a_line = check_file.readline() #Reads the NEXT line from where last READ left off after NEW LINE \n
# print (check_a_line)
 
# check_file.close()





# check_file.close()


# file_list = check_file.readlines() #Returns the entire contents as a LIST
# print (file_list [0:4]) #Print the FIRST 4 LINES as a list (items 0,1,2,3)
# print (file_list [5]) #Prints the 6th item (positions 0,1,2,3,4,5)



# check_file = open("ccdata.txt", "r") #Opens the file from location path
 
# file_string = check_file.read() #Reads the ENTIRE FILE into a single string
# print (file_string) #Prints the entire file as a single string formatted with lines, columns, etc.
# print (len(file_string)) #Prints the number of characters in entire file string
# print (file_string [0:145]) #Prints from characters 0-144
 
# check_file.close()



# check_file_loop = open("ccdata.txt", "r") #Opens the file from location path
 
# each_line = check_file_loop.readline()
 
# while each_line:
#     values = each_line.split()
#     print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emissions were', values[2], 'gigatons.')
#     each_line = check_file_loop.readline()
 
# check_file_loop.close()
















# in_file = open("ccdata.txt", "r") #Opens the file to READ from location path
 
# each_line = in_file.readline() #This write_file expression is TRUE unless the line is empty
# print ("Year\tEmission\n") #Prints Title Bar with YEAR and EMISSION separated by space (\t) and ends with New Line (\n)
# while each_line: #Starts as TRUE unless the file is empty line
#     items = each_line.split() #breaks the items for each line
#     data_line = items[0] + '\t' + items [2] #This will omit the middle column and separate column 0 and 2 with \t space
#     print (data_line)
#     each_line = in_file.readline() #Iterates to the next line of text
 
# in_file.close()




in_file = open("ccdata.txt", "r") #Opens the file to READ from location path
out_file = open("ccdata2.txt", "w") #Opens a NEW file to WRITE to location path

each_line = in_file.readline() #This write_file expression is TRUE unless the line is empty
out_file.write ("Year\tEmission\n") #This will be the ONLY line in "out_file" ("year_and_emmisions_data.txt") at this point
 
while each_line: #Starts as TRUE unless the file is empty line
    items = each_line.split() #breaks the items for each line
    data_line = items[0] + '\t' + items [2] #This will omit the middle column and separate column 0 and 2 with \t space
    out_file.write(data_line + '\n') #Writes the same data into the new file ("out_file")
    each_line = in_file.readline() #Iterates to the next line of text
 
in_file.close()
out_file.close()












print()
