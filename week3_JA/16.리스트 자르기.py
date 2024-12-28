def solution(n, slicer, num_list):
    if n ==1:
       return num_list[0:slicer[1]+1]
    elif n ==2:
        return num_list[slicer[0]:]
    elif n ==3:
        return num_list[slicer[0]:slicer[1]+1]    
    elif n ==4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]        
        
# slicer[0] : a
# slicer[1] : b
# slicer[2] : c