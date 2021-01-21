def compound(seed, days, interest, monthly=0):
    for i in range(days):
        if i % 30 == 0:
            seed += monthly
        seed = seed + (seed * interest)
    seed = str(int(seed))

    for idx, i in enumerate(seed):
        idx = len(seed) - idx
        unit = ["원", "만", "억", "조"]
        if idx % 4 == 1 and idx != 0:
            print(i, end=unit[idx // 4] + ' ')
        else:
            print(i, end="")


def main():
    seed = 0
    days = 365 * 2
    monthly = 500000
    interest = 0.01
    compound(seed, days, interest, monthly)


if __name__ == '__main__':
    main()
