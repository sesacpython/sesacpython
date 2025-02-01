def solution(date1, date2):
    date1[0], date2[0] = str(date1[0]).zfill(4),str(date2[0]).zfill(4)
    date1[1], date2[1] = str(date1[1]).zfill(2),str(date2[1]).zfill(2)
    date1[2], date2[2] = str(date1[2]).zfill(2),str(date2[2]).zfill(2)
    
    return + (''.join(date1) < ''.join(date2))