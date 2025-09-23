import sys

while True:
    summation = sum(list(map(int, sys.stdin.readline().split())))
    
    if summation == 0:
        break
    
    print(summation)
