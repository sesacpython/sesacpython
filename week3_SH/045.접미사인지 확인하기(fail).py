def solution(my_string, is_suffix):
    my_string= my_string[-1::-1]
    result=''
    word=[]
    for i in my_string:
        result.extend += i
        word.append(result)
    if is_suffix in word:
        return 1
    else:
        return 0