def solution(a, d, included):
    e=0
    for i in range(len(included)):
        if included[i] is True:
            c= a+d*(i)
            e += c
    return e