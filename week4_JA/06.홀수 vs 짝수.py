def solution(num_list):
    odd = 0
    for odd_idx in range(0,len(num_list), 2): #홀수번
        odd += num_list[odd_idx]
        
    even = 0
    for even_idx in range(1,len(num_list), 2): #짝수번
        even += num_list[even_idx]
        
    if odd > even:
        return odd
    else:
        return even