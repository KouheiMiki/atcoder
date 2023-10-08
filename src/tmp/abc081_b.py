n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = False
while True:
  for x in a:
    if x % 2 != 0:
      flag = True
      break
  if flag:
    break

  for x in range(len(a)):
    a[x] = a[x] / 2
  ans += 1
print(ans)
