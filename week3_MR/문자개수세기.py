def solution(my_string):
    answer = [0]*52
    
    for s in my_string:
        asc = ord(s) - 65 if s.isupper() else 26 + (ord(s)-97)
        answer[asc] += 1
    
    return answer
