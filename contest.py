# TODO: TASK A - DONE!
#
# def sixteen(num):
#     letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: 'F'}
#     res = []
#     while num != 0:
#         if num % 16 < 10:
#             res.append(num % 16)
#         else:
#             res.append(letters[num % 16])
#         num //= 16
#     ans = res[:3][::-1] if len(res) >= 3 else str(0 * (3 - len(res))) + str(res[::-1])
#     return ''.join(str(el) for el in ans)
#
#
# def cipher(data):
#     res = []
#     for el in data:
#         unique_letters = len(set(el[0] + el[1] + el[2]))
#         day_plus_month = sum([int(ch) for ch in el[3]]) + sum([int(ch) for ch in el[4]])
#         surname_letter = ord(el[0][0].lower()) - ord('a') + 1
#         ciphernum = surname_letter * 256 + unique_letters + 64 * day_plus_month
#         res.append(sixteen(ciphernum))
#     return res
#
#
# data = []
#
# count = input()
# for i in range(int(count)):
#     data.append(input().split(','))
#
# res = cipher(data)
# print(' '.join(res))


#   TODO TASK B - DONE! (можно через defaultdict, кода будет меньше (но будет ли онт аким же быстрым?))

# dct = {}
# count = int(input())
#
# for i in range(count):
#     data = input().split()
#     time_traveled = (int(data[0]) * 24 + int(data[1])) * 60 + int(data[2])
#     if data[4] == 'A':
#         if int(data[3]) not in dct:
#             dct[int(data[3])] = -time_traveled
#         else:
#             dct[int(data[3])] += -time_traveled
#     elif data[4] in ('S','C'):
#         if int(data[3]) not in dct:
#             dct[int(data[3])] = time_traveled
#         else:
#             dct[int(data[3])] += time_traveled
#
# sorted_dct = sorted(dct.items(), key=lambda x:x[0])
# val = [el[1] for el in sorted_dct]
# print(' '.join(str(el) for el in val))

#   TODO: TASK D - DONE!

# def bin_search(orders, request, index):
#     left, right = 0, len(orders) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if request[0] <= orders[mid][index] <= request[1] or orders[mid][index] > request[1]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     l1, r1 = left, len(orders) - 1
#     while l1 <= r1:
#         mid = (l1 + r1) // 2
#         if request[0] <= orders[mid][index] <= request[1]:
#             l1 = mid + 1
#         else:
#             r1 = mid - 1
#     return left, r1

#
# o = int(input())
# orders = []
# for i in range(o):
#     orders.append([int(el) for el in input().split()])
#
# res = []
# orders1 = sorted(orders, key=lambda x: (x[0], x[1]))
# orders2 = sorted(orders, key=lambda x: (x[1], x[0]))
#
# precost = [0]
# cost = 0
# for el in orders1:
#     cost += el[2]
#     precost.append(cost)
#
# preduration = [0]
# duration = 0
# for el in orders2:
#     duration += el[1]-el[0]
#     preduration.append(duration)
#
# r = int(input())
# for i in range(r):
#     request = [int(el) for el in input().split()]
#     if request[2] == 1:
#         low, high = bin_search(orders1, request, request[2] - 1)
#         data = precost[high+1] - precost[low]
#     else:
#         low, high = bin_search(orders2, request, request[2] - 1)
#         data = preduration[high+1] - preduration[low]
#     res.append(str(data))
# print(' '.join(res))
