def solution(n_str):
    answer = ''
    list = 0
    for i in n_str:
        if i != '0':
            list = 1
            answer += i
        elif list:
            answer += i
    return answer
