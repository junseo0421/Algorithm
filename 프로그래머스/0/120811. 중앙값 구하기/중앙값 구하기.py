def solution(array):
    array.sort()
    
    length = len(array)
    
    return array[length // 2] if length % 2 == 1 else array[length // 2 - 1]