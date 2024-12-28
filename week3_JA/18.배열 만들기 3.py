def solution(arr, intervals):
    arr2 = arr[intervals[0][0]:intervals[0][1]+1]
    arr3 = arr[intervals[1][0]:intervals[1][1]+1]
    return arr2 + arr3

# a1: intervals[0][0], b1: intervals[0][1]
# a2: intervals[1][0], b2: intervals[1][1]