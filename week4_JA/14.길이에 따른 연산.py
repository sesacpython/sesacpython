def solution(num_list):
    n=0
    n1=1
    for num in num_list:
        if len(num_list) >=11:
            n+=num    
        elif len(num_list) <=10:
            n1*=num            
    if n > 0:
        return n
    elif n1 > 1:
        return n1