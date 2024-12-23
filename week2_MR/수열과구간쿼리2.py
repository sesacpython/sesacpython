def solution(arr, queries):
    answer = []
    
    for q in queries:
        result = sorted(arr[q[0]:q[1]+1])
        num_list = list(filter(lambda n: n>q[2], result))
        answer.append(num_list[0] if num_list else -1) 
        
    return answer
