def matmult(a, b):
    zip_b = list(zip(*b))
    return [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def f(n):
    left = [[1, 2, 1], [1, 0, 0], [0, 1, 0]]
    new = [[1, 2, 1], [1, 0, 0], [0, 1, 0]]
    right = [[2], [1], [0]]
    for _ in range(n - 1):
        new = matmult(new, left)
    final = matmult(new, right)
    return final[2][0]


def main():
    n = int(input())
    result = f(n)
    print(result % 10007)


if __name__ == '__main__':
    main()
