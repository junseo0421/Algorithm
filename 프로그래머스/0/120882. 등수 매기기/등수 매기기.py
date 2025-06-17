def solution(score):
    avg_score = [sum(i)/len(i) for i in score]
    
    sort_avg = sorted(avg_score, reverse=True)
    
    num_dict = {}
    count = 1
    
    for num in sort_avg:
        if not num in num_dict:
            num_dict.update({num:count})
        count += 1
    
    return [num_dict[i] for i in avg_score]