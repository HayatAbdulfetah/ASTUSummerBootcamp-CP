t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    actions = list(map(int, input().split()))

    recent = list(range(1, n + 1))
    inside = set(recent)

    ans = [-1] * (n + 1)

    for time, post in enumerate(actions, 1):

        if post in inside:
            recent.remove(post)
            recent.insert(0, post)

        else:
            removed = recent.pop()
            inside.remove(removed)

            if removed <= n:
                ans[removed] = time

            recent.insert(0, post)
            inside.add(post)

    print(*ans[1:])

# problem link --> https://codeforces.com/problemset/problem/1799/A
