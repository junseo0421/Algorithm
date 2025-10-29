import sys
input = sys.stdin.readline

def main():
    count = 0
    answer = -1

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    def merge(low, mid, high):
        nonlocal count, answer, arr

        l = low
        m = mid + 1

        temp = []

        while l <= mid and m <= high:
            if arr[l] <= arr[m]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[m])
                m += 1

        while l <= mid:
            temp.append(arr[l])
            l += 1

        while m <= high:
            temp.append(arr[m])
            m += 1

        t = 0
        for idx in range(low, high+1):
            arr[idx] = temp[t]
            t += 1

            count += 1
            if count == k:
                answer = arr[idx]

    def sort(low, high):
        if low >= high:
            return
        mid = (high + low) // 2

        sort(low, mid)
        sort(mid+1, high)
        merge(low, mid, high)

    sort(0, n-1)
    sys.stdout.write(str(answer))


main()
