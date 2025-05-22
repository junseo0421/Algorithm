def solution(my_string, num1, num2):
    my_string = list(my_string)
    
    first = my_string[num1]
    second = my_string[num2]
    
    my_string[num1] = second
    my_string[num2] = first
    
    return "".join(my_string)