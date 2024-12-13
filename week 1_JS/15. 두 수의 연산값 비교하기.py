def solution(a, b):
    ab = int(str(a) + str(b))
    cd = int(str(2*a*b))

    if ab >= cd :
        return int(ab)
    else:
        return int(cd)
