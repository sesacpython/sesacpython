def solution(myStr):
    a_part = myStr.split('a')
    result = []
    for part_a in a_part:
        b_part = part_a.split('b')
        for part_b in b_part:
            c_part = part_b.split('c')
            for part_c in c_part:
                if part_c:
                    result.append(part_c)
    return result if result else ["EMPTY"]
