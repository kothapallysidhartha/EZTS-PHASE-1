# #some operators in python
# a=5
# a+=5
# print(a)
# a%=5
# print(a)
# a=5
# a**=5
# print(a)
# a//=5
# print(a)

user_name="sidhu_012"
pass_code="12345678"
check_user=input("User name:")
check_pass=input("pass code:")
if((user_name==check_user) and (pass_code!=check_pass)):
    print("pass code is incorrect")
elif((pass_code==check_pass) and (user_name!=check_user)):
    print("user name is incorrect")
elif((user_name==check_user) and (pass_code==check_pass)):
    print("login success")
else:
    print("both pass code and user id is incorrect")


# n=1
# a=[]
# while (n!=21):
#     x=int(input("Enter roll.no:"))
#     a.append(x)
#     n+=1
# print(a)


# a=[]
# n=int(input("enter no.of inputs:"))
# 
# for i in range(1,n):
#     if((i<21 or i==50)):
#         print(i,"eligible")
#         a.append(i)
#     else:
#         print(i,"not eligible")
# print(a)
days=84
calls=3000
msg=100
data=2
while True:
    u_days=input("enter day:")
    u_calls=int(input("enter no.of calls:"))
    u_msg=int(input("Enter no.of msg:"))
    u_data=float(input("Enter data usage:"))
    if not (u_days>=1 or u_calls>3000 or u_msg>100 or data>2):
        print("invalid input \n Enter correct input")
        continue
    else:
        break
if(u_days>84):
    print("plane was expired ,please kindly recharge")
elif(u_days<84 and u_days>=1):
    print("DAY:",u_days)
    print("CALLS LEFT-OVER:",calls-u_calls)
    print("MSG LEFT-OVER:",msg-u_msg)
    print("DATA LEFT-OVER:",data-u_data)
