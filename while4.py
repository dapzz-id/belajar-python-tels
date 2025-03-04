data = [5, 12, 8, 20, 7, 14, 11]
filtered_data = []
i = 0

while i < len(data):
    if data[i] > 10:
        filtered_data.append(data[i])
    i += 1

print('Data yang sudah difilter:', filtered_data)