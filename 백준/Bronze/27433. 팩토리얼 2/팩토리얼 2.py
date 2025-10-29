import sys
input = sys.stdin.readline

def factorial(n):
    return n * factorial(n-1) if n > 1 else 1
    
def main():
    n = int(input())
    sys.stdout.write(str(factorial(n)))

main()
