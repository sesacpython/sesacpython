# 배열 만들기 4
def solution(arr):
    i = 0
    stk =[]
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            #stk.remove(stk[-1]) # 리스트의 전체를 순회하여 해당 값을 찾아 제거, 시간복잡도가 o(n)
            stk.pop()  # remove 대신 pop 사용
    return stk

solution([1, 4, 2, 5, 3])