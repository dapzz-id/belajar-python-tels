nums = [1, 2, -3, 4, -5, 6]
sum_positives = 0
sum_ganjil = 0;

for num in nums:
    if num < 0:
        continue
    sum_positives += num

for numer in nums:
    if numer % 2 == 0:
        break
    sum_ganjil += numer

print('sum of positive numbers:', sum_positives)
print('sum of positive odd numbers:', sum_ganjil)