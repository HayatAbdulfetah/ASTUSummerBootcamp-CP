t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    left = [0] * n
    left_idx = [0] * n

    left[0] = p[0]
    left_idx[0] = 0

    for i in range(1, n):
        if p[i] < left[i - 1]:
            left[i] = p[i]
            left_idx[i] = i
        else:
            left[i] = left[i - 1]
            left_idx[i] = left_idx[i - 1]

    right = [0] * n
    right_idx = [0] * n

    right[-1] = p[-1]
    right_idx[-1] = n - 1

    for i in range(n - 2, -1, -1):
        if p[i] < right[i + 1]:
            right[i] = p[i]
            right_idx[i] = i
        else:
            right[i] = right[i + 1]
            right_idx[i] = right_idx[i + 1]

    found = False

    for j in range(1, n - 1):
        if left[j - 1] < p[j] and right[j + 1] < p[j]:
            print("YES")
            print(left_idx[j - 1] + 1, j + 1, right_idx[j + 1] + 1)
            found = True
            break

    if not found:
        print("NO")

# problem link --> https://codeforces.com/problemset/problem/1380/A
