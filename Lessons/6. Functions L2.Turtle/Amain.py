

#Main Program File for Module_Test_1
print()
print("Welcome to the module import program!")
 
import AModule_database
 
print ("We will now access the data from the module!")
 
#Call script-1 function from Module
AModule_database.script_1()
print ("Magic!!")
 
#Call art_1 function from Module, BUT WAITS FOR USER TO CLICK ENTER!
input ("ready for some art? (Click Enter to start) ")
AModule_database.art_1()
 
print ("Thanks, goodbye")