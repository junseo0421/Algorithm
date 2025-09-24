import sys

text = sys.stdin.readline().rstrip()

for i in range(26):
    print(text.find(chr(i+97)), end=" ")
