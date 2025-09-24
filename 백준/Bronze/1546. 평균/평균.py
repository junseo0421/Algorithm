import sys

N = int(sys.stdin.readline())

score_list = list(map(int, sys.stdin.readline().split()))

print(sum(score_list)*100/max(score_list)/N)