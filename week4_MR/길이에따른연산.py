def solution(num_list):
    return eval('*'.join([str(n) for n in num_list])) if len(num_list) < 11 else sum(num_list)