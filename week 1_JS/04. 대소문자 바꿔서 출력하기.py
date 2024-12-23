def solution(str):
    result = ''
    for char in str:
        if char.islower():
            result += char.upper()
        else:  # 문자가 대문자라면
            result += char.lower()
    return result
