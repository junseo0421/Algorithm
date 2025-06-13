def solution(dots):
    grad_list = []
    
    matching_list = [[1, 2, 3], [2, 1, 3], [3, 1, 2]]
    
    dots.sort()
    
    for i in range(3):
        match = matching_list[i]
        grad_1 = (dots[0][0] - dots[match[0]][0]) / (dots[0][1] - dots[match[0]][1])
        grad_2 = (dots[match[1]][0] - dots[match[2]][0]) / (dots[match[1]][1] - dots[match[2]][1])
        if grad_1 == grad_2:
            return 1
            
    return 0