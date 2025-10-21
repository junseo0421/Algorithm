import sys

input = sys.stdin.readline

def main():
    t = int(input())

    result = []

    for _ in range(t):
        val = 0
        is_vps = True
        s = input().rstrip()
        for i in s:
            if i == '(':
                val += 1
            else:
                val -= 1
                if val < 0:
                    is_vps = False
                    break
        result.append("YES" if val == 0 and is_vps else "NO")

    return result


sys.stdout.write("\n".join(main()))
