# ABC049C - 白昼夢
# https://atcoder.jp/contests/abs/tasks/arc065_a

s = list(input())
s.reverse()
print(s)
ans = 'NO'
tmp = 0
while True:
  print(tmp)
  if len(s) == tmp:
    ans = 'YES'
    break
  if s[tmp:7] == list('dreamer'):
    tmp += 7
  elif s[tmp:6] == list('eraser'):
    tmp += 6
  elif s[tmp:5] == list('dream') or s[:5] == list('erase'):
    tmp += 5
  else:
    break
print(ans)