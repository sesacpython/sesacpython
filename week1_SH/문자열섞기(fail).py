def solution(str1,str2):
    result = []
    a= len(str1)
    for i in range(a+1):
        result.extend(str1[i])
        result.extend(str2[i])
        return result*a