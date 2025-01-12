def solution(arr, k):
    a=list(set(arr))
    if len(a)>= k:
        return a[:k]
    else:
        for i in range(k-len(a)):
            a.append(-1)
        return a