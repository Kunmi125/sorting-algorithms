






data = [ 7, 12, 54, 67, 90, 11]

for i in range(1, len(data)):
    swap = False
    for j in range(0, len(data) - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swap = True

    if swap == False:
        break
           
    print(data)