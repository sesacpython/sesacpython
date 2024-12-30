def solution(arr, intervals):
    iv_arr = arr[intervals[0][0]:intervals[0][1]+1]
    iv_arr.extend(arr[intervals[1][0]:intervals[1][1]+1])
    return iv_arr
