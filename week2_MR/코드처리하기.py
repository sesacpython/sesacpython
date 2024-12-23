def solution(code):
    mode, ret = 0, ""

    for idx in range(0, len(code)):
        if code[idx] == "1":
            mode = +(not mode)   
        else:
            if idx % 2 == mode: ret += code[idx]

    return ret or "EMPTY"
