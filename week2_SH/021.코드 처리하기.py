def solution(code):
    mode=0
    ret=''
    a=len(code)
    for idx in range(a):
        if mode ==0:
            if code[idx]!='1' and idx%2==0:
                ret += code[idx]
            elif code[idx] =='1':
                mode = 1
        elif mode ==1:
            if code[idx]!='1' and idx%2==1:
                ret += code[idx]
            elif code[idx]=='1':
                mode =0
    
    if ret == '':
        return 'EMPTY'
    else:
        return ret