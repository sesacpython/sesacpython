def solution(n):
    answer = []
    
    for i in range(n):
        result = []
        for j in range(n):
            if i == j:
                result.append(1)
            else:
                result.append(0)
        answer.append(result)
            
    return answer
    