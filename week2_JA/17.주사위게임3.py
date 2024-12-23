def solution(a, b, c, d):
    # 주사위 숫자들을 리스트에 저장
    dice = [a, b, c, d]
    
    # 숫자들의 빈도수를 확인
    counter = {}
    for num in dice:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    # Case 1: 네 숫자가 모두 같을 경우
    if len(counter) == 1:
        return 1111 * a
    
    # Case 2: 세 숫자가 같고, 하나가 다를 경우
    if len(counter) == 2 and 3 in counter.values():
        for k, v in counter.items():
            if v == 3:
                p = k
            else:
                q = k
        return (10 * p + q) ** 2
    
    # Case 3: 두 숫자가 두 쌍으로 나올 경우
    if len(counter) == 2 and 2 in counter.values():
        keys = list(counter.keys())
        p, q = keys[0], keys[1]
        return (p + q) * abs(p - q)
    
    # Case 4: 두 숫자만 같고, 나머지 두 숫자는 서로 다를 경우
    if len(counter) == 3:
        for k, v in counter.items():
            if v == 2:
                p = k
            else:
                if 'q' not in locals():
                    q = k
                else:
                    r = k
        return q * r
    
    # Case 5: 네 숫자가 모두 다를 경우
    return min(dice)

# 예시 테스트
print(solution(2, 2, 2, 2))  # 2222
print(solution(4, 1, 4, 4))  # 1681
print(solution(6, 3, 3, 6))  # 27
print(solution(6, 4, 2, 5))  # 2
