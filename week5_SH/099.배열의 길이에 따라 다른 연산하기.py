def solution(arr, n):
    result = []
    if len(arr)%2 ==1:
        for i,j in enumerate(arr):
            if i%2==0:
                result.append(j+n)
            else:
                result.append(j)
    else: 
         for i, j in enumerate(arr):
                if i%2==1:
                    result.append(j+n)
                else:
                    result.append(j)
    return result