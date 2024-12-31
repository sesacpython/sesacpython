def solution(my_strings, parts):
    result=''
    for i,j in enumerate(my_strings):
        result += j[parts[i][0]:parts[i][1]+1]
    return result