def solution(myString, pat):
    str1 = myString.lower()
    pat1 = pat.lower()
    if pat1 in str1:
        return 1
    else:
        return 0