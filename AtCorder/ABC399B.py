def sortTuple(array, index):
    if array == []:
        return []
    pin = array[0]
    smaller = []
    bigger = []
    same = [array[0]]
    for i in range(1,len(array)):
        if pin[index] > array[i][index]:
            smaller.append(array[i])
        elif pin[index] < array[i][index]:
            bigger.append(array[i])
        else:
            same.append(array[i])
    return sortTuple(bigger, index) + same + sortTuple(smaller, index)

def one():
    N = int(input())
    ps = [[int(score)] for score in input().split()]
    for i in range(N):
        ps[i].append(i)
    # print(ps)

    ps = sortTuple(ps, 0)
    # print(ps)
    rank = 1
    ps[0].append(rank)
    k = 1
    for i in range(1,N):
        if ps[i][0] == ps[i-1][0]:
            k += 1
        else:
            rank += k
            k = 1
        ps[i].append(rank)
    # print(ps)
    ps = sortTuple(ps, 1)
    for i in range(N):
        print(ps[N-1-i][2])

def getMaxScore(array):
    max = 0
    for item in array:
        if item[1] and item[0] > max:
            max = item[0]
    return max

def two():
    N = int(input())
    ps = [[int(score), True] for score in input().split()]
    print(ps)
    r = 1
    while r <= N:
        k = 0
        max = getMaxScore(ps)
        for i in range(N):
            if ps[i][0] == max:
                ps[i].append(r)
                ps[i][1] = False
                k += 1
        r += k
    print(ps)
    for item in ps:
        print(item[2])
two()