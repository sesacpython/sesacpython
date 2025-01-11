def solution(myString):
    return sorted([nonx for nonx in myString.split("x") if nonx])
