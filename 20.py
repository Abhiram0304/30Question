#binary search

l=[3,5,6,8,11,12,14,15,17,18]

key=179

start=0
end=len(l)-1
mid=(start+end)//2
check=False
while(start<end):
    if(l[mid]==key):
        check=True
        break
    
    elif(l[mid]<key):
        start=mid+1
    
    elif(l[mid]>key):
        end=mid-1
    
    mid=(start+end)//2

if(check==True):
    print("found")

else:
    print("NOt Found")