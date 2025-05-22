def solution(my_string):
    number_list = [int(i) for i in my_string if i.isdigit()]
    
    number_list.sort()
    
    return number_list