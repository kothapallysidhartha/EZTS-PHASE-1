# li=[]
# li1=[4,3,4,2,1,2,1,5,5,8,3]
# for i in range(0,len(li1)):
#     if i==0:
#         li.append(li1(i))
#     else:
#         for j in li1:
#             if j!=li1(i):
#                 li.append(j)
#

# li=[4,3,4,2,1,2,1,5,5,8,3]
# count=0
# for i in range(0,len(li),1):
#     for j in range(i+1,len(li),1):
#         if(li[i]==li[j]):
#             count+=1
#     if count==0:
#         print(li[i])
#

# lst = [4, 2, 3, 4, 1, 2, 5, 1, 5, 8, 3, 5]
# result = []
# for i in lst:
#     if lst.index(i) == len(lst) - 1 - lst[::-1].index(i):
#         result.append(i)
# 
# print(result)
# # 
# # The if statement in this code is checking if an element in the list lst is unique.
# # 
# # The expression inside the if statement is checking if the first index of the element in the lst is equal to the length of lst minus one minus the first index of the element in the reversed lst.
# # 
# # if lst.index(i) == len(lst) - 1 - lst[::-1].index(i):
# # Here's what each part of the expression means:
# # 
# # lst.index(i) returns the first index of the element i in the lst.
# # lst[::-1] returns a reversed copy of the lst.
# # lst[::-1].index(i) returns the first index of the element i in the reversed lst.
# # len(lst) - 1 gives the last index of the lst.
# # len(lst) - 1 - lst[::-1].index(i) gives the last index of the i in the lst.
# # So, the expression lst.index(i) == len(lst) - 1 - lst[::-1].index(i) is checking if the first index of i in the lst is equal to the last index of i in the lst, which means that i is the only occurrence of i in the lst.
# # 
# # If the expression is true, then the element i is appended to the result list.

# a = [4, 2, 3, 4, 1, 2, 5, 1, 5, 8, 3, 5]
# for k in range(0,len(a)-1,1):
#     for i in range(0,len(a)-1,1):
#         j=i+1
#         if (a[i]!=a[j] and i<=len(a)):
#             continue
#         else:
#             a.remove(a[i])
# print(a)

# a=bin(int(input("")))
# a=a[2:]
# b=int(input("position:"))
# print(a)
# if (a[b]==1):
#     print('true')
# else:
#     print("false")

# 
# a=['apple','sid','teja','ram']
# b=a[1::-1]
# print(b)
        
# a=bin(int(input("")))
# a=a[2:]
# b=int(input("position:"))
# print(a)
# c=int(a)>>b
# d=bin(c)
# print(d[2:])
# if (d[-1]=='1'):
#     print("T")
# else:
#     print("F")

# a=int(input("number:"))
# div=0
# for i in range(1,a):
#     if(a%i==0):
#         div+=i
# if(div==a):
#     print("{} is a perfect number".format(a))
# else:
#     print("{} is not a perfect number".format(a))

a=[-10,0,-1,2,15,1,10,3,4,5,6,7,8,9,11,12,13,15,14,16,20,-5,-3]
b=int(input(""))
c=0
for i in a:
    for j in a[i::]:
        if(i+j==b):
            print(i,"+",j,"=",b)
            c+=1
if c==0:
    print("no such case")  