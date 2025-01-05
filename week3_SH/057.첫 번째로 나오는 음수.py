def solution(num_list):
    result=[]
    for i in num_list:
        if i < 0:
            result.append(num_list.index(i))
            return result[0]
    if result == []:
        return -1
            