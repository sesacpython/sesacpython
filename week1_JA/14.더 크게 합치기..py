def solution(a, b):
    if str(a)+str(b) < str(b)+str(a):
        return int(str(b)+str(a))
    else:
        return int(str(a)+str(b))