def solution(my_string, alp):
    str1 = ''
    for s in my_string:
        if s == alp:
            str1+=s.upper()
        else:
            str1+=s
    return str1