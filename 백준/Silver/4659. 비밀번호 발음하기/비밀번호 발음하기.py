import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    string = input().rstrip()

    if string == 'end':
        break

    is_vowel = 0
    vowel_n = 0
    con_n = 0
    is_acceptable = 1
    prev = ''

    for idx, s in enumerate(string):
        if idx != 0:
            # 연속적으로 같은 글자 두 번 오는 경우
            if prev == s:
                if not (s == 'e' or s == 'o'):
                    is_acceptable = 0
                    break

        prev = s

        # 모음 3개 혹은 자음 3개 연속 판정
        if s in vowel:
            vowel_n += 1
            con_n = 0

            if not is_vowel:
                is_vowel = 1

        else:
            vowel_n = 0
            con_n += 1

        if vowel_n == 3 or con_n == 3:
            is_acceptable = 0
            break

    if is_acceptable == 0 or is_vowel == 0:
        print(f'<{string}> is not acceptable.')
    else:
        print(f'<{string}> is acceptable.')
