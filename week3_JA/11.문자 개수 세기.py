def solution(my_string):
    lst = [0] * 52
    apb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for idx, val in enumerate(my_string):
        for i, v in enumerate(apb):
            if val == v:
                lst[i] +=1
    return lst
