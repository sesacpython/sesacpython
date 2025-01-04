def solution(myString):
    str1=''
    for s in myString:
        if s.isupper():
            str1+=s.lower()
        else:
            str1+=s
    return str1