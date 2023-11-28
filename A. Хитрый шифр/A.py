def sixteen(num):
    letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    res = []
    while num != 0:
        if num % 16 < 10:
            res.append(num % 16)
        else:
            res.append(letters[num % 16])
        num //= 16
    ans = res[:3][::-1] if len(res) >= 3 else str(0 * (3 - len(res))) + str(res[::-1])
    return ''.join(str(el) for el in ans)


def cipher(data):
    res = []
    for el in data:
        unique_letters = len(set(el[0] + el[1] + el[2]))
        day_plus_month = sum([int(ch) for ch in el[3]]) + sum([int(ch) for ch in el[4]])
        surname_letter = ord(el[0][0].lower()) - ord('a') + 1
        ciphernum = surname_letter * 256 + unique_letters + 64 * day_plus_month
        res.append(sixteen(ciphernum))
    return res


data = []

count = input()
for i in range(int(count)):
    data.append(input().split(','))

res = cipher(data)
print(' '.join(res))
