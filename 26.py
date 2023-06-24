f=open("vocablulary.txt","r")

#a--97 m--109
#N--78 Z--90

l=[]


for i in range(0,10):
    line=f.readline()
    nl=line.split(" ")
    nl.pop()
    l.append(nl)

for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        check=True
        for k in range(0,len(l[i][j])):
            if((l[i][j][k]>=97 and l[i][j][k]<=109) or (l[i][j][k]))


print(l)