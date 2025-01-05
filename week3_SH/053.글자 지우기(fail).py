def solution(my_string, indices):
    result=[]
    for i in my_string:
        result.append(i)
    for i in indices:
         result.pop(indices)
    return result
    