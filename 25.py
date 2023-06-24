def palindrome(s):
    
    rev=s[-1:-(len(s)+1):-1]
    if(s==rev):
        return True
    else:
        return False

f=open("str.txt","r")
data=f.read()
l=data.split(" ")

print(l)
count=0
for i in l:
    if(palindrome(i)):
        count=count+1
print(count)

