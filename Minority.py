t = int(input())
for _ in range(t):
  s = input()
  
  ones = s.count('1')
  zeros = s.count('0')

  if ones < zeros:
    print(ones)
  elif ones > zeros:
    print(zeros)
  else:
    print(0)


# Codeforces problem link --> https://codeforces.com/problemset/problem/1633/B
