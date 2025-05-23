def solution(order):
    # 0 제외 해야함
    
    return sum([1 if int(i) is not 0 and int(i)%3==0 else 0 for i in str(order)])