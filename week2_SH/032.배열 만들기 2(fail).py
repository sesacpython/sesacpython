def solution(l, r):
    a=l
    b=r
    c=1
    d=1
    while a >= 10:
        a =  a//10
        c += 1
    while b >= 10:
        b = b //10
        d += 1
    return a