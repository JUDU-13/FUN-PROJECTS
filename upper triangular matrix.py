def is_upper_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True


def main():
    n = int(input().strip())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))

    result = is_upper_triangular(matrix)
    print(1 if result else 0)


if __name__ == '__main__':
    main()
