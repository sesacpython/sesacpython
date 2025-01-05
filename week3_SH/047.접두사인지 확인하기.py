def solution(my_string, is_prefix):
    result=''
    word=[]
    for i in my_string:
        result += i
        word.append(result)
    if is_prefix in word:
        return 1
    else:
        return 0