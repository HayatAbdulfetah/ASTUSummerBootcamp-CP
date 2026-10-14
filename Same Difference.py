t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    target = s.count(s[-1])
    ans = len(s) - target

    print(ans)

# Codeforces problem link --> https://codeforces.com/problemset/problem/1520/D
