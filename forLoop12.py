# Outer Loop
for i in range(2, 6):
    # Inner Loop
    for j in range(1, 11):
        if i == j:
            continue
        print(i*j, end=", ")
    print("\n")