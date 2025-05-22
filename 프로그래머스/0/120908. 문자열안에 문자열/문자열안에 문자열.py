def solution(str1, str2):
    c = str1.count(str2)
    if c != 0:
        answer = 1
    else:
        answer = 2
    return answer