#linear search/sequential search

l=[15,18,2,19,18,0,8,14,19,14]

key=19

check=False

for i in range(0,len(l)):
    if(l[i]==key):
        check=True
        break

if(check==True):
    print("found")
else:
    print("Not Found")
