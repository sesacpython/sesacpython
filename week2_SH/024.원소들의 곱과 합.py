
def solution(num_list):
    result1 = 0
    result2 = 1
    for i in num_list:
        result1 += i
    for i in num_list:
        result2 *= i       
    if result2 < result1**2:
        return 1
    else:
        return 0