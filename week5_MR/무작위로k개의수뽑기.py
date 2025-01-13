def solution(arr, k):
    return list(dict.fromkeys(arr))[:k] if len(list(dict.fromkeys(arr))) >= k else list(dict.fromkeys(arr)) + [-1 for _ in range(k-len(list(dict.fromkeys(arr))))]