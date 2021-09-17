def make_one(x):
    if x < 0:
        return

    for i in range(1, 10):
        if x % i == 0:
            pass
            print(i)
            break
        else:
            make_one(x-1)

make_one(26)
