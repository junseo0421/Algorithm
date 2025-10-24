import sys
input = sys.stdin.readline


def main():
    n = int(input())
    
    if n == 0:
        sys.stdout.write('1')
    else:
        factorial = 1
    
        for i in range(2, n+1):
            factorial *= i
    
        sys.stdout.write(str(factorial))

main()
