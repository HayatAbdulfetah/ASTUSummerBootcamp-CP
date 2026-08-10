n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm = 0
total = 0

for x in b:
    while x > total + a[dorm]:
        total += a[dorm]
        dorm += 1

    print(dorm + 1, x - total)

# CodeForces problem link --> https://codeforces.com/problemset/problem/978/C
