from math import isqrt

n = int(input())
a = list(map(int, input().split()))

limit = 10**6
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, isqrt(limit) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

for x in a:
    root = isqrt(x)

    if root * root == x and prime[root]:
        print("YES")
    else:
        print("NO")

# codeforces problem link --> https://codeforces.com/problemset/problem/230/B
