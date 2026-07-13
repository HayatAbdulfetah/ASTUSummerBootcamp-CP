t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    mx = 0
    ans = []

    for i in range(n):
        s += a[i]
        mx = max(mx, (s + i) // (i + 1))
        ans.append(mx)

    print(*ans)
  
# problem link --> https://codeforces.com/problemset/problem/2232/B
