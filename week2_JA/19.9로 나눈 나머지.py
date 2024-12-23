def solution(number):
    
    sum1 = 0
    for num in number:
        #print(num)
        sum1 += int(num)
    return sum1 % 9
