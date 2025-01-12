def solution(strArr):
    long = []
    result= 0
    for i in range(30):
        long.append(0)
    for j in strArr:
        long[len(j)-1] += 1
    for index, k in enumerate(long):
        if result < k:
            result = index+1
    return result
        