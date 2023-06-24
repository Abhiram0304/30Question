import random

def gcd(n1,n2):
    if(n2==0):
        return n1
    return gcd(n2,n1%n2)

f=open("numbers.txt.txt","w")
for i in range(1,101):
    f.write(f"{i}")
    f.write("\n")
f.close()

f=open("numbers.txt.txt","r")
data=f.read().split("\n")
print(data)
for i in range(4,99,5):
    r=random.randrange(1,101)
    if(gcd(int(data[i]),r)==1):
        data[i]="1"
    else:
        data[i]="0"
f.close()

f=open("numbers.txt","w")

for i in range(0,100):
    f.write(data[i])
    f.write("\n")
f.close()

