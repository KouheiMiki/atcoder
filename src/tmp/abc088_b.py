# ABC088B - Card Game for Two
# https://atcoder.jp/contests/abs/tasks/abc088_b

n = int(input())
a = list(map(int, input().split()))
ans = 0
a = sorted(a, reverse=True)
for i in range(n):
  if i % 2 == 0:
    ans += a[i]
  else:
    ans -= a[i]
print(ans)
