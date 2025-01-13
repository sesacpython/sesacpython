def solution(number):
    total_sum = sum(int(digit) for digit in number)
    return total_sum % 9
