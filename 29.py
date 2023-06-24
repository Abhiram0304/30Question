def reverse(name,vowel_index):
    s=""
    for i in range(vowel_index-1,-1,-1):
        s=s+name[i]
    return s

f=open("student.txt","r")

name=[]

for i in range(0,3):
    data=f.readline().split(" ")
    name.append(data[0])

for i in range(0,3):
    check=True
    for j in range(0,len(name[i])):
        if(check==True):
            if(name[i][j] in "aeiou"):
                rev=reverse(name[i],j)
                remain=name[i][j:len(name[i])]
                name[i]=rev+remain
                check=False
    
print(name)
