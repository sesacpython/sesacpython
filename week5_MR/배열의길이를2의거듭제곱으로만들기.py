def solution(arr):
    i = 2
    if len(arr) == 1 or len(arr) == 2:
        return arr
    while True:
        num = 2**i
        if len(arr) <= num:
            break
        i+=1
    return arr+[0 for _ in range(2**i-len(arr))]
    