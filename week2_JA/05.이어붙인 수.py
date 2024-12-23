def solution(num_lst):
    even = []
    odd = []
    for num in num_lst:
        if num %2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
            
    return int(''.join(even)) + int(''.join(odd))