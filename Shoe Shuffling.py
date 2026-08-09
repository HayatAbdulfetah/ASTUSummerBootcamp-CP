t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    p = [0] * n
    possible = True

    i = 0

    while i < n:
        j = i
      
        while j < n and s[j] == s[i]:
            j += 1

        if j - i == 1:
            possible = False
            break

        for k in range(i, j - 1):
            p[k] = k + 2

        p[j - 1] = i + 1

        i = j

    if possible:
        print(*p)
    else:
        print(-1)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1691/B
