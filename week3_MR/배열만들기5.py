def solution(intStrs, k, s, l):
    return list(filter(lambda x: k<x, [int(st[s:s+l]) for st in intStrs]))
