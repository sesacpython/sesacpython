#인덱스 순회하며 indices와 비교
def solution(my_string, indices):
    s_lst = list(my_string)
    
    ans = ''
    for idx in range(len(my_string)):
        if idx not in indices:
            ans += my_string[idx]
        
    return ans

    