def solution(names):
    leaders = []
    for i in range(0, len(names), 5):
        leaders.append(names[i])
    return leaders
