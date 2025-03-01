# 解法1
n = int(input())
a = [int(item) for item in input().split(" ")]
# print(a)
count = 0
while True:
  flag = False
  for i in range(n):
    if a[i] % 2 == 1:
      flag = True
      break
    else:
      a[i] = a[i]/2
  if flag:
    break
  else:
    count += 1
  # print(a)
print(count)

# 解法2
n = int(input())
a = [int(item) for item in input().split(" ")]
res = 100000000000
for item in a:
  tmp = 0
  while True:
    if item % 2 == 1:
      break
    else:
      tmp += 1
      item /= 2
  if tmp < res:
    res = tmp
print(res)