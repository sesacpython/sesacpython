def solution(num_list):
    if num_list[-1] > num_list[-2]:
        a= num_list[-1] - num_list[-2]
    else:
        a=num_list[-1] *2
    num_list.append(a)
    
    return(num_list)
