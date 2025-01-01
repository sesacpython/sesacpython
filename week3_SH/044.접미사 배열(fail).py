def solution(my_string):
    result=[]
    a=len(my_string)
    for i in a:
        result.append(my_string[-1:i:-1])
    result.sort()
    return result
             