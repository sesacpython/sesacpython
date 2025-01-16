def solution(num_str):
    total = 0
    for digit in num_str:
        total += int(digit)
    return total
