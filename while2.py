data = [2, 4, 6, 8, 10]
sum = 0
i = 0

while i < len(data):
    sum += data[i]
    i += 1

rata_rata = sum / len(data)
print("Rata-rata: ", rata_rata)