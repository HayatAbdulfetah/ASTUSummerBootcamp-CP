n = int(input())
s = input()

rooms = [0] * 10

for ch in s:
    if ch == "L":
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break

    elif ch == "R":
        for i in range(9, -1, -1):
            if rooms[i] == 0:
                rooms[i] = 1
                break

    else:
        rooms[int(ch)] = 0

print(*rooms, sep="")

#  Codefoces link --> https://codeforces.com/problemset/problem/1200/A
