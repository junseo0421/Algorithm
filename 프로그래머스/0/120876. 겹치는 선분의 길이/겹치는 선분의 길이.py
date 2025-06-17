def solution(lines):
    overlap_list = []
    
    lines.sort()
    
    [[x1, x2], [y1, y2], [z1, z2]] = lines
    
    if x2 - y1 > 0:
        for i in range(max(x1, y1), min(x2, y2)):
            overlap_list.append(i)
    
    if y2 - z1 > 0:
        for i in range(max(y1, z1), min(y2, z2)):
            overlap_list.append(i)
        
    if x2 - z1 > 0:
        for i in range(max(x1, z1), min(x2, z2)):
            overlap_list.append(i)
        
    return len(set(overlap_list))