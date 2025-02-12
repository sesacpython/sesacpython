def solution(participant, completion):
    
    participant_dict = {}
    
   
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1  
        else:
            participant_dict[name] = 1   
            
 
    for name in completion:
        participant_dict[name] -= 1
    

    for name, count in participant_dict.items():
        if count > 0:
            return name
