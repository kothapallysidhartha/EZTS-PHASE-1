# v=0
# c=0
# s=0
# num=0
# special=0
# exp=input("Enter statement")
# for i in exp:
#     if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
#         v+=1
#     elif(i==' '):
#         s+=1
#     elif(i>='0' and i<='9'):
#         num+=1
#     elif((i>'a' and i<='z' ) or (i>'A' and i<='Z') and( i!='e' or'E' or'I'or'i'or'o'or'O'or'U'or'u')):
#         c+=1
#     else:
#         special+=1
# print("Vowels:",v,"\ncon:",c,"\nspaces:",s,"\nnumbers:",num,"\nspecial char:",special)
#


# def oddeven(n):
#     if n%2!=0:
#         return True
#     else:
#         return False
# def pal():
#     st = input("enter the  string: ")
#     j = -1
#     flag = 0
#     for i in st:
#         if i != st[j]:
#             flag = 1
#             break
#         j = j - 1
#     if flag == 1:
#         print("NO")
#     else:
#         print("Yes")
# def prime(x):
#     count=0
#     if x==1:
#         print("Not a prime number")
#     elif(x==2):
#         print(x,"is a prime number")
#     elif x>=2:
#         for i in range(2,x):
#             if(x%i)==0:
#                 print(x,"is ","Not a prime number")
#                 count=0
#                 break
#             else:
#                 count=1
#     if(count==1):
#         print(x,"is a prime number")
def pattern():
    names = "balaji"
    n = len(names)
    for i in range(n):
        for j in range(n):
            if i == j or i == n-j-1:
                print(names[j], end=" ")
            else:
                print(" ", end=" ")
#         print("\n")
# while True:   
#     print("Select:\n1.Prime\n2.ODD OR EVEN\n3.palindrome\n4.pattern\n5.Exit")
#     a=int(input(("Enter choice:")))
#     if(a==1):
#         x=int(input("Enter a number"))
#         prime(x)
#     elif(a==2):
#         j=int(input("Enter a number"))
#         val=oddeven(j)
#         if(val==True):
#             print("Odd")
#         else:
#             print("Even")
#     elif(a==3):
#         pal()
#     elif(a==4):
#         pattern()
#     else:
#         break
    
# class mohith:
#     print('the neon numbers are:')
#     for i in range(0,101):
#         x=i*i
#         s=0
#     while(x!=0):
#         s=s+x%10
#         x=x//10
#     if(i==s):
#         print(i,end=" ")
# class bike2(mohith):
#     user_num = int(input("Enter a number: "))
#     if is_magical_prime(user_num):
#         print(f"{user_num} is a magical prime number.")
#     else:
#         print(f"{user_num} is not a magical prime number.")
# 
#     number = input("Enter a number: ")
#     print(len(str(number)))
#     num = int(input("Enter a number: "))
#     flag = False
#     if num == 1:
#         print(num, "is not a prime number")
#     elif num > 1:
#     
#         for i in range(2, num):
#             if (num % i) == 0:
#             
#                 flag = True
#       
#             break
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")






# parent class
# class Student():
#    # constructor of parent class
#    def __init__(self, name, enrollnumber):
#       self.name = name
#       self.enrollnumber = enrollnumber
#    def display(self):
#       print(self.name)
#       print(self.enrollnumber)
# # child class
# class College( Student ):
#    def __init__(self, name, enrollnumber, admnyear, branch):
#       self.admnyear = admnyear
#       self.branch = branch
#       # invoking the __init__ of the parent class
#       Student.__init__(self, name, enrollnumber)
# # child class
# class University( Student ):
#    def __init__(self, name, enrollnumber, refno, branch):
#       self.refno = refno
#       self.branch = branch
#       # invoking the __init__ of the parent class
#       Student.__init__(self, name, enrollnumber)
# # creation of an object for base/derived class
# obj_1 = College('Rohit',42414802718,2018,"CSE")
# obj_1.display()
# obj_2 = University ('Rohit',42414802718,"st2018","CSE")
# obj_2.display()

class student:
    rollno =2000
    x=20
    name="sidhu"
    age=19
    sal=100000
    def _init_(self):
       print("wish all the success")
    def _init_(self):
         print("best of luck")
    def display(self):
        print(self.rollno,self.name,self.age,self.sal)    
st=student()
print(st.display(),st._init_())