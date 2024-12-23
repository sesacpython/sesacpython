def solution(q, r, code):
    return ''.join([code[i] if i%q == r else '' for i, c in enumerate(code)])
