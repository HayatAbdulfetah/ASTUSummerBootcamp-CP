t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    for n in nums:
        print(min(n, a[0] - 1), end=" ")
    print()
  

# problem link --> https://codeforces.com/problemset/problem/1956/A
