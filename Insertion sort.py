lis = [5, 65, 76, 11, 9]

for i in range(1, len(lis)):
    j = i
    while j > 0:
        if lis[j - 1] > lis[j]:
            lis[j - 1],  lis[j] = lis[j], lis[j - 1]
        j -= 1

    print(lis)
