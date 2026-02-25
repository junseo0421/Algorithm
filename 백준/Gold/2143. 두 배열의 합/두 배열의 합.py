import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
a_array = list(map(int, input().split()))
m = int(input())
b_array = list(map(int, input().split()))

# 부분합 배열을 전부 구한 뒤에, dictionary 로 개수를 저장한 뒤에 합하기

a_part_sum, b_part_sum = [], []
a_dict, b_dict = {}, {}

def count_partial_sum(length, array, sum_lst):
    for i in range(length):
        summation = array[i]
        sum_lst.append(summation)  # 한 자릿수 더하기

        k = 1

        while True:
            if i + k >= length:
                break

            summation += array[i + k]
            sum_lst.append(summation)

            k += 1

def make_dictionary(sum_lst, dict):
    for num in sum_lst:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1


count_partial_sum(n, a_array, a_part_sum)
count_partial_sum(m, b_array, b_part_sum)

make_dictionary(a_part_sum, a_dict)
make_dictionary(b_part_sum, b_dict)

ans = 0

for dict_num, value in a_dict.items():
    b_dict_key = T - dict_num

    if b_dict_key in b_dict:
        ans += value * b_dict[b_dict_key]

sys.stdout.write(str(ans))