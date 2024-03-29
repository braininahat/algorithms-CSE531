mat = []
pi = []


def gen_mat(len_1, len_2):
    global mat, pi
    mat = [[0 for x in range(len_2 + 1)] for y in range(len_1 + 1)]
    pi = [[0 for x in range(len_2 + 1)] for y in range(len_1 + 1)]


def lcs(charset_a, charset_b):
    global mat, pi
    len_1 = len(charset_a)
    len_2 = len(charset_b)
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if charset_a[i - 1] == charset_b[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
                pi[i][j] = "d"
            else:
                left = mat[i - 1][j]
                right = mat[i][j - 1]
                if left <= right:
                    mat[i][j] = mat[i][j - 1]
                    pi[i][j] = "l"
                else:
                    mat[i][j] = mat[i - 1][j]
                    pi[i][j] = "u"
    i = len_1
    j = len_2
    s = []
    while i > 0 and j > 0:
        if pi[i][j] == "d":
            s.insert(0, charset_a[i-1])
            i -= 1
            j -= 1
        elif pi[i][j] == "u":
            i -= 1
        else:
            j -= 1
    return s


def main():
    string_a = input()
    string_b = input()

    charset_a = list(string_a)
    charset_b = list(string_b)

    len_1 = len(charset_a)
    len_2 = len(charset_b)

    gen_mat(len_1, len_2)

    subsequence = lcs(charset_a, charset_b)

    print(len(subsequence))
    print("".join(subsequence))


if __name__ == '__main__':
    main()
