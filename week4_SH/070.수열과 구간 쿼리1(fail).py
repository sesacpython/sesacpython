def solution(arr, queries):
     for i in queries:
            for j in i:
                arr[j]= arr[j]+1
        return arr
        