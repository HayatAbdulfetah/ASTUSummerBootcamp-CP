t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    used = set()
    ans = []

    for x in a:
        if x not in used:
            ans.append(x)
            used.add(x)

    for x in a:
        if ans.count(x) < a.count(x):
            ans.append(x)

    print(*ans)

# problem link --> https://codeforces.com/problemset/problem/1497/A
