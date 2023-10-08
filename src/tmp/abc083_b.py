n, a, b = map(int, input().split())
ans = 0
for ni in range(1, n + 1):
  nli = [int(x) for x in list(str(ni))]
  if a <= sum(nli) <= b:
    ans += ni
print(ans)
