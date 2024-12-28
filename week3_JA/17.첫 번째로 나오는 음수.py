def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1 # if문 내부에서 return 값을 반환하지 못하면 단순히 여기 return 값 반환
