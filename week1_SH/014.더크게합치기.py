def solution(a, b):
    stra =str(a)
    strb =str(b)
    A=stra+strb 
    B=strb+stra
    INTA=int(A)
    INTB=int(B)
    if INTA >= INTB:
        return INTA
    else:
        return INTB