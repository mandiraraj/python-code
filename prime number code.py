import math
def prime(n):
    if n==2:
        return True
    
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
            break
    else:

        return True
def get(n):
    l=[]
    for i in range(2,n):
        if prime(i)==True:
            l.append(i)
    return l,len(l)
n=int(input('enter a no'))
print(get(n))
            
    
