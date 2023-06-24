def fibb(n1,n2,term,next_term):
    if(term==9):
        return
    print(next_term,end=" ")
    n1=n2
    n2=next_term
    next_term=n1+n2
    return fibb(n1,n2,term,next_term)


n1=0
n2=1
next_term=n1+n2
term=0
fibb(n1,n2,term,next_term)

