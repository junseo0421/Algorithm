def solution(my_string):
    remove_string = ["a", "e", "i", "o", "u"]
    for i in remove_string:
        my_string = my_string.replace(i, "")
        
    return my_string