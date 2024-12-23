
def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        valid = True
        for char in str(i):
            if char == '0' or char == '5':
                continue
            else:
                valid = False
                break
        if valid:
            answer.append(i)
    
    return answer if answer else [-1]
