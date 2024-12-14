def solution(n):
    odd2=0
    even2=0
    if n %2 != 0:
        for odd in range(1, n+1, 2):
            odd2 += odd
        return odd2
    else:
        for even in range(2, n+1, 2):
            even2 += even*even
        return even2
        