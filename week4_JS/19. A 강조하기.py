def solution(myString):
    result = ""
    for index in myString.lower():
        if index == 'a':
            result += 'A'
        else:
            result += index
    return result
