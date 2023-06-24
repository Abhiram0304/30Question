f=open("mytxt.txt","r")

data=f.read()
l=data.split(" ")

d={}

s=set(l)

for i in s:
    count=0

    for j in l:
        if(i==j):
            count=count+1
    
    d.update({i:count})

maxi=-1
word=""

for k,v in d.items():
    if(v>maxi):
        maxi=v
        word=k
print(word)
print(d)
