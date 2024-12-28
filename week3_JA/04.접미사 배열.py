def solution(my_string):
    answer = []
    for idx, val in enumerate(my_string):
        answer.append(my_string[idx:])
    return sorted(answer)