# A - First ABC 2
# https://atcoder.jp/contests/abc322/tasks/abc322_a

n = int(input())
s = input()

for ni in range(n):
  if s[ni:ni+3] == 'ABC':
    print(ni+1)
    exit()
print(-1)