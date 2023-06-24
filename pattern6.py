l=int(input("Enter no.of rows"))
for x in range(l,0,-1):
    for y in range(0,x):
        print(chr(y+65),end="")
    print("\n")