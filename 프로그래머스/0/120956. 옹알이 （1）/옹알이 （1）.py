babbling_list = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    result = 0
    for i in babbling:
        count = ""
        for j in i:
            count += j
            if count in babbling_list:
                count = ""
                
        if count == "":
            result += 1
    
    return result