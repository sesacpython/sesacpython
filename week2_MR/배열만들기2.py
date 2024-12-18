def ex_func(n):
    ex_str = '12346789'
    return ('0' in str(n) or '5' in str(n)) and len(list(filter(lambda x: x in str(n), ex_str))) == 0

def solution(l, r):
    x_list = list(filter(ex_func, range(l, r+1)))
    return sorted(x_list) if x_list else [-1]
