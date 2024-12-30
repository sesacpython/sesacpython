def solution(my_string, is_suffix):
    return +(is_suffix in my_string and is_suffix[-1]==my_string[-1])
