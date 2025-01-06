def solution(arr, idx):
    result = -1
    a=arr[idx::]
    if 1 not in a:
        return -1 
    for i in a:
        if i ==1:
            result +=1
            return idx+result
        else:
            result +=1
    
        