t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if p[i] <= i + 1:
            ans += 1

    print(ans)

# problem link --> https://codeforces.com/problemset/problem/2210/B
