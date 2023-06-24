l=[15,5,4,18,12,19,14,10,8,20]

# count=0

for i in range(0,len(l)):

    # if(count==4):
    #     break

    current=l[i]
    j=i-1

    while(current<l[j] and j>=0):
        l[j+1],l[j]=l[j],l[j+1]
        j=j-1

    # count=count+1
    
    l[j+1]=current

print(l)