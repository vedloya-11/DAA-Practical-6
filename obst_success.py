def obst_success(p, n):
    e = [[0] * n for _ in range(n)]
    w = [[0] * n for _ in range(n)]
    for i in range(n):
        e[i][i] = p[i]
        w[i][i] = p[i]

    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1
            w[i][j] = w[i][j - 1] + p[j]
            e[i][j] = float('inf')

            for r in range(i, j + 1):
                left_cost = e[i][r - 1] if r > i else 0
                right_cost = e[r + 1][j] if r < j else 0
                cost = left_cost + right_cost + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
    return e[0][n - 1]
p = [0.1, 0.2, 0.4, 0.3]
n = len(p)

result = obst_success(p, n)
print("Min cost:"f"{result:.4f}")
