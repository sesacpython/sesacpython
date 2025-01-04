def solution(myString):
    str1 = ''
    for s in myString:
        if s.islower():
            str1+=s.upper()
        else:
            str1+=s
    return str1