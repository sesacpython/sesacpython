#a 2배//  가로2배=aa가 2줄(세로2배) 
def solution(picture, k):
    result = []
    
    for i in picture:
        garo = ""  
        
        for char in i:
            garo += char * k
        
        for i in range(k):
            result.append(garo)
    
    return result
