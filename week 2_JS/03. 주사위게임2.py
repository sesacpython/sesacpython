def solution(a, b, c):
    if a != b and c != b and a != c:
        return a+b+c
    elif a == b and b == c:
        return (a + b + c) * (a*a + b*b + c*c ) * (a*a*a + b*b*b + c*c*c )
    else:
        return (a + b + c) * (a*a + b*b + c*c )
