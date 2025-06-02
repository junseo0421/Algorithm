def solution(keyinput, board):
    direction_dict = {'left':[-1,0], 'right':[1,0], 'up':[0,1], 'down':[0,-1]}
    
    x_axis, y_axis = 0, 0
    x_axis_max, y_axis_max = board[0] // 2, board[1] // 2
    
    for i in keyinput:
        num_list = direction_dict[i]
        if -x_axis_max <= x_axis + num_list[0] <= x_axis_max:
            x_axis += num_list[0]
        if -y_axis_max <= y_axis + num_list[1] <= y_axis_max:
            y_axis += num_list[1]

    return [x_axis, y_axis]