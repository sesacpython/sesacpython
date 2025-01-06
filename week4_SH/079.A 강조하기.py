def solution(myString):
    result = ""
    for i in myString:
        if i == "a":
            result += i.upper()
        elif i != 'A':
            result += i.lower()
        elif i == "A":
            result += i
    return result
        