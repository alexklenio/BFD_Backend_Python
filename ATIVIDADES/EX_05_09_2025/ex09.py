for i in range (1, 61):
    if i % 3 == 0 and i < 60:
        print(i, end=" - ")
    elif i == 60:
        print(i)
