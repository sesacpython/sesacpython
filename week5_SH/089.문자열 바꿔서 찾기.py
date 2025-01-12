def solution(myString, pat):
    a=myString.replace('A', 'b')
    b=a.replace('B', 'a')
    if pat in b.upper():
        return 1
    else:
        return 0
