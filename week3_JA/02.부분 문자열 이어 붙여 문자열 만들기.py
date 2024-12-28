def solution(my_strings, parts):
    result = ''
    for string, (s, e) in zip(my_strings, parts):
        result += string[s:e+1]
    return result

# zip함수 --> 리스트 원소간 연산(슬라이싱)이므로
my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]

# 실행
print(solution(my_strings, parts))
