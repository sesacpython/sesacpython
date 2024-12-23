def solution(code):
    ret = ''
    mode = 0
    
    for idx, ch in enumerate(code):
        if mode == 0:
            if ch == '1':
                mode = 1
            elif idx % 2 == 0:
                ret += ch
        else:
            if ch == '1':
                mode = 0
            elif idx % 2 == 1:
                ret += ch
    
    return ret if ret else 'EMPTY'

# 예시 테스트
print(solution("abc1abc1abc"))  # "acbac"
print(solution("1a1b1c"))       # "EMPTY"
