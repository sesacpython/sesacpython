def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        temp = ''.join([p*k  for p in picture[i]])
        for _ in range(k):
            answer.append(temp)
        
    return answer