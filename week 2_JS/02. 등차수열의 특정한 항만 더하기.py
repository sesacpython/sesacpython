def solution(a, d, included):
    total = 0 
    
    for i in range(len(included)):
        if included[i] == 1:  
            total += a + i * d
    
    return total
