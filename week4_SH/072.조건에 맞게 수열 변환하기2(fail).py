def solution(arr):
    num=0
    result1=[]
    result=arr
    while result1!=result:
        result1=result
        result=[]
        num += 1
        for i in result1:
            if i >= 50 and i%2==0:
                result.append(i/2)
            elif i < 50 and i%2==1:
                result.append(i*2)
            else:
                result.append(i)
    return num