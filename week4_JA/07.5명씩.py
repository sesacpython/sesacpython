def solution(names):
    ans = []
    for fst_idx in range(0,len(names), 5):
        ans.append(names[fst_idx])
    return ans