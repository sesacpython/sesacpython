def solution(my_string):
    result=[]
    abc=[]
    defg="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for k in range(52):
        abc.append(0)
    for i in defg:
        result.append(i)
    for j in my_string:
            a=result.index(j)
            abc[a] +=1
    return abc