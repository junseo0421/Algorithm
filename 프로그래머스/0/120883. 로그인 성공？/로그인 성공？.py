def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            return 'login'
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            return 'wrong pw'
    return 'fail'