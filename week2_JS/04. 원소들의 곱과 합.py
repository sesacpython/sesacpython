def solution(num_list):
    result = 1 
    result2 = 0 
    
    for i in num_list:
        result *= i
    for i in num_list:
        result2 += i
    
    if result < result2 * result2:
        return 1
    else:
        return 0
