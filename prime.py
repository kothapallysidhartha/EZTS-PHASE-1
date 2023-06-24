# x=int(input("Enter a number:"))
# count=0
# if x==1:
#     print("Not a prime number")
# elif(x==2):
#     print(x,"is a prime number")
# elif x>=2:
#     for i in range(2,x):
#         if(x%i)==0:
#             print(x,"is ","Not a prime number")
#             count=0
#             break
#         else:
#             count=1
# if(count==1):
#     print(x,"is a prime number")

strings = input("Enter strings separated by spaces: ").split()

print("The strings you entered are:", strings)
