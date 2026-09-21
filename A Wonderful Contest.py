t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 100 in a:
        print("Yes")
    else:
        print("No")

# Codeforces problem link --> https://codeforces.com/problemset/problem/2222/A
