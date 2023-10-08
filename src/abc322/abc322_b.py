# B - Prefix and Suffix
# https://atcoder.jp/contests/abc322/tasks/abc322_b

n, m = map(int, input().split())
s = input()
t = input()

if t[0:n] == s and t[-1 * n:] == s:
  print(0)
elif t[0:n] == s:
  print(1)
elif t[-1 * n:] == s:
  print(2)
else:
  print(3)
