li=[1,0,1,8,0,1,0,98,2,5,2,10,5]
#normal for loop is not a optimal code
for i in range(len(li)):
    c=0
    for j in range(len(li)):
        if(li[i]==li[j]):
            c+=1
    if(c==1):
        print(li[i])
#using dictionarys the time complexity is better
d={}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d.keys():
    if(d[i]==1):
        print(i)