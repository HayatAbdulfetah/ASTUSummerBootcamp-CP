t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    left = 0
    right = n - 1

    blue_sum = a[left]
    red_sum = a[right]

    blue_count = 1
    red_count = 1

    left += 1
    right -= 1

    ok = False

    while left <= right:
        blue_sum += a[left]
        blue_count += 1
        left += 1

        if red_sum > blue_sum and red_count < blue_count:
            ok = True
            break

        if left <= right:
            red_sum += a[right]
            red_count += 1
            right -= 1

    print("YES" if ok else "NO")
  

# problem link--> https://codeforces.com/problemset/problem/1646/B
