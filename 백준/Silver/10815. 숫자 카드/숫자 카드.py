import sys

n = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))
n_dict = {}

for i in n_list:
    n_dict[i] = 1
    
m = int(sys.stdin.readline())

m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    try:
        print(n_dict[i], end=" ")
    except:
        print(0, end=" ")
