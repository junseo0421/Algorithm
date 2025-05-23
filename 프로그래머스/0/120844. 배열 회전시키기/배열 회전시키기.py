def solution(numbers, direction):
    if direction == 'right':
        numbers[0], numbers[1:len(numbers)] = numbers[-1], numbers[0:len(numbers)-1]
    if direction == 'left':
        numbers[-1], numbers[0:len(numbers)-1] = numbers[0], numbers[1:len(numbers)]
    return numbers