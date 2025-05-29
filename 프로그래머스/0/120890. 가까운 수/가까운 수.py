def solution(array, n):
    sort_array = sorted(array)
    new_array = [abs(i-n) for i in sort_array]
    return sort_array[new_array.index(min(new_array))]