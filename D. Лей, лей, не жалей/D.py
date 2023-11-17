def bin_search(orders, request, index):
    left, right = 0, len(orders) - 1
    while left <= right:
        mid = (left + right) // 2
        if request[0] <= orders[mid][index] <= request[1] or orders[mid][index] > request[1]:
            right = mid - 1
        else:
            left = mid + 1
    l1, r1 = left, len(orders) - 1
    while l1 <= r1:
        mid = (l1 + r1) // 2
        if request[0] <= orders[mid][index] <= request[1]:
            l1 = mid + 1
        else:
            r1 = mid - 1
    return left, r1


o = int(input())
orders = []
for i in range(o):
    orders.append([int(el) for el in input().split()])

res = []
orders1 = sorted(orders, key=lambda x: (x[0], x[1]))
orders2 = sorted(orders, key=lambda x: (x[1], x[0]))

precost = [0]
cost = 0
for el in orders1:
    cost += el[2]
    precost.append(cost)

preduration = [0]
duration = 0
for el in orders2:
    duration += el[1]-el[0]
    preduration.append(duration)

r = int(input())
for i in range(r):
    request = [int(el) for el in input().split()]
    if request[2] == 1:
        low, high = bin_search(orders1, request, request[2] - 1)
        data = precost[high+1] - precost[low]
    else:
        low, high = bin_search(orders2, request, request[2] - 1)
        data = preduration[high+1] - preduration[low]
    res.append(str(data))
print(' '.join(res))
