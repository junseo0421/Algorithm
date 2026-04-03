import sys
input = sys.stdin.readline

channels = []
N = int(input())

ch1 = ch2 = 0

for i in range(N):
    ch = input().rstrip()
    channels.append(ch)

    if ch == 'KBS1':
        ch1 = i
    elif ch == 'KBS2':
        ch2 = i

if ch1 < ch2:  # KBS1이 더 위에 있을 경우
    sys.stdout.write('1'*ch1 + '4'*ch1 + '1'*ch2 + '4'*(ch2-1))
else:
    sys.stdout.write('1'*ch1 + '4'*ch1 + '1'*(ch2+1) + '4'*ch2)