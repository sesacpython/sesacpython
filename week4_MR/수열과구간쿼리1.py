def solution(arr, queries):
    for q in queries:
        arr =[arr[i]+1 if q[0]<=i<=q[1] else arr[i] for i in range(len(arr)) ]
    return arr