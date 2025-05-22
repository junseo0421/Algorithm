def solution(my_string):
    return ''.join([i.lower() if i.upper()==i else i.upper() for i in my_string])