t = int(input())

for _ in range(t):
    s = input()

    ones = s.count('1')
    zeros = s.count('0')

    if ones != zeros:
        print(min(ones, zeros))
    else:
        print(ones - 1)


# Codeforces problem link --> https://codeforces.com/problemset/problem/1633/B
