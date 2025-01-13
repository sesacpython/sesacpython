def solution(arr):
    number = 1
    while number < len(arr):
        number *= 2
    number_add = number - len(arr)
    answer = arr + [0] * number_add 
    return answer
