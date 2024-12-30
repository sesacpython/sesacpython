def solution(arr, idx):
    return ''.join([str(a) for a in arr]).find('1', idx, )
