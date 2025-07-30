def exteuclid(a, b):
    n=0
    m = b
    e = a
    q = []
    while a!=0 and b!=0:
        if a > b:
            q.append(a//b)
            a = a % b
        elif a < b:
            q.append(b//a)
            b = b % a
        n = n+1
    a = 0
    b = 1
    for x in range(n-1):
        if x%2==0:
            a = (a-b*q[x])%m
        if x%2==1:
            b = (b-a*q[x])%m
    a = int((1 - e*b)/m)
    return (a, b)
p=26513
q=32321
(a, b) = exteuclid(p,q)
print(a,b)
