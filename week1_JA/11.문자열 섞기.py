def solution(str1, str2):
    a_lst = []
    for i in str1:
        a_lst += i
        
    b_lst = []
    for s in str2:
        b_lst += s
        
    c_lst = list(zip(a_lst, b_lst))
    
    d_lst=[]
    for a, b in c_lst:
        d_lst += a, b
    return ''.join(d_lst)


solution("aaaaa", "bbbbb")