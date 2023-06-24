# n=input("")
# b=input("")
# if b<=0 or b>n*n or n<=0:
#     print("Invalid Input")
# elif b<=n or b%n==0 or (b-1)%n==0 or (b<=n*n and b>=(n*n)-n):
#     print(" ")
# else:
#     print("*")


# li=list(map(int,input().split()))
# method-1
# sum=0
# for i in range(0,len(li)):
#     c=0
#     for j in range(0,i):
#         if li[i]>li[j] and i!=j:
#             c+=1
#     if c==i:
#         sum+=li[i]
# print(sum)

# method-2
# current_max=li[0]
# result=current_max
# for i in range(len(li)):
#     if li[i]>current_max:
#         current_max=li[i]
#         result+=li[i]
# print(result)


# #wap to print difference btwn left sum and rightsum of every element in list
# li=list(map(int,input().split()))
# left=[]
# right=[]
# left.append(0)
# for i in range(0,len(li)-1):
#     left.append(li[i]+left[i])
# print(left)
# x=-1
# i=0
# right.append(0)
# while i!=3:
#     right.append(li[x]+right[i])
#     i+=1
#     x-=1
# right.reverse()
# print(right)
# for i in range(0,len(li)):
#     sol = left[i]-right[i]
#     print(abs(sol),end=" ")
    
# a=input("")
# l=len(a)-1
# temp=a[0]
# a[0]=a[l-1]
# a[l-1]=temp
# print(a)
li=list(map(str,input().split(",")))
d={}
for i in li:
    i=i.lower()
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for key,value in d.items():
    print(f'{key}:{value}')
    