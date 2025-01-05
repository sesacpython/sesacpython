def solution(num_list):
    odd=0
    even=0
    for i,j in enumerate(num_list):
        if (i+1)%2 == 1:
            odd +=j
        else:
            even +=j
    if odd >= even:
        return odd
    else:
        return even