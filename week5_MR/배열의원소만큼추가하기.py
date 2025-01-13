def solution(arr):
    answer = []
    answer.extend([a for a in arr for i in range(a)])
    return answer