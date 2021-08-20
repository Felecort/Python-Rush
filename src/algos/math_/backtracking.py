

def backtracking():  # Неэффективно на больших задачах NxN, n = 100 - слишком долго
    """ O(n!), o(e^n)
    NP - non polinomial нет решения за полином"""
    pass


def backtracking_queens(row, col, diag1, diag2):
    n = len(col)
    if row == n:
        return 1

    count = 0
    for column in range(n):
        if col[column] == 0 and diag1[column + row] == 0 and diag2[row - column + (n - 1)] == 0:
            col[column] = 1
            diag1[column + row] = 1
            diag2[row - column + (n - 1)] = 1
            count += backtracking_queens(row + 1, col, diag1, diag2)
            col[column] = 0
            diag1[column + row] = 0
            diag2[row - column + (n - 1)] = 0
    return count


n = 13
col = [0 for _ in range(n)]
diag1 = [0 for _ in range(2 * n - 1)]
diag2 = [0 for _ in range(2 * n - 1)]

x = backtracking_queens(0, col, diag1, diag2)
print(x)