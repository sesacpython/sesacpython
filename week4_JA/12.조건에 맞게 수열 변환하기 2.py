def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        
        old = new  # 새로운 상태로 업데이트
        answer += 1  # 반복 횟수 증가 (조건과 상관없이)
    
    return answer