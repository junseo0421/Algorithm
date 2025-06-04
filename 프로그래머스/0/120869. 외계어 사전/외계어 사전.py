def solution(spell, dic):
    for i in dic:
        if len(i) == len(spell):
            num_count = 0
            for j in spell:
                if i.count(j) == 1:
                    num_count += 1
                if num_count == len(spell):
                    return 1

    return 2