def solution(s, e):
    lst = []
    for x in range(e,s+1):
        lst.append(x)
    return lst[::-1]