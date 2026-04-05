import sys
input = sys.stdin.readline

num_dict = {0:1, 1:0}

switch_n = int(input())
switches = list(map(int, input().split()))
student_n = int(input())

for _ in range(student_n):
    gender, switch = map(int, input().split())

    p = 1

    # 남학생 1, 여학생 2
    if gender == 1:
        for i in range(1, switch_n // switch + 1):
            switches[switch * i - 1] = num_dict[switches[switch * i - 1]]

    else:
        switch -= 1
        switches[switch] = num_dict[switches[switch]]

        while p <= switch and p < switch_n - switch:
            if switches[switch + p] == switches[switch - p]:
                switches[switch + p] = switches[switch - p] = num_dict[switches[switch - p]]
            else:
                break

            p += 1

for i in range(switch_n):
    if i > 0 and i % 20 == 0:
        print()

    print(switches[i], end=" ")