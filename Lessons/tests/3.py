


def square (x):
    running_total = 0
    for counter in range(x):
        running_total = running_total + x
    return running_total
 
send_to_square = 12
square_result = square(send_to_square)
 
print ("The result of", send_to_square, "squared is", square_result)