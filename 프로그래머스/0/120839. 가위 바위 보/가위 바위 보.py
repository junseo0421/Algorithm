def solution(rsp):
    dictionary = {'2':'0', '0':'5', '5':'2'}
    
    return "".join([dictionary[i] for i in rsp])