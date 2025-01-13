def solution(myString, pat):
    dic = myString.maketrans('AB', 'BA')
    return +(pat in myString.translate(dic))