def is_upper_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                return False
    return True


def main():
    n = int(input("Enter the size of the matrix: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(
            "Enter row {} elements (separated by space): ".format(i + 1)).strip().split()))
        matrix.append(row)

    result = is_upper_triangular(matrix)
    print("The matrix is upper triangular." if result else "The matrix is not upper triangular.")


if __name__ == '__main__':
    main()
