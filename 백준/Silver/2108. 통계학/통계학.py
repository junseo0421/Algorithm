import sys
input = sys.stdin.readline


def main():
    n = int(input())
    num_list = []
    fre_arr = [0] * (8000 + 1)
    result = []

    for i in range(n):
        num = int(input())

        fre_arr[num+4000] += 1
        num_list.append(num)

    max_fre = max(fre_arr)
    fre_count = []
    for idx, i in enumerate(fre_arr):
        if max_fre == i:
            fre_count.append(idx-4000)

    num_list.sort()
    result.append(str(round(sum(num_list) / n)))
    result.append(str(num_list[n//2]))
    if len(fre_count) > 1:
        result.append(str(sorted(fre_count)[1]))
    else:
        result.append(str(fre_count[0]))
    result.append(str(num_list[-1] - num_list[0]))

    sys.stdout.write('\n'.join(result))

main()
