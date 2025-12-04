import sys
input = sys.stdin.readline

string = input().rstrip()

str_split = list(string.split('-'))

if len(str_split) == 1:
    sum_only = sum([int(x) for x in str_split[0].split('+')])
    sys.stdout.write(str(sum_only))
else:
    mi = 0
    sum_only = sum([int(x) for x in str_split[0].split('+')])
    for i in range(1, len(str_split)):
        mi += sum([int(x) for x in str_split[i].split('+')])
    sys.stdout.write(str(sum_only - mi))