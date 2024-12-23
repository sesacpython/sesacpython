def solution(arr, q):
    for s, e, k in q:
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
    return arr
