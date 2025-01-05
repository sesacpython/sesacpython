def solution(q, r, code):
    result =""
    for i,j in enumerate(code):
        if i%q == r:
            result += j
    return result
        