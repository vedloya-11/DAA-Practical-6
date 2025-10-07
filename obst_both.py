def optimal_bst(keys, p, q, n):

    e = [[0] * (n + 1) for _ in range(n + 2)]
    
    w = [[0] * (n + 1) for _ in range(n + 2)]
    
    root = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for length in range(1, n + 1): 
        for i in range(1, n - length + 2):
            j = i + length - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i, j + 1):
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = r
    return e[1][n]
n = 4
keys = [10, 20, 30, 40]
p = [0.1, 0.2, 0.4, 0.3]    
q = [0.05, 0.1, 0.05, 0.05, 0.1] 

result = optimal_bst(keys, p, q, n)
print("Min Cost :"f"{result:.4f}")
