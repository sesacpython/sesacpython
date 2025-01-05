def solution(n, k):
    result=[]
    for i in range(1,n+1):
        if  k <= i <= n and i%k == 0 :
            result.append(i)
    return result