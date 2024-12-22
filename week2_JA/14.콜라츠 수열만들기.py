# 콜라츠 수열
def solution(n):
    n_lst =[]
    n_lst.append(n)
    
    while n !=1:
        if n % 2== 0:
           n = n // 2
           n_lst.append(n)
        else:
            n = 3 * n +1
            n_lst.append(n) 
    return n_lst

solution(10)
