def solution(strArr):
    return [strArr[i].lower() if (i+1)%2 else strArr[i].upper() for i in range(len(strArr))]