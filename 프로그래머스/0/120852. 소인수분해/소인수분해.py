def solution(n):
    div = 2
    num_list = []
    while(div**2 <= n):
        if n % div == 0:
            num_list.append(div)
            n = n // div
        else:
            div += 1
    if n > 1:
        num_list.append(n)
    
    return sorted(list(set(num_list)))