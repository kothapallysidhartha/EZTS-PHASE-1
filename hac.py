n=int(input(""))
li=list(map(int,input().split(" ")))
lar=li[0]
li.sort()
x=len(li)-1
m=1
while(m):
    if li[x]==li[x-1]:
        x-=1
    else:
        print(li[x-1])
        m=0
a=5
b=5
print(id(a))
print(id(b))