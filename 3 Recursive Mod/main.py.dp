fdict = {0: 0, 1: 1, 2: 2}


def f(n):
    global fdict
    if n not in fdict:
        fdict[n] = (f(n - 3) + (2 * f(n - 2)) + f(n - 1))
    return fdict[n]


def main():
    # n = int(input())
    n = 10000000
    [f(x) for x in range(0,n,2000)]
    print(f(n) % 10007)


if __name__ == '__main__':
    main()
