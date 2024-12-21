def solution(intStrs, k, s, l):
    result = []
    for num_str in intStrs:
        sub_str = num_str[s:s + l]
        num = int(sub_str)
        if num > k:
            result.append(num)
    return result
