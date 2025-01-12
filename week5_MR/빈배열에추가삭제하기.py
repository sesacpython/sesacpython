def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            if flag[i]:
                answer.extend([arr[i], arr[i]])
            else:
                if answer: answer.pop()  
    return answer