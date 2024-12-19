def solution(a, b, c, d):
    li = [0 for i in range(10)]
    
    for i in [a, b, c, d]:
        li[i] += 1
        
    if li.count(4):
        return li.index(4) * 1111
    if li.count(3):
        return (10*li.index(3)+li.index(1))**2
    if li.count(2)==2:
        s = list(set([a,b,c,d]))
        return sum(s) * abs(s[0]-s[1])
    if li.count(2)==1:
        arr = list(filter(lambda x: x>-1, [i if e==1 else -1 for i, e in enumerate(li)]))
        return arr[0]*arr[1]
    if li.count(1):
        return min(set([a,b,c,d]))
