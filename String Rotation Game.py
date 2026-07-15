t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    blocks = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            blocks += 1

    ans = blocks
    edge = (s[0] != s[-1])

    for i in range(n - 1):
        cur = blocks
        if s[i] != s[i + 1]:
            cur -= 1
        if edge:
            cur += 1
        ans = max(ans, cur)

    print(ans)

# problem link --> https://codeforces.com/problemset/problem/2192/A
