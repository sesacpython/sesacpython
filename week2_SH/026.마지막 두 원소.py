def solution(num_list):
    a=len(num_list)
    b=num_list
    if b[a-1] > b[a-2]:
        b.append(b[a-1]-b[a-2])
        return b
    else:
        b.append(b[a-1]*2)
        return b