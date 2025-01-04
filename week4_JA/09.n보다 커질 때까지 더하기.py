def solution(numbers, n):
    sum1 = 0
    for num in numbers:
        sum1 += num
        if sum1 > n:
            return sum1