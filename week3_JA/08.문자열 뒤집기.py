def solution(my_string, s, e):    
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:] 
    #return my_string[:s]+my_string[e:s-1:-1]+my_string[e+1:]  #불가 --> 2개틀림: s가 0일때 오류