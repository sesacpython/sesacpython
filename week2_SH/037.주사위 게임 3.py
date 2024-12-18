def solution(a, b, c, d):
    dice=[a,b,c,d]
    dice.sort()
    dice_many=set(dice)
    if len(dice_many)== 1 :
        return a*1111
    elif len(dice_many)==2:
        if dice[0] == dice[2] == dice[1]:
            return (dice[2]*10+dice[3])**2
        elif dice[3] == dice[1] ==dice[2]:
            return(10*dice[3]+dice[0])**2
        elif dice[1] != dice[2]:
            if (dice[1]-dice[2]) >0:
                return (dice[1]+dice[2])*(dice[1]-dice[2])
            else:
                return (dice[1]+dice[2])*(dice[2]-dice[1])
    elif len(dice_many) == 3:
        if dice[0] == dice[1]:
            return dice[2]*dice[3]
        elif dice[1] == dice[2]:
            return dice[0]*dice[3]
        else:
            return dice[0]*dice[1]
    elif len(dice_many) == 4:
         return dice[0]  