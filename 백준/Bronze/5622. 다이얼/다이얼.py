import sys

al_list = {"ABC":3, "DEF":4, "GHI":5, "JKL":6, "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}
A = sys.stdin.readline().rstrip()

total = 0

for i in A:
    for j in al_list.keys():
        if i in j:
            total += al_list[j]

print(total)