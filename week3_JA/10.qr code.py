def solution(q, r, code):
    ans = ''
    for idx, str1 in enumerate(code):
        if idx % q == r:
            ans+=str1
    return ans