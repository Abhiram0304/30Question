password="nitap@1234"
sc=["_","@","#",".","$","&",";","*"]
check=True

#I
if(len(password)<8 and len(password)>12):
    check=False

#II
if(password[0] in sc):
    check=False

#III
cap=0
dig=0
sma=0

for i in password:
    if(i.isdigit()):
        dig=dig+1
    if(ord(i)>=65 and ord(i)<=90):
        cap=cap+1
    
    if(ord(i)>=97 and ord(i)<=122):
        sma=sma+1

if(dig<1 or sma<1 or cap<1):
    check=False

#IV
char=0
for i in sc:
    if(i in password):
        char=char+1

if(char<1):
    check=False

if(check==True):
    print("Valid Password")
else:
    print("INvalid password")