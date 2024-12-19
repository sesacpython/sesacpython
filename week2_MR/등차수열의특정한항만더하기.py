def solution(a, d, included):
    li1 = [i for i in range(a, a+d*len(included), d)]
    return sum([li1[j] if included[j] else 0 for j in range(0, len(included))])