def solution(array):
    num_list = [0] * (max(array) + 1)
    
    for i in array:
        num_list[i] += 1
    
    if num_list.count(max(num_list)) >= 2:
        return -1
    else:
        return num_list.index(max(num_list))