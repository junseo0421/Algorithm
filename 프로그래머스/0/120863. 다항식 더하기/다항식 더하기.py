def solution(polynomial):
    poly_list = polynomial.split(' + ')
    
    x_list = 0
    num_list = 0
    
    for i in poly_list:
        if 'x' in i:
            if len(i) == 1:
                x_list += 1
            else:
                x_list += int(i[:-1])
        else:
            num_list += int(i)
            
    if x_list and num_list:
        if x_list == 1:
            return 'x + ' + str(num_list)
        else:
            return str(x_list) + 'x + ' + str(num_list)
    elif x_list == 0:
        return str(num_list)
    elif num_list == 0:
        if x_list == 1:
            return 'x'
        else:
            return str(x_list) + 'x'
    