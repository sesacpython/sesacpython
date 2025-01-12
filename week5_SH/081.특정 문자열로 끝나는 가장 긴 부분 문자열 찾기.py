def solution(myString, pat):
    my = myString[::-1]
    p= pat[::-1]
    for i in range(len(my)):
        if my[i:i+len(p)] == p:
            result = my[i:]
            return result[::-1]
    