def solution(ineq, eq, n, m):
    return +eval(f'{n}{ineq+eq if eq!="!" else ineq}{m}')
