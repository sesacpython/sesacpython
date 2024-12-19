def solution(n):
    answer = [n]
    
    while n != 1:
        n = int(3*n+1 if n%2 else n/2)
        answer.append(n)
        
    return answer
