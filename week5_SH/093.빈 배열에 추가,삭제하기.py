def solution(arr, flag):
    result = []
    for index, i in enumerate(flag):
        if i ==True:
            for j in range(arr[index]*2):
                result.append(arr[index])
        elif i == False:
            for j in range(arr[index]):
                result.pop()
    return result
        