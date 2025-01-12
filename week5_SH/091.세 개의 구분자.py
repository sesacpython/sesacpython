def solution(myStr):
    a=myStr.replace('a', ' ')
    b=a.replace('b', ' ')
    c=b.replace('c', ' ')
    if c.split() == []:
        return ["EMPTY"]
    else:
        return c.split()
        
    