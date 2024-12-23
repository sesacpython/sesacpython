def solution(arr, q):
    answer = []
    
    for s, e, k in q:
        # s부터 e까지의 부분 배열 추출
        arr2 = arr[s:e+1]
        
        # k보다 큰 값들 필터링
        filtered = [x for x in arr2 if x > k]
        
        # 필터링된 값 중 최소값 찾기
        if filtered:
            answer.append(min(filtered))
        else:
            answer.append(-1)
    
    return answer


arr = [0, 1, 2, 4, 3]
qu = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]
print(solution(arr, q))  # 출력: [3, 4, -1]
