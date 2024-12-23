def solution(numLog):
    result = []
    for i in range(1, len(numLog)):
        f = numLog[i] - numLog[i-1]
        if f == 1:
            result.append("w")
        elif f == -1:
            result.append("s")
        elif f == 10:
            result.append("d")
        elif f == -10:
            result.append("a")
    return ''.join(result)
