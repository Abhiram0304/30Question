s=input("String  : ")
l=s.split(",")

for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]

print(l)