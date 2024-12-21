#수정중
arr = [0, 1, 2, 4, 3]
queries=[[0, 4, 1],[0, 3, 2],[0, 3, 3]]

def solution(arr,queries):
    for i in queries:
        s,e,k = i
        for j in arr[s,e+1]:
            if j % k ==0:
                arr[j] = arr[j]+1
                
    return arr
