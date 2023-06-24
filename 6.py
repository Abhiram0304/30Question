n=int(input())
s=int(input())
l=[]

i=2
while(len(l)<=n):
    check=True
    for j in range(2,i):
        if(i%j==0):
            check=False
            break
    if(check==True):
        l.append(i)
    i=i+1

sum=0
for i in l:
    term=1/(i**s)
    sum=sum+term

print(sum)