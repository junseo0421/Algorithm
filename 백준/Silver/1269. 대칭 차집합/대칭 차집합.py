import sys

n, m = map(int, sys.stdin.readline().split())

a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

print(len(a_set.symmetric_difference(b_set)))
