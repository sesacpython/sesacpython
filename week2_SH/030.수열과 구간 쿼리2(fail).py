def solution(arr, queries):
    result=[]
    for i in range(len(queries)):
        if queries[i][2] != queries[i][1] and queries[i][2]<queries[i][1]:
            result.append(arr[arr.index(queries[i][2]+1)])
        else:
            result.append(-1)
    return result