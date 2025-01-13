def solution(arr, n):
    return [(arr[i]+n if i%2==0 else arr[i]) if len(arr)%2 else (arr[i]+n if i%2 else arr[i]) for i in range(len(arr))]