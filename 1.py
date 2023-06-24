# n=int(input())
l=[1,2,3,4,5,6,7,8,9,10]

# for i in range(0,n):
#     e=int(input())
#     l.append(e)

odd=0
even=0

for i in l:
    if(i%2==0):
        even=even+1
    else:
        # odd+=1
        odd=odd+1

print("even: ",even)
print("odd: ",odd)