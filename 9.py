a=int(input())
x=int(input())
n=int(input())

sum=0
for i in range(1,n+1):
    term=(a**i)*(x**(n-i+1))
    sum=sum+term
print(sum)