def solution(my_string, is_prefix):
    answer = []
    for n in range(len(my_string)):
        answer.append(my_string[:n])
    if is_prefix in answer:
        return 1
    else:
        return 0