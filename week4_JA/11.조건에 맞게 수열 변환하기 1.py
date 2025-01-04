def solution(arr):
    
    arr2 = []
    for a in arr:
        if a >= 50 and a %2 ==0:
            arr2.append(a / 2)
        elif a < 50 and a % 2 !=0:
            arr2.append(a * 2)
        else:
            arr2.append(a)
    return arr2