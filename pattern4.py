i=int(input("Enter no.of rows"))
for x in range(1,i+1):
    for y in range(i+1,x,-1):
        print("*",end="")
    print("\n")