import sys
input = sys.stdin.readline

# 1. 첫 글자 우선
# 2. 왼쪽부터 보기

# 첫 글자를 보기 위해선 공백으로 split

# 문자열을 리스트로 다루면서 [@] 를 삽입하는 식으로?

N = int(input())

shortcut = []

for _ in range(N):
    string = list(input().split())

    is_find = False

    for idx, s in enumerate(string):
        if not s[0].upper() in shortcut:
            string[idx] = s.replace(s[0], f'[{s[0]}]', 1)
            shortcut.append(s[0].upper())
            is_find = True
            print(' '.join(string))
            break

    if not is_find:
        for idx, s in enumerate(string):
            for i in s[1:]:
                if not i.upper() in shortcut:
                    string[idx] = s.replace(i, f'[{i}]', 1)
                    shortcut.append(i.upper())
                    is_find = True
                    print(' '.join(string))
                    break

            if is_find:
                break

    if not is_find:
        print(' '.join(string))
