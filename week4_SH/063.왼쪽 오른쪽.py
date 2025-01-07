def solution(str_list):
    for j,i in enumerate(str_list):
        if j==0 and i =="l":
            return []
        elif j== len(str_list)-1 and i=="r":
            return []
        elif i == "l":
            return str_list[:j]
        elif i =="r":
            return str_list[j+1:]
        elif str_list == []:
            return []
        elif "l" not in str_list and "r" not in str_list:
            return []