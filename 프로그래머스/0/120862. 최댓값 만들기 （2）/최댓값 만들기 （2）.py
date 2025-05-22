def solution(numbers):
    numbers.sort()
    
    pos = numbers[-2] * numbers[-1]
    neg = numbers[0] * numbers[1]
    
    if pos >= neg:
        return pos
    else:
        return neg