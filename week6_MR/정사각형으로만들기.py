def solution(arr):
    bool_ = len(arr) < len(arr[0])
    if bool_:
        for i in range(len(arr[0])-len(arr)):
            arr.append([0]*len(arr[0]))
    else:
        l = len(arr)-len(arr[0])
        for a in arr:
            a.extend([0]*l)
            
    return arr