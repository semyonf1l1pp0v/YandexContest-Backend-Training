dct = {}
count = int(input())

for i in range(count):
    data = input().split()
    time_traveled = (int(data[0]) * 24 + int(data[1])) * 60 + int(data[2])
    if data[4] == 'A':
        if int(data[3]) not in dct:
            dct[int(data[3])] = -time_traveled
        else:
            dct[int(data[3])] += -time_traveled
    elif data[4] in ('S', 'C'):
        if int(data[3]) not in dct:
            dct[int(data[3])] = time_traveled
        else:
            dct[int(data[3])] += time_traveled

sorted_dct = sorted(dct.items(), key=lambda x: x[0])
val = [el[1] for el in sorted_dct]
print(' '.join(str(el) for el in val))
