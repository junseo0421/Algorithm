import sys
input = sys.stdin.readline

N = int(input())

if N % 2 == 0:
    sys.stdout.write('CY')
else:
    sys.stdout.write('SK')