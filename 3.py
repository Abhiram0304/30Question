k=3

l=[4,6,4,3,3,4,3,4,3,8]
s=set(l)

ans=[]

for i in s:
    count=0
    for j in l:
        if(i==j):
            count=count+1   
    if(count>k):
        ans.append(i)

print(ans)
