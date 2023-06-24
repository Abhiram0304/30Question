def power(b,p):
    if(p==0):
        return 1
    
    if(p%2==0):
        return (b**(p//2) * b**(p//2))
    else:
        return(b * b**(p//2) * b**(p//2))

print(power(5,99))

