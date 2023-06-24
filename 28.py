f=open("input_string.txt","r")

k=4

# word="abcd"
# rev=""
# for i in range(2,-1,-1):
#     print(word[i],end="")

word=f.read()
size=len(word)

for i in range(1,5):
    end=i-1
    before=""
    for i in range(end,-1,-1):
        before=before+word[i]
    after=word[end+1:len(word)]
    word=before+after
    # print(word)

print(word)