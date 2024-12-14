def solution(ineq, eq, n, m):
    condition = f"n {ineq}{eq if eq == '=' else ''} m" 
                #{}안에 조건식 사용가능
                #{}안에 ''가 사용된 경우 --> 밖은 ""(큰따옴표) 써줘야함
    #print(condition, type(condition)) # "n > m", str
    if eval(condition) == True:
        return 1
    else:
        return 0
    
solution(">", "!", 4, 5)