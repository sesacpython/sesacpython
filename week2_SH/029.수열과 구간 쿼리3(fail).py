def solution(arr, queries):
    a=len(queries)
    for i in range(a):
        arr[queries[i][0]]=arr[queries[i][1]]
        arr[queries[i][1]]=arr[queries[i][0]]
    return arr