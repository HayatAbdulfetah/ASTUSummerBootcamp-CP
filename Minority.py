t = int(input())
for _ in range(t):
  s = input()
  
  ones = s.count('1')
  zeros = s.count('0')

  if ones >= zeros:
    print(ones)
  else:
    print(zeros)
