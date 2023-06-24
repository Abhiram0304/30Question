f=open("sample.txt","r")

data=f.read()

l=data.split()

size=0
answord=""

for i in l:
    if(len(i)>size):
        size=len(i)
        answord=i

print("MAx Word : ",answord)
print("Its length : ",size)
