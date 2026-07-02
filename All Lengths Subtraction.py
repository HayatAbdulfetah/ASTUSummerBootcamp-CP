from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))

    ok = True

    for x in range(1, n + 1):
        if d and d[0] == x:
            d.popleft()
        elif d and d[-1] == x:
            d.pop()
        else:
            ok = False
            break

    print("YES" if ok else "NO")

# problem link --> https://codeforces.com/problemset/problem/2143/A
