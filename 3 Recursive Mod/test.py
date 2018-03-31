def matmult(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b)):
            product = 0
            for k in range(len(a[i])):
                product += a[i][k] * b[k][j]
            row.append(product)
        result.append(row)
    return result


def power(n):
    if n == 0:
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    floor = (n // 2)
    R = power(floor)
    R = matmult(R, R)
    if n % 2 == 1:
        R = matmult(R, [[1, 2, 1], [1, 0, 0], [0, 1, 0]])
    R = [[elem % 10007 for elem in row] for row in R]
    return R


def f(n):
    if n <= 2:
        return n
    M = matmult(power(n - 1), [[2], [1], [0]])
    return (M[1][0] % 10007)


def main():
    print(f(int(input())))


if __name__ == '__main__':
    main()
