l=["sec","pen","penin","ball","seeegc"]

s=set(l)
d={}
for i in s:
    count=0
    pre=i[0]
    suff=i[len(i)-1]
    for j in l:
        if(j[0]==pre and j[len(j)-1]==suff):
            count=count+1

    presuf=pre+suff
    d.update({presuf:count})
print(d)
