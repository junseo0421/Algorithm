import sys
input = sys.stdin.readline

N = int(input())

num_list = sorted(map(int, input().split()), reverse=True)

result = 0

for idx, num in enumerate(num_list):
    result += num * (idx+1)
    
sys.stdout.write(str(result))
