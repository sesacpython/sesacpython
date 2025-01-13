def solution(strArr):
    dic = {}
    for s in strArr:
        if str(len(s)) in dic.keys():  dic[str(len(s))].append(s)
        else: dic[str(len(s))] = [s]
    return max([len(s) for s in dic.values()])