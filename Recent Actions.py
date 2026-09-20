t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    first_times = []
    seen = set()

    for i in range(m):
        if p[i] not in seen:
            seen.add(p[i])
            first_times.append(i + 1)

    ans = [-1] * n

    for i in range(min(n, len(first_times))):
        ans[n - 1 - i] = first_times[i]

    print(*ans)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1799/A
