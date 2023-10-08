# A - 321-like Checker
# https://atcoder.jp/contests/abc321/tasks/abc321_a

# First
n = list(map(int,input()))

tmp = 'Yes'
for ni in range(len(n)):
  if len(n) == 1:
    break

  if ni+1 == len(n):
    break

  if n[ni] > n[ni + 1]:
    continue

  tmp = 'No'
  break

print(tmp)

# Second
n = input()

for ni in range(len(n)-1):
  if n[ni] <= n[ni+1]:
    print('No')
    break
else:
  # nが1桁の場合
  # nの最後の桁までforが続いた場合
  print('Yes')