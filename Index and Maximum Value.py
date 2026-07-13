t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    mx = max(a)

    ans = []

    for _ in range(m):
        op, l, r = input().split()
        l = int(l)
        r = int(r)

        if l <= mx <= r:
            if op == '+':
                mx += 1
            else:
                mx -= 1

        ans.append(str(mx))

    print(*ans)

# https://codeforces.com/problemset/problem/2007/B
