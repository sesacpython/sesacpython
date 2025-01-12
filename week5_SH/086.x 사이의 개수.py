def solution(myString):
    a=myString.replace("x", " ")
    b=a.split(' ')
    return [len(i) for i in b]