def solution(str_list):
    for s in str_list:
        if s == "l" :
            return str_list[:str_list.index('l')]
        elif s == 'r':
            return str_list[str_list.index('r')+1:]
    return []