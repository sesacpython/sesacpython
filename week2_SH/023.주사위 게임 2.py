def solution(a, b, c):
    if a ==b and a == c and b == c:
        d = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b and a != c and b != c:
        d = a+b+c
    else:
        d=(a+b+c)*(a**2+b**2+c**2)
    return d