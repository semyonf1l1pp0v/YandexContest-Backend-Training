#   TODO: TASK A - DONE!
# Volozh,Arcady,Yurievich,11,2,1964
# Segalovich,Ilya,Valentinovich,13,9,1964

# def sixteen(num):
#     letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: 'F'}
#     res = ''
#     while num != 0:
#         if num % 16 < 10:
#             res += str(num % 16)
#         else:
#             res += letters[int(num % 16)]
#         num //= 16
#     return res[:3][::-1] if len(res) >= 3 else str(0 * (3 - len(res))) + res[::-1]
#
#
# def cipher(data):
#     people = [el.split(',') for el in data.split()]
#     res = ''
#     for el in people:
#         unique_letters = len(set(el[0] + el[1] + el[2]))
#         day_plus_month = sum([int(ch) for ch in el[3]]) + sum([int(ch) for ch in el[4]])
#         surname_letter = ord(el[0][0].lower()) - ord('a') + 1
#         ciphernum = surname_letter * 256 + unique_letters + 64 * day_plus_month
#         res += sixteen(ciphernum) + ' '
#     return res.strip()
#
#
# data = ''
#
# count = input()
# for i in range(int(count)):
#     data += input() + '\n'
#
# print(cipher(data))


# print(cipher('2\nVolozh,Arcady,Yurievich,11,2,1964\nSegalovich,Ilya,Valentinovich,13,9,1964\n'))

#   TODO TASK B - DONE!

# 8
# 50 7 25 3632 A
# 14 23 52 212372 S
# 15 0 5 3632 C
# 14 21 30 212372 A
# 50 7 26 3632 C
# 14 21 30 3632 A
# 14 21 40 212372 B
# 14 23 52 3632 B

# from collections import defaultdict
# dct = defaultdict(int)
# ans = ''
# count = int(input())
#
# for i in range(count):
#     data = input().split()
#     time_traveled = (int(data[0]) * 24 + int(data[1])) * 60 + int(data[2])
#     if data[4] == 'A':
#         dct[int(data[3])] += -time_traveled
#     elif data[4] in ('S','C'):
#         dct[int(data[3])] += time_traveled
#     else:
#         dct[int(data[3])] += 0
#
# sorted_dct = sorted(dct.items())
# for el in sorted_dct:
#     ans += str(el[1]) + ' '
# print(ans)

# data = '3 4 6 8 7'
# res = []
# res.append([int(el) for el in data.split()])
# print(res)

#   TODO: TASK D

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
# r = int(input())
# for i in range(r):
#     request = [int(el) for el in input().split()]
#     if request[2] == 1:
#         low, high = bin_search(orders1, request, request[2] - 1)
#         data = sum(el[2] for el in orders1[low:high + 1])
#     else:
#         low, high = bin_search(orders2, request, request[2] - 1)
#         data = sum(el[1] - el[0] for el in orders2[low:high + 1])
#     res.append(str(data))
# print(' '.join(res))



# 5
# 5 20 5
# 6 21 4
# 6 22 3
# 7 23 2
# 10 24 1
# 3
# 6 11 1
# 4 6 1
# 7 11 1


# def consec_ones(nums):
#     if not nums:
#         return 0
#     dp = [1] if nums[0] == 1 else [0]
#     dp += [0] * (len(nums) - 1)
#     for i in range(1, len(nums)):
#         if nums[i] == 1:
#             dp[i] = dp[i - 1] + 1
#     return max(dp)
#
#
# nums_count = int(input())
# nums_str = ''
# for i in range(nums_count):
#     nums_str += str(input()) + '\n'
# nums = [int(el) for el in nums_str.strip().split('\n')] if nums_str else []
# ans = str(consec_ones(nums)) + '\n'
# print(ans.strip())

# count = int(input())
# res = []
# ch = -2**31-1
# for i in range(count):
#     num = int(input())
#     if num != ch:
#         res.append(num)
#         ch = num
# for el in res:
#     print(el)
