def solution(rank, attendance):
    possible_students = []
    for i in range(len(rank)):
        if attendance[i]:
            possible_students.append((rank[i], i))
    possible_students.sort()
    
    a = possible_students[0][1]
    b = possible_students[1][1]
    c = possible_students[2][1]
    return 10000 * a + 100 * b + c
