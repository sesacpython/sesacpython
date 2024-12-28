def solution(arr):
    if 2 not in arr:  # 2가 없으면 -1 반환
        return [-1]
    
    # 첫 번째 2의 인덱스
    start = arr.index(2)
    
    # 마지막 2의 인덱스
    end = len(arr) - 1
    while arr[end] != 2:
        end -= 1
    
    # 2가 하나만 있을 경우
    if start == end:
        return [arr[start]]
    
    # 2가 여러 개 있을 경우
    return arr[start:end+1]
