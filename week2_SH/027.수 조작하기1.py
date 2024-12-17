def solution(n, control):
    a=n
    for i in control:
        if i =='w':
            a += 1
        elif i == 's':
            a -= 1
        elif i == 'd':
            a += 10
        else:
            a -= 10
    return a