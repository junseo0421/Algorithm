import sys
input = sys.stdin.readline

def recursion(s, l, r):
    if l >= r: return 1, l+1
    elif s[l] != s[r]: return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

def main():
    n = int(input())
    
    for _ in range(n):
        a, b = isPalindrome(input().rstrip())
        print(a, b)
        
main()


