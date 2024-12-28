def solution(my_string, is_suffix):
    answer =[]
    for idx, val in enumerate(my_string):
        answer.append(my_string[idx:])
    
    if is_suffix in answer:
        return 1
    else: 
        return 0