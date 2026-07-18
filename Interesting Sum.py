t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(a[-1] + a[-2] - a[0] - a[1])

#problem link --> https://codeforces.com/problemset/problem/1720/B
