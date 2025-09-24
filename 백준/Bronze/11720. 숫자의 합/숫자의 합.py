import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().rstrip()

total = 0

for i in num:
    total += int(i)
    
print(total)