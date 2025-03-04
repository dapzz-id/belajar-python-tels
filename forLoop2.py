for i in range(2, 4):
    for j in range(1, 11):
        if i == j:
            #break
            continue
        print(i, "*", j, "=", i*j)