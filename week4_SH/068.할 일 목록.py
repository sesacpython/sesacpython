def solution(todo_list, finished):
    result= []
    for i,j in enumerate(todo_list):
        if finished[i] == 0:
            result.append(j)
    return result