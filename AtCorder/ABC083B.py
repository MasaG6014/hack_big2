NAB = [int(item) for item in input().split(" ")]
N = int(NAB[0])
A = int(NAB[1])
B = int(NAB[2])
answer = 0

for i in range(1,N + 1):
  counter = 0
  for ii in str(i):
    counter += int(ii)
  if A <= counter & counter <= B:
      answer += i

print(answer)