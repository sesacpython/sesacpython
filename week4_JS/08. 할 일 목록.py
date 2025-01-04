def solution(todo_list, finished):
    unfinished = []
      for i in range(len(todo_list)):
        if not finished[i]:
            unfinished.append(todo_list[i])
    return unfinished
