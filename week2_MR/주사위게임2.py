def solution(a, b, c):
    if a==b==c:
        return (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)
    elif a-b == 0 or b-c==0 or a-c==0:
        return (a+b+c) * (a**2+b**2+c**2)
    else:
        return a+b+c