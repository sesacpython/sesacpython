def solution(str1,str2):
    result = ''
    a=len(str1)
    for i in range(a):
            result += str1[i]
            result += str2[i]
    return result