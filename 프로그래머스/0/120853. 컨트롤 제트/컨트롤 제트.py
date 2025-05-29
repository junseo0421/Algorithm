def solution(s):
    s_list = s.split()
    return sum([int(num) if not num=='Z' else -int(s_list[i-1]) for i, num in enumerate(s_list)])