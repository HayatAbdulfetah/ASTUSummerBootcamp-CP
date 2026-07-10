t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = 0
    right = n - 1
    ans = 0

    while True:

        while left < n and a[left] == 0:
            left += 1

        while right >= 0 and a[right] == 1:
            right -= 1

        if left < right:
            ans += 1
            left += 1
            right -= 1
        else:
            break

    print(ans)

# problem link --> https://codeforces.com/problemset/problem/1746/B
