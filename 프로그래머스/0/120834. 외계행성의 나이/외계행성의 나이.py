import string

def solution(age):
    alpha = [i for i in string.ascii_lowercase]
    
    return "".join([alpha[int(j)] for j in str(age)])