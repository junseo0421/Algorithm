def solution(numbers):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    num_str = ''
    num_list = []
    for i in numbers:
        num_str += i
        
        if num_str in num_dic:
            num_list.append(num_str)
            num_str = ''
        
    return int(''.join(num_dic[i] for i in num_list))