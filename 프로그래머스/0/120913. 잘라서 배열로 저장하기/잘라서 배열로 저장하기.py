def solution(my_str, n):
    str_list = [i for i in my_str]
    for i in range((len(my_str)-1) // n):
        str_list[(i+1)*n] = ' ' + my_str[(i+1)*n]
        
    return ''.join(str_list).split()