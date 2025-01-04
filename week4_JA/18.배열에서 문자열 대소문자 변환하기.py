def solution(strArr):
    lst =[]
    for i, s in enumerate(strArr):
        if i % 2 ==0:
            lst.append(s.lower())
        else:
            lst.append(s.upper())
    return lst