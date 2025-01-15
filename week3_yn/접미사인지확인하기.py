def solution(my_string, is_suffix):
    if my_string[-1*(len(is_suffix)):] == is_suffix:
        return 1
    else: 
        return 0
