def solution(order):
    total = 0  
    
    for item in order:
        if "americano" in item:
            total += 4500  
        elif "cafelatte" in item:
            total += 5000  
        elif item == "anything":
            total += 4500  
     
    return total
