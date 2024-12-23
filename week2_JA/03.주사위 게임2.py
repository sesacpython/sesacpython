# 주사위게임2
def solution(a, b, c):
    #if a != b != c: # 틀린 코드: 만약 a와 c가 같은 경우라도 b와 다르면 이 조건이 통과될 수 있음
    if a != b and b != c and a != c:
        return a + b + c
    elif a==b and b==c and a==c:
        return (a + b + c) * (a**2 + b**2 + c**2)* (a**3 + b**3 + c**3)
    elif (a==b or b==c or c==a):
    #else:
        return (a + b + c) * (a**2 + b**2 + c**2)

#a b c 1 2 3
#a a c 1 1 2
#a a a 1 1 1
#b c c 2 3 3

solution(4, 4, 4)