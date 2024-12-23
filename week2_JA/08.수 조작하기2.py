# 수 조작하기 2

def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
    
    return answer

# 예시 테스트
print(solution([0, 1, 0, 10, 0, 1, 0, 1, 0, -1, -2, -1]))  # "wsdawsdassw"
