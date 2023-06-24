# for i in range(1,11):
#     print(i,end=" ")
# a=["a","b","c","d"]
# print(a[-3:-1:1])


# def is_palin(a):
#     x=int(len(a)/2)
#     c=0
#     while(x!=0):
#         if li[x]==li[-x-1]:
#             c+=1
#         x-=1
#     if c==int(len(a)/2):
#         print("yes")
#     else:
#         print("no")
# li=list(map(str,input().split()))
# is_palin(li)

li=list(map(int,input().split()))
for i in li[::-1]:
    print(i,end=" ")
