def solution(arr, q):
    for i, j in q:
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# 예시
print(solution([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]]))
