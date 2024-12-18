def solution(arr, queries):
    for j in range(len(queries)):
        for i in range(queries[j][1]-queries[j][0]+1):
            if  (queries[j][0]+i)%queries[j][2]==0 and (queries[j][0]+i)<=queries[j][1]:
                arr[queries[j][0]+i] += 1
                
    return arr