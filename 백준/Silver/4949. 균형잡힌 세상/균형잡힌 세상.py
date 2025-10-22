import sys
input = sys.stdin.readline


def main():
    result = []
    
    while True:
        string = input().rstrip()
        if string == '.':
            break

        is_bal = True
        stack = []

        for s in string:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    is_bal = False
                    break
            elif s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    is_bal = False
                    break

        result.append('yes' if (not stack) and is_bal else 'no')

    sys.stdout.write("\n".join(result))


main()
