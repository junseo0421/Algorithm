import sys

N, B = sys.stdin.readline().split()

B = int(B)
total = 0

for idx, i in enumerate(reversed(N)):
    if i.isdigit():
        total += (B**idx)*int(i)
    else:
        total += (B**idx)*(ord(i)-55)

print(total)
