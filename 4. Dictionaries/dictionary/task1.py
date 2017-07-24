strs = input().lower().split(" ")

unique = list()
count = dict()

for x in strs:
  if x in count:
    count[x] += 1
  else:
    count[x] = 1
    unique.append(x)

ans = list()

for key in unique:
  if count[key] % 2 == 1:
    ans.append(key)

print(", ".join(ans))