import sys
input = sys.stdin.readline

N = int(input())

num_set = set()

for _ in range(N):
    string = input().rstrip()
    
    if string == 'all':
        num_set = set(range(1, 21))
        continue
    elif string == 'empty':
        num_set.clear()
        continue
    
    a, b = string.split()
    b = int(b)

    if a == 'add':
        if b not in num_set:
            num_set.add(b)
    elif a == 'remove':  # remove는 요소가 집합에 없으면 KeyError가 발생한다
        num_set.discard(b)
    elif a == 'check':
        if b in num_set:
            print(1)
        else:
            print(0)
    else:
        if b in num_set:
            num_set.remove(b)
        else:
            num_set.add(b)
