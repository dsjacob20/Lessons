
print()

rfile = open("../P1/doc.txt", "r", encoding= "utf-8-sig")
wfile =  open("doc2.txt", "w")

el = rfile.readline() 
wfile.write ("Country \t Violent-Crimes\t Property-Crimes\n")

while el:
    values = el.split()
    newline = values[0] + '\t' + values[1] + '\t' + values[2]
    wfile.write(newline + '\n') #Writes the same data into the new file ("out_file")
    el = rfile.readline()

rfile.close()
wfile.close()

print()