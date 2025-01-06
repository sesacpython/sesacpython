def solution(my_string, indices):
    result=""
    indices.sort()
    for i,j in enumerate(my_string):
        if i not in indices:
            result += j
    return result
