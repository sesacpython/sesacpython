def solution(x1, x2, x3, x4):
    a=[x1,x2,x3,x4]
    if a.count(True)==3 or a.count(True)==4:
        return True
    elif a.count(True)==1:
        return False
    elif x1==x2 or x3==x4:
        return False
    else:
        return True
        