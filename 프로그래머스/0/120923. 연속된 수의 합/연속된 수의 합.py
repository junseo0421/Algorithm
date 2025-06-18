def solution(num, total):
    dif_list = [i + (0.5 - num//2) if num%2==0 else i - num//2 for i in range(num)]
    num_list = [total / num] * num
    
    return [x+y for x, y in zip(num_list, dif_list)]