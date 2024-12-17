def solution(numLog):
    a=''
    b=len(numLog)
    for idx, i in enumerate(numLog):
        if idx+1 ==b:
            return a
        elif numLog[idx+1]-numLog[idx] == 1:
            a += 'w'
        elif numLog[idx+1]-numLog[idx] == -1:
            a += 's'
        elif numLog[idx+1]-numLog[idx] == 10:
            a += 'd'
        else:
            a += 'a'