def solution(arr):
    i=len(arr)
    if  i==3:
        arr.append(0)
    elif 4 < i <8:
        while len(arr) !=8:
            arr.append(0)
    elif 8 < i <16:
        while len(arr) !=16:
            arr.append(0)
    elif 16 < i <32:
        while len(arr) !=32:
            arr.append(0)
    elif 32 < i <64:
        while len(arr) !=64:
            arr.append(0)
    elif 64 < i <128:
        while len(arr) !=128:
            arr.append(0)
    elif 128 < i <256:
        while len(arr) !=256:
            arr.append(0)
    elif 256 < i <512:
        while len(arr) !=512:
            arr.append(0)
    elif 512 < i <1024:
        while len(arr) !=1024:
            arr.append(0)
    return arr
