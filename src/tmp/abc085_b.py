# ABC085B - Kagami Mochi
# https://atcoder.jp/contests/abs/tasks/abc085_b

n = int(input())
d = []
for i in range(n):
  tmp = int(input())
  if tmp not in d :
    d.append(tmp)
print(len(d))