import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = input().rstrip()
    length = len(string)
    K = int(input())

    num_dict = {}
    index_dict = {}
    ans1, ans2 = 10001, 0

    left = 0
    right = 0

    while right < length:
        if not string[right] in num_dict:
            num_dict[string[right]] = 1
            index_dict[string[right]] = [right]
        else:
            num_dict[string[right]] += 1
            index_dict[string[right]].append(right)

        while num_dict[string[right]] >= K:
            num_dict[string[left]] -= 1
            ans1 = min(ans1, right - left + 1)
            left += 1

        right += 1

    # 만족하는 연속 문자열이 없을 시
    if ans1 == 10001:
        print(-1)
        continue

    for alpha in index_dict:
        index_lst = index_dict[alpha]
        if len(index_lst) < K:
            continue

        j = 0

        while j + K - 1 < len(index_lst):
            ans2 = max(ans2, index_lst[j + K - 1] - index_lst[j] + 1)
            j += 1

    print(ans1, ans2)