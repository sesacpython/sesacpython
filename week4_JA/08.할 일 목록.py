def solution(todo_list, finished):
    res =[]
    for todo, fin in zip(todo_list,finished):
        if fin == bool(False):
            res.append(todo)
    return res
        