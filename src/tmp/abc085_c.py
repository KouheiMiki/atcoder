# ABC085C - Otoshidama
# https://atcoder.jp/contests/abs/tasks/abc085_c

n, y = map(int, input().split())
for i in range(n + 1):
  for s in range(n + 1 - i):
    if i * 10000 + s * 5000 + (n - i - s) * 1000 == y:
      print(i, s, (n - i - s))
      exit()
print(-1,-1,-1)