a = int(input())
b = int(input())
c = int(input())
x = int(input())
coina = 500
coinb = 100
coinc = 50
ans = 0
for ai in range(a + 1):
  if coina * (a - ai) > x:
    continue
  elif coina * (a - ai) == x:
    ans += 1
    continue
  else:
    for bi in range(b + 1):
      if coina * (a - ai) + coinb * (b - bi) > x:
        continue
      elif coina * (a - ai) + coinb * (b - bi) == x:
        ans += 1
        continue
      else:
        for ci in range(c + 1):
          if coina * (a - ai) + coinb * (b - bi) + coinc * (c - ci) > x:
            continue
          elif coina * (a - ai) + coinb * (b - bi) + coinc * (c - ci) == x:
            ans += 1
            continue
          else:
            break
print(ans)
