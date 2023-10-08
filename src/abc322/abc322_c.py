# C - Festival
# https://atcoder.jp/contests/abc322/tasks/abc322_c

n, m = map(int, input().split())
a = list(map(int, input().split()))
tmp = 0
for ni in range(n):
  if ni+1 < a[tmp]:
    print(a[tmp] - (ni + 1))
  elif ni+1 == a[tmp]:
    print(0)
    tmp += 1