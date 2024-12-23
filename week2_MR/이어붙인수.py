def solution(num_list):    
    return int(''.join([str(i) if i%2 else '' for i in num_list]))+int(''.join([str(j) if not(j%2) else '' for j in num_list]))
