import sys
input = sys.stdin.readline

N, G = input().split()
N = int(N)

people = set()

for _ in range(N):
    p = input().rstrip()
    people.add(p)

if G == 'Y':
    print(len(people))
elif G == 'F':
    print(len(people) // 2)
else:
    print(len(people) // 3)