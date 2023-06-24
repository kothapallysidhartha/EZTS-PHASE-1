l=int(input("Enter no.of rows"))
for x in range(l,0,-1):
    for y in range(l,0,-1):
        if(x>=y):
            print("*",end="")
        else:
            print("",end="")
    print("\n")
        