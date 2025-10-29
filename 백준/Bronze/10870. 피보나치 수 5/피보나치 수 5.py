import sys
input = sys.stdin.readline

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input())
    sys.stdout.write(str(fibonacci(n)))

main()
