import sys

def palindrome(a):
    a1=a[::-1]
    if a==a1:
        return True
    else:
        return False
    
a=input()
n=len(a)
for i1 in range(1,n-1):
    a1=a[:i1]
    if palindrome(a1):
        for j1 in range(1,n-i1-1): 
            a2=a[i1:i1+j1]
            a3=a[i1+j1:]
            if palindrome(a2) and palindrome(a3):
                print(a1)
                print(a2)
                print(a3,end='')
                sys.exit()
                
print('Impossible',end='')