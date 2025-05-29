def solution(my_string):
    set_list = list(set(my_string))
    
    for i in set_list:
        my_string = my_string[:my_string.find(i)+1] + my_string[my_string.find(i)+1:].replace(i, "")
    
    return my_string