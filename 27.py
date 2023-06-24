def btd(n):
    deci=0
    i=0
    while(n>0):
        ld=n%10
        deci=deci+(ld)*(2**i)
        i=i+1
        n=n//10
    return deci

b=open("binary.txt","r")
d=open("decimal.txt","r")

bl=b.read().split(" ")
dl=d.read().split(" ")

for i in range(0,len(bl)):
    bl[i]=str(btd(int(bl[i])))

count=0

for i in bl:
    for j in dl:
        if(i==j):
            count=count+1

print(bl)
print(dl)

print(count)