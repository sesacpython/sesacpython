def solution(num_list):
    
    gob = 1
    sum1 = 0
    for num in num_list:
        gob *= num
        sum1 += num
    sum2 = sum1**2
    
    if gob < sum2:
        return 1
    else:
        return 0
        