for i in range (1, 11):
    if(i % 2 == 1):
        continue

    for j in range (1, 11):
        if(j % 2 == 1):
            continue

        print(i, "*", j, "=", i*j)