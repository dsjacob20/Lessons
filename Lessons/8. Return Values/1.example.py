





#define a function called square, which requires an argument for "x" parameter
def square (x):
    y = x * x
    return y
    #y is the return value from the square function
 
#set a value to send as argument
send_to_function = 12
 
#set a return variable which is assigned the return value from function call
square(send_to_function)
return_value_from_square = square (send_to_function)
 
print()
#print statement showing execution of function and return value
print ("The value returned from the square function with", send_to_function,"sent as argument is", return_value_from_square)

print()