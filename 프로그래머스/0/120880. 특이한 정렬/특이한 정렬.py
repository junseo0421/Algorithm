def solution(numlist, n):
    sorted_num = sorted(numlist)
    abs_list = [abs(i-n) for i in sorted_num]
    num_dict = dict(zip(sorted_num, abs_list))
    
    result = sorted(num_dict.items(), key= lambda x: (x[1], -x[0]))
        
    return [i[0] for i in result]