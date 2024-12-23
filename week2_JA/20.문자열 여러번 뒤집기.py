def solution(my_string, queries):
    # 문자열을 리스트로 변환
    s_l = list(my_string)
    
    # 각 쿼리를 순차적으로 처리
    for s, e in queries:
        s_l[s:e+1] = s_l[s:e+1][::-1]  # [s:e+1] 부분을 뒤집기
    
    # 리스트를 다시 문자열로 변환 후 반환
    return ''.join(s_l)

# 테스트
result = solution("remrgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
print(result)
