def solution(arr, queries):
    for i in queries:
        for i in range(i[0],i[1]+1):
            arr[i] +=1
    return arr
        