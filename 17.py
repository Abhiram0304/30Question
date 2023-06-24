#selection sort

l=[17,7,12,14,19,1,6,18,8,20]
size=len(l)

for i in range(0,len(l)-1):  # for question(0,4)
    for j in range(i+1,len(l)):
        if(l[j]<l[i]):
            # temp=l[i]
            # l[i]=l[j]
            # l[j]=temp
            l[j],l[i]=l[i],l[j]
print(l)


