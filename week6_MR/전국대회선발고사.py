def solution(rank, attendance):
    arr = []
    i = 1
    while len(arr)<3:
        if attendance[rank.index(i)]: 
            arr.append(rank.index(i))
        i+=1
    return 10000*arr[0]+100*arr[1]+arr[2]