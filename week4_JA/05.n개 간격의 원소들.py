def solution(num_list, n):
    lst =[]
    for idx in range(0,len(num_list),n):
        lst.append(num_list[idx])
    return lst