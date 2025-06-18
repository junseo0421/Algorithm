def solution(common):
    diff1, diff2 = common[1] - common[0], common[2] - common[1]
    
    if diff1 == diff2:
        return common[-1] + diff1
    
    return common[-1] * (common[1] // common[0])
    