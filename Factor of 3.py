def new_array(a):
    b=[0]*3
    for i in a:
        b[i%3]+=1
    return b


t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=new_array(a)
    if a[0]>0:
        if a[0]<=(a[1]+a[2]+1):
            print('Yes')
        else:
            print('No')
    else:
        if a[1]==0 or a[2]==0:
            print('Yes')
        else:
            print('No')