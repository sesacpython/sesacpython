def solution(arr):
    answer = 0
    arr2 = []
    
    while arr != arr2:
        arr2 = arr
        arr = [int(a/2)+1 if a >= 50 and a %2 == 0 else (a*2+1 if a<50 and a%2 else a) for a in arr]
        answer += 1
        
    return answer-1