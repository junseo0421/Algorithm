import sys
input = sys.stdin.readline

def main():
    def split_str(low, high):  # ex) 6, 8 / 0, 2
        nonlocal temp
        if high - low < 2:
            return

        step = (high - low + 1) // 3

        for i in range(low+step, low+step*2):
            temp.append(i)

        split_str(low, low+step-1)
        split_str(low+step*2, high)

    while True:
        n = input().rstrip()

        if not n:
            break

        string = ['-'] * (3 ** int(n))

        temp = []
        split_str(0, 3 ** int(n) - 1)

        for blank in temp:
            string[blank] = " "

        print(''.join(string))

main()
