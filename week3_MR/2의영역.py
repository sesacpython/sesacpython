def solution(arr):
    try:
        first = arr.index(2)
    except:
        return [-1]
    last = len(arr)-arr[::-1].index(2)
    return arr[first:last]
