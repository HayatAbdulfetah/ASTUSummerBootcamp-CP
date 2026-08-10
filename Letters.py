from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix = []
total = 0

for x in a:
    total += x
    prefix.append(total)

for x in b:
    i = bisect_left(prefix, x)

    if i == 0:
        room = x
    else:
        room = x - prefix[i - 1]

    print(i + 1, room)

# CodeForces problem link --> https://codeforces.com/problemset/problem/978/C
