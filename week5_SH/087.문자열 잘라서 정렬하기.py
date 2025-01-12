def solution(myString):
    return list([i for i in myString.replace('x', ' ').split()].sort())

    