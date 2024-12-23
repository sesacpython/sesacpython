def solution(n, control):
    for v in control:
        if v == 'w':
            n += 1
        elif v == 's':
            n -= 1
        elif v == 'd':
            n += 10
        elif v == 'a':
            n -= 10
    return n
