str1 = input() #"aBcDeFg

new_str = ''
for idx in range(len(str1)):
    if str1[idx].islower():
        #str1[idx].upper() #str1에 바로 반영X
        #str1[idx] = str1[idx].upper() # 문자열은 특정 위치를 직접 수정하는 것 불가
        new_str += str1[idx].upper()
    elif str1[idx].isupper():
        #str1[idx] = str1[idx].lower()
        new_str += str1[idx].lower()
        
print(new_str)