def solution(strArr):
    result=[]
    for i,j in enumerate(strArr):
        if i%2==1:
            result.append(j.upper())
        else:
            result.append(j.lower())
    return result
            
            