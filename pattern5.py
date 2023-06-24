i=int(input("Enter no.of rows"))
for x in range(65,i+65):
    for y in range(65,x+1):
        print(chr(x),end="")
    print("\n")