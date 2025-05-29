def solution(my_string):
    num_string = ''.join([i if i.isdigit() else " " for i in my_string])
    return sum([int(i) for i in num_string.split()])