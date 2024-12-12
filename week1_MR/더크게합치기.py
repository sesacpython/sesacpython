def solution(a, b):
    return int(str(a)+str(b)) if int(str(b)+str(a)) < int(str(a)+str(b)) else int(str(b)+str(a))
