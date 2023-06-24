

roll=9
s=""
while(roll>0):
    ld=roll%2
    s=s+str(ld)
    roll=roll//2

binary=s[-1:-(len(s)+1):-1]

rev=binary[-1:-(len(binary)+1):-1]

if(binary==rev):
    print("Palindrome")
else:
    print("Not Palindrome")