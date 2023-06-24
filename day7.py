# x=int(input(""))
# r=1
# for i in range(1,x+1):
#     r*=i
# print(r)

# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter a number:"))
# print("factorial of ",n," is:",fact(n))

# def fab(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fab(n-1)+fab(n-2)
# 
# n=int(input("Enter a number:"))
# for i in range(0,n):
#     print(fab(i),end=" ")



# def mut(x,y):
#     z=x%y
#     if z==0:
#         return x
#     return x*mut(y,z)/z
# 
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# print(mut(a,b))

# def harmonic_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return 1/n + harmonic_sum(n-1)
# 
# n = int(input("Enter integer: "))
# print("The harmonic sum of", n, "is", harmonic_sum(n))


# 
# x=int(input("Enter size of list:"))
# li=[]
# print("Enter elements:")
# for i in range(0,x):
#     li.append(int(input("")))
# un=int(input("Enter a number:"))
# c=0
# for i in li:
#     if i<un:
#         c+=1
# if c==un:
#     print("unique")
# else:
#     print("not unq")



# x=int(input("Enter size of list:"))
# li=[]
# print("Enter elements:")
# for i in range(0,x):
#     li.append(int(input("")))
# k=int(input("Enter k value:"))
# e=int(input("Enter expt marks:"))
# sorted_list = []
# while li:
#     minimum = li[0]
#     for item in li:
#         if item < minimum:
#             minimum = item
#     sorted_list.append(minimum)
#     li.remove(minimum)
# print(sorted_list)
# sum=0
# for i in range(0,k):
#     sum+=sorted_list[i]
# print(sum)
# if sum<e:
#     print("avg")
# else:
#     print("good")


# x=int(input("Enter size of list:"))
# li=[]
# print("Enter elements:")
# for i in range(0,x):
#     li.append(int(input("")))
# 
# dub=li[1]
# count=0
# for i in li:
#     if i==dub or count==0:
#         count+=1
#     else:
#         print(dub," is repeated for ",count)
#         dub=i
#         count=1

# a=[0,1,2,3,6]
# c=0
# for i in a:
#     for j in a[::]:
#         if i!=j:
#             print(i," ",j)
#         c+=1

# x=input()
# if len(x)>=5:
#     count=1
#     for i in x:
#         if count<len(x):
#             count+=1
#     print(x[0],count-2,i)
# else:
#     print("string length is shorter than 5")


n=int(input())
li=[]
while n!=1:
    if n%3==0:
        n=n/3
        li.append(int(n))
    elif n%2==0:
        n=n/2
        li.append(int(n))    
    else:
        n=n-1
print(li)
