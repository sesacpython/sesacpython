def solution(intStrs, k, s, l):
    lst =[]
    for str1 in intStrs:
        if int(str1[s:s+l])  > k: # str1의 길이: s+l-s
            lst.append(int(str1[s:s+l]))
        else:
            pass
    return lst
    