x=int(input("Enter no.of rows"))
y=x
for i in range(65,x+65):
    for j in range(65,i+1):
        print(chr(j),end="")
    print("\n")