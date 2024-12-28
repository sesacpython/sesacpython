def solution(s, m, c):
    # 문자열을 m개씩 나누기
    lst = [s[i:i+m] for i in range(0, len(s), m)] # m개씩 건너뛰기
    
    # 각 부분에서 c번째 문자 추출
    ans = ''.join(row[c-1] for row in lst if len(row) >= c)
    
    return ans
