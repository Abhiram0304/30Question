#bubble sort

l=[19,1,9,7,12,3,10,13,15,8]

end=len(l)-1

while(end>0):      #len(l)-4
    for i in range(0,end):
        if(l[i]>l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
    end=end-1

print(l)