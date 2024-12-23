# 등차수열

def solution(a, d, included):
    
    # n=0, 1차항
    dc = []
    sum_ = 0
    for n in range(len(included)):
        dc.append(a + d*n)
    for idx, cl in enumerate(included):
        if cl == True:
           sum_ += dc[idx] 
    
    return sum_
