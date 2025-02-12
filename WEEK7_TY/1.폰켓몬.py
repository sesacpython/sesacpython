def solution(nums):
   
    type_count = {}  

    
    for num in nums:
        if num in type_count:
            type_count[num] += 1
        else:
            type_count[num] = 1

  
    unique_types = len(type_count)

    
    allowed_selection = len(nums) // 2

    
    #    유일한 종류의 수와 가져갈 수 있는 총 개수 중 작은 값입니다.
    return min(unique_types, allowed_selection)
