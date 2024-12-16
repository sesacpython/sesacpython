def solution(a, b):
    stra =str(a)
    strb =str(b)
    A=stra+strb
    INTA=int(A)
    if INTA >= 2*a*b:
        return INTA
    else:
        return 2*a*b