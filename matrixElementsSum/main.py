def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])

    dp = [1] * m
    r = 0

    for j in range(m):
        for i in range(n):
            if matrix[i][j] == 0:
                dp[j] = 0
            if dp[j] == 1:
                r += matrix[i][j]

    return r


if __name__ == '__main__':
    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]
    print(solution(matrix), 9)
