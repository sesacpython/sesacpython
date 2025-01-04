def solution(myString):
    str1 =''
    for s in myString:
        if s == 'a' or s =='A':
            str1+=s.upper()
        elif s == ' ':
            str1 += ' '
        else:
            str1+=s.lower()
    return str1