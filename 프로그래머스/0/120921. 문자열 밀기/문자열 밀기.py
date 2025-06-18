def solution(A, B):
    if A == B:
        return 0

    for i in range(len(A) - 1):
        A_list = list(A)
        A_list[1:len(A)], A_list[0] = A[:len(A)-1], A[-1]
        A = ''.join(A_list)
        
        if A == B:
            return i+1
        
    return -1