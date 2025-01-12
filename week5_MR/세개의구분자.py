def solution(myStr):
    answer = ''.join([s if s not in 'abc' else ' ' for s in myStr])
    return answer.split() or ["EMPTY"]