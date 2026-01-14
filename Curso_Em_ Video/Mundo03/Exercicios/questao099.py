def maior(*num):
    maior = num[0]
    for i in num:
        if maior < i:
            maior = i

    print(f"o mairo numero e {maior}")


maior(10, 7, 3, 9)
