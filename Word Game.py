t = int(input())

for _ in range(t):
    n = int(input())

    a = input().split()
    b = input().split()
    c = input().split()

    cnt = {}

    for word in a + b + c:
        cnt[word] = cnt.get(word, 0) + 1

    p1 = p2 = p3 = 0

    for word in a:
        if cnt[word] == 1:
            p1 += 3
        elif cnt[word] == 2:
            p1 += 1

    for word in b:
        if cnt[word] == 1:
            p2 += 3
        elif cnt[word] == 2:
            p2 += 1

    for word in c:
        if cnt[word] == 1:
            p3 += 3
        elif cnt[word] == 2:
            p3 += 1

    print(p1, p2, p3)

# problem link --> https://codeforces.com/problemset/problem/1722/C
