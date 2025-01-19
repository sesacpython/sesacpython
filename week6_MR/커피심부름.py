def solution(order):
    return sum([4500 if 'americano' in menu or 'anything' in menu else 5000 for menu in order])