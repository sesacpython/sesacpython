def solution(n, k):
    
    lst = []
    for i in range(1, n+1):
        if i % k ==0:
            lst.append(i)
    return lst