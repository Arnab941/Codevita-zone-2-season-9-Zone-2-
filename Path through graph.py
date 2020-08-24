def largest(a):
    s=int(a**(1/2))+1
    if a==2:
        return 1
    for i1 in range(2,s):
        if a%i1==0:
            return (a//i1)  
    return 1

def path(a,b):
    if a==b:
        return 0
    else:
        if b>a:
            a,b=b,a
        a=largest(a)
        return (1+path(a,b))

a,b=map(int,input().split())
m=path(a,b)
print(m,end='')
