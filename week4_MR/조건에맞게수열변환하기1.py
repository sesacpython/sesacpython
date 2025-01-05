def solution(arr):
    return [int(n/2) if n>=50 and n%2==0 else n*2 if n<50 and n%2  else n for n in arr]