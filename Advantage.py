t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    ans = []
    
    a = sorted(s)
    
    max1 = a[-1]
    max2 = a[-2]
    
    for x in s:
        if x == max1:
            ans.append(x - max2)
        else:
            ans.append(x - max1)
            
    print(*ans)

# problem link --> https://codeforces.com/problemset/problem/1760/C
