def solution(emergency):
    sort_list = sorted(emergency)
    sort_list.reverse()
    
    return [sort_list.index(i)+1 for i in emergency]