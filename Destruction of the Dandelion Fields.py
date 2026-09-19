import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    evens_sum = 0
    odds = []
    for v in a:
        if v % 2 == 0:
            evens_sum += v
        else:
            odds.append(v)
    k = len(odds)
    if k == 0:
        print(0)
        continue
    odds.sort(reverse=True)
    take = (k + 1) // 2
    print(evens_sum + sum(odds[:take]))

# Codeforces problem link --> https://codeforces.com/problemset/problem/2148/D
