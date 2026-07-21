t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    freq = {}
    count = 0
    
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            count += 1
            
        count += 1
        
    print(count)

# problem link --> https://codeforces.com/problemset/problem/1703/B
